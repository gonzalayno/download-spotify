# 🎵 Spotify Playlist Downloader

Una aplicación web moderna para descargar playlists de Spotify en formato MP3 de alta calidad (320kbps).

## ✨ Características

- 🎨 Interfaz web moderna y responsive
- 🎵 Descarga playlists completas de Spotify
- 📦 Archivos MP3 de alta calidad (320kbps)
- 📊 Barra de progreso en tiempo real
- 🎯 Descarga individual de canciones (una por una)
- 🖼️ Muestra información de la playlist antes de descargar
- ⚡ Procesamiento asíncrono en segundo plano
- 🚫 Botón de cancelar descarga
- 🔄 Actualización automática de yt-dlp (última versión)

## 🚀 Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- FFmpeg (para conversión de audio)

### Instalar FFmpeg

#### En Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### En macOS:
```bash
brew install ffmpeg
```

#### En Windows:
Descarga desde [ffmpeg.org](https://ffmpeg.org/download.html) y añade al PATH.

### Configuración

1. **Clona o descarga este repositorio**

2. **Crea un entorno virtual (recomendado):**
```bash
python3 -m venv venv
source venv/bin/activate  # En Linux/macOS
# o
venv\Scripts\activate  # En Windows
```

3. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

4. **Configura las credenciales de Spotify:**

   a. Ve a [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   
   b. Inicia sesión con tu cuenta de Spotify
   
   c. Haz clic en "Create an App"
   
   d. Completa el formulario:
      - App name: Spotify Downloader (o el nombre que prefieras)
      - App description: Aplicación para descargar playlists
      - Marca las casillas de aceptación
   
   e. Una vez creada, verás tu **Client ID** y **Client Secret**
   
   f. Copia el archivo `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
   
   g. Edita el archivo `.env` y añade tus credenciales:
   ```
   SPOTIFY_CLIENT_ID=tu_client_id_real
   SPOTIFY_CLIENT_SECRET=tu_client_secret_real
   ```

## 🎮 Uso

1. **Inicia el servidor:**
```bash
python app.py
```

2. **Abre tu navegador y ve a:**
```
http://localhost:5000
```

3. **Descarga una playlist:**
   - Abre Spotify y busca una playlist
   - Haz clic en los tres puntos (...) > Compartir > Copiar enlace de la playlist
   - Pega la URL en la aplicación web
   - Haz clic en "Obtener Información"
   - Verifica que sea la playlist correcta
   - Haz clic en "Descargar Playlist"
   - Observa el progreso en tiempo real
   - Las canciones se descargan automáticamente una por una

## 📁 Estructura del Proyecto

```
spotify_downloader/
├── app.py                 # Servidor Flask (backend)
├── templates/
│   └── index.html        # Interfaz web (frontend)
├── downloads/            # Carpeta de descargas (se crea automáticamente)
├── requirements.txt      # Dependencias de Python
├── .env.example         # Plantilla de variables de entorno
├── .gitignore           # Archivos ignorados por Git
└── README.md            # Este archivo
```

## 🔧 Tecnologías Utilizadas

### Backend
- **Flask**: Framework web de Python
- **yt-dlp**: Descarga de audio de YouTube (última versión 2025.10.14)
- **spotipy**: Cliente de la API de Spotify
- **Flask-CORS**: Manejo de CORS para peticiones cross-origin
- **FFmpeg**: Conversión de audio a MP3

### Frontend
- **HTML5**: Estructura de la página
- **CSS3**: Estilos modernos con gradientes y animaciones
- **JavaScript**: Interactividad y comunicación con el backend

## ⚠️ Notas Importantes

1. **Uso Legal**: Esta herramienta está diseñada para uso personal. Asegúrate de tener los derechos necesarios para descargar el contenido.

2. **Rendimiento**: La velocidad de descarga depende de:
   - Tu conexión a internet
   - El número de canciones en la playlist
   - La disponibilidad de las canciones en YouTube (spotdl busca en YouTube)

3. **Limitaciones**:
   - Las canciones que no estén disponibles públicamente no se podrán descargar
   - Algunas canciones pueden tener nombres o metadatos ligeramente diferentes

## 🐛 Solución de Problemas

### Error: "FFmpeg not found"
Asegúrate de tener FFmpeg instalado y en tu PATH.

### Error: "Invalid credentials"
Verifica que tus credenciales de Spotify en el archivo `.env` sean correctas.

### Las canciones no se descargan
- Verifica tu conexión a internet
- Comprueba que la playlist sea pública
- Algunos contenidos pueden no estar disponibles

### El servidor no inicia
- Verifica que el puerto 5000 esté disponible
- Asegúrate de haber activado el entorno virtual
- Comprueba que todas las dependencias estén instaladas

## 🌐 Despliegue Gratuito

Para poner tu aplicación en internet **completamente gratis**, consulta la **[Guía de Despliegue Gratuito](DESPLIEGUE_GRATUITO.md)**.

### Opciones Disponibles:
- 🚀 **Railway** (Recomendado) - Más fácil de usar
- 🎯 **Render** - Más estable para producción  
- ⚡ **Heroku** - Muy conocido (limitado)
- 🔥 **Vercel** - Muy rápido (para desarrollo)

### Pasos Rápidos:
1. **Fork este repositorio** en GitHub
2. **Elige una plataforma** (Railway es la más fácil)
3. **Configura las variables de entorno**
4. **¡Despliega!** - Obtén tu URL pública
5. **¡Comparte!** - Cualquier persona puede usar tu app

📖 **[Ver guía completa de despliegue](DESPLIEGUE_GRATUITO.md)**

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún bug o tienes alguna sugerencia, no dudes en abrir un issue.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso personal.

## 🙏 Agradecimientos

- [spotdl](https://github.com/spotDL/spotify-downloader) - Por la excelente librería de descarga
- [Spotify API](https://developer.spotify.com/) - Por la API de Spotify
- [Flask](https://flask.palletsprojects.com/) - Por el framework web

---

**Nota**: Esta aplicación descarga audio de YouTube basándose en los metadatos de Spotify. No descarga directamente de Spotify.

