const express = require('express');
const bodyParser = require('body-parser');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.set('view engine', 'ejs');

let clients = []; // Clientes conectados a los logs

// Ruta principal
app.get('/', (req, res) => {
    res.render('index');
});

// Ruta para enviar logs en tiempo real
app.get('/logs', (req, res) => {
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    clients.push(res);

    req.on('close', () => {
        clients = clients.filter(client => client !== res);
    });
});

// Función para enviar logs en tiempo real
function sendLog(message) {
    clients.forEach(client => client.write(`data: ${message}\n\n`));
}

// Ruta para manejar la descarga
app.post('/download', (req, res) => {
    const { url, format, path: downloadPath } = req.body;

    if (!url || !format || !downloadPath) {
        return res.status(400).send('Faltan parámetros');
    }

    const fullDownloadPath = path.join(downloadPath, '%(title)s.%(ext)s');

    // Ejecutar spotdl con el formato y la ruta seleccionadossvcvc
    const downloadProcess = spawn('spotdl', ['--cookie-file','cookies.json','--log-level' ,'DEBUG','download', url, '--format', format, '--output', '/home/glayno/Descargas/testing_musica']);

    downloadProcess.stdout.on('data', (data) => {
        console.log(`Salida: ${data}`);
        sendLog(data.toString());
    });

    downloadProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
        sendLog(`ERROR: ${data.toString()}`);
    });

    downloadProcess.on('close', (code) => {
        sendLog(`Proceso finalizado con código ${code}`);
    });

    res.status(200).send('Descarga iniciada, revisa el log en la página.');
});

// Iniciar el servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
