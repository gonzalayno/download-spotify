@echo off
REM Script de inicio rápido para Spotify Downloader (Windows)

echo 🎵 Spotify Playlist Downloader - Script de Inicio
echo ==================================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado
    echo    Instala Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Verificar si el entorno virtual existe
if not exist "venv\" (
    echo 📦 Creando entorno virtual...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Error al crear el entorno virtual
        pause
        exit /b 1
    )
    echo ✅ Entorno virtual creado
)

REM Activar entorno virtual
echo 🔧 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Verificar si las dependencias están instaladas
if not exist "venv\Lib\site-packages\flask\" (
    echo 📦 Instalando dependencias...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Error al instalar dependencias
        pause
        exit /b 1
    )
    echo ✅ Dependencias instaladas
)

REM Verificar si existe el archivo .env
if not exist ".env" (
    echo.
    echo ⚠️  No se encontró el archivo .env
    echo    Ejecutando script de configuración...
    echo.
    python setup.py
    
    if not exist ".env" (
        echo.
        echo ❌ No se pudo crear el archivo .env
        echo    Por favor, crea manualmente un archivo .env con:
        echo    SPOTIFY_CLIENT_ID=tu_client_id
        echo    SPOTIFY_CLIENT_SECRET=tu_client_secret
        pause
        exit /b 1
    )
)

REM Iniciar la aplicación
echo.
echo 🚀 Iniciando servidor...
echo.
python app.py

pause

