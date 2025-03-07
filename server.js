const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const os = require('os');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');
app.use(express.static('public'));

let clients = []; // Clientes conectados a los logs

// Directorios configurables

// Función para obtener archivo de cookies
function prepareCookiesFile() {
    // Verificar si hay un archivo local
    const localCookiesPath = path.join(__dirname, 'www.youtube.com_cookies.txt');
    return localCookiesPath;
    }


// Ruta principal
app.get('/', (req, res) => res.render('index'));

// Logs en tiempo real
app.get('/logs', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    clients.push(res);
    req.on('close', () => clients = clients.filter(client => client !== res));
});

// Función para enviar logs
function sendLog(message) {
    clients.forEach(client => client.write(`data: ${message}\n\n`));
}

// Subida de cookies
app.post('/upload-cookies', (req, res) => {
    if (!req.body.cookiesContent) return res.status(400).send('No se proporcionó contenido de cookies');

    const cookiesPath = path.join(COOKIES_DIR, 'youtube_cookies.txt');
    fs.writeFileSync(cookiesPath, req.body.cookiesContent);
    res.status(200).send('Cookies actualizadas correctamente');
});

// Descarga de música
app.post('/download', (req, res) => {
    const { url, format } = req.body;
    const downloadPath = req.body.path || DOWNLOADS_DIR;

    if (!url || !format) return res.status(400).send('Faltan parámetros');

    if (!fs.existsSync(downloadPath)) {
        try {
            fs.mkdirSync(downloadPath, { recursive: true });
        } catch (error) {
            console.error(`❌ Error creando directorio: ${error.message}`);
            return res.status(500).send(`Error creando directorio: ${error.message}`);
        }
    }

    const fullDownloadPath = path.join(downloadPath, '%(title)s.%(ext)s');
    const cookiesFilePath = prepareCookiesFile();

    if (!cookiesFilePath) return res.status(500).send('No se encontró un archivo de cookies válido');

    // Ejecutar `yt-dlp` en lugar de `spotdl` para autenticación
    // Configurar argumentos para spotdl
    const spotdlArgs = [
        '--cookie-file', 'www.youtube.com_cookies.txt',
        'download', url,
        '--format', format,
        '--output', path.join(downloadPath, '%(title)s.%(ext)s')
    ];
    
    sendLog(`Iniciando descarga de: ${url}`);
    sendLog(`Usando cookies de: ${cookiesFilePath}`);
    sendLog(`Guardando en: ${downloadPath}`);
    
    // Ejecutar spotdl con el formato y la ruta seleccionados
    const downloadProcess = spawn('spotdl', spotdlArgs);

    downloadProcess.stdout.on('data', (data) => sendLog(data.toString()));
    downloadProcess.stderr.on('data', (data) => sendLog(`❌ ERROR: ${data.toString()}`));

    downloadProcess.on('close', (code) => {
        sendLog(code === 0 ? '✅ Descarga completada exitosamente' : `⚠️ Proceso finalizado con código ${code}`);
    });

    res.status(200).send('Descarga iniciada, revisa el log en la página.');
});

// Actualizar `yt-dlp`
app.post('/update-ytdlp', (req, res) => {
    const updateProcess = spawn('yt-dlp', ['-U']);

    updateProcess.stdout.on('data', (data) => sendLog(`🔄 Actualización yt-dlp: ${data.toString()}`));
    updateProcess.stderr.on('data', (data) => sendLog(`❌ ERROR de actualización: ${data.toString()}`));

    updateProcess.on('close', (code) => {
        sendLog(`✅ yt-dlp actualizado con código ${code}`);
        res.status(200).send(`yt-dlp actualizado con código ${code}`);
    });
});

// Iniciar servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`));
