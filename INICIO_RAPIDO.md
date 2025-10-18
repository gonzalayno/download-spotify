# 🚀 Guía de Inicio Rápido

Esta guía te ayudará a poner en marcha el **Spotify Playlist Downloader** en menos de 5 minutos.

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado:

- ✅ **Python 3.8 o superior** - [Descargar aquí](https://www.python.org/downloads/)
- ✅ **FFmpeg** - Necesario para conversión de audio

### Instalar FFmpeg

**En Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**En macOS:**
```bash
brew install ffmpeg
```

**En Windows:**
1. Descarga desde [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extrae el archivo
3. Añade la carpeta `bin` al PATH del sistema

## 🎯 Instalación en 3 Pasos

### 1️⃣ Instalar Dependencias

**Linux/macOS:**
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

**Windows:**
```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2️⃣ Configurar Credenciales de Spotify

**Opción A: Usar el script de configuración (Recomendado)**
```bash
python setup.py
```
El script te guiará paso a paso.

**Opción B: Configuración manual**
1. Ve a https://developer.spotify.com/dashboard
2. Crea una aplicación
3. Copia el Client ID y Client Secret
4. Crea un archivo `.env` con:
```
SPOTIFY_CLIENT_ID=tu_client_id_aqui
SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui
```

📖 **[Ver guía detallada](INSTRUCCIONES_SPOTIFY_API.md)**

### 3️⃣ Iniciar el Servidor

**Método 1: Script automático**

Linux/macOS:
```bash
./start.sh
```

Windows:
```cmd
start.bat
```

**Método 2: Manual**
```bash
python app.py
```

## 🎵 Usar la Aplicación

1. **Abre tu navegador** en: http://localhost:5000

2. **Obtén el enlace de una playlist de Spotify:**
   - Abre Spotify (web o app)
   - Busca cualquier playlist
   - Haz clic en los tres puntos (...) junto al nombre de la playlist
   - Selecciona "Compartir" → "Copiar enlace de la playlist"
   - El enlace se ve así: `https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M`

3. **Descarga la playlist:**
   - Pega el enlace en la aplicación web
   - Haz clic en "Obtener Información"
   - Verifica que sea la playlist correcta
   - Haz clic en "Descargar Playlist"
   - Observa el progreso en tiempo real
   - Las canciones se descargan automáticamente una por una

## 📁 ¿Dónde están mis descargas?

Las canciones se descargan automáticamente en tu navegador:
- 🎵 **Descarga individual**: Cada canción se descarga por separado
- 📱 **Directamente al navegador**: No necesitas buscar archivos
- 🎯 **Formato MP3**: Audio de alta calidad (320kbps)
- ⚡ **Progreso en vivo**: Ve qué canción se está descargando

## 🔧 Solución Rápida de Problemas

### ❌ Error: "FFmpeg not found"
**Solución:** Instala FFmpeg (ver arriba)

### ❌ Error: "Invalid credentials"
**Solución:** 
1. Verifica que el archivo `.env` exista
2. Comprueba que las credenciales sean correctas
3. Ejecuta `python setup.py` para reconfigurar

### ❌ Error: "Module not found"
**Solución:**
```bash
pip install -r requirements.txt
```

### ❌ El servidor no inicia
**Solución:**
1. Verifica que Python esté instalado: `python --version`
2. Activa el entorno virtual
3. Instala dependencias
4. Verifica que el puerto 5000 esté libre

### ❌ Las canciones no se descargan
**Causas posibles:**
- La playlist es privada (debe ser pública)
- No tienes conexión a internet
- Las canciones no están disponibles en YouTube

## 📊 Características

✅ Descarga playlists completas  
✅ Formato MP3 de alta calidad (320kbps)  
✅ Metadatos automáticos (artista, título, álbum)  
✅ Barra de progreso en tiempo real  
✅ Descarga individual de canciones  
✅ Botón de cancelar descarga  
✅ Interfaz web moderna y fácil de usar  
✅ yt-dlp actualizado (última versión)  

## 🎓 Ejemplos de Playlists

Prueba con estas playlists públicas de Spotify:

- **Top 50 Global**: https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF
- **Rock Classics**: https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U
- **Chill Vibes**: https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6

## 🔒 Seguridad

- ✅ Todas las descargas se procesan localmente en tu computadora
- ✅ No se comparten datos con terceros
- ✅ Tus credenciales de Spotify permanecen seguras
- ⚠️ **NUNCA** compartas tu archivo `.env` o tu Client Secret

## 🌐 Despliegue Gratuito (Para Compartir)

### 🚀 Railway (Más Fácil)
1. **Fork este repositorio** en GitHub
2. **Ve a [Railway.app](https://railway.app)** y conéctate con GitHub
3. **Selecciona tu fork** del repositorio
4. **Configura las variables:**
   - `SPOTIFY_CLIENT_ID`: Tu Client ID
   - `SPOTIFY_CLIENT_SECRET`: Tu Client Secret
5. **¡Despliega!** - Railway creará tu URL pública

### 🎯 Render (Alternativa)
1. **Fork este repositorio** en GitHub
2. **Ve a [Render.com](https://render.com)** y conéctate con GitHub
3. **Crea un Web Service**
4. **Configura:**
   - Build: `pip install -r requirements.txt`
   - Start: `python app.py`
   - Variables: `SPOTIFY_CLIENT_ID` y `SPOTIFY_CLIENT_SECRET`
5. **¡Despliega!** - Render creará tu URL pública

### 💡 Consejos para Despliegue
- **Railway** es más fácil para principiantes
- **Render** es más estable para producción
- **Ambos son gratuitos** para uso personal
- **Tu app estará disponible 24/7** en internet

## 📞 ¿Necesitas Ayuda?

1. Lee el [README.md](README.md) completo
2. Consulta las [instrucciones de Spotify API](INSTRUCCIONES_SPOTIFY_API.md)
3. Verifica la lista de solución de problemas arriba

## 💡 Consejos

- Para playlists grandes (100+ canciones), la descarga puede tardar varios minutos
- Asegúrate de tener suficiente espacio en disco
- La calidad de las canciones depende de la disponibilidad en YouTube
- Puedes descargar múltiples playlists (se procesan en segundo plano)

---

¡Listo! 🎉 Ahora puedes descargar todas tus playlists favoritas de Spotify.

**Disfruta tu música** 🎵

