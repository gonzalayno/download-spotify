#!/bin/bash

# Script de inicio rápido para Spotify Downloader

echo "🎵 Spotify Playlist Downloader - Script de Inicio"
echo "=================================================="
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "   Instala Python 3 desde: https://www.python.org/downloads/"
    exit 1
fi

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "❌ Error al crear el entorno virtual"
        exit 1
    fi
    echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Verificar si las dependencias están instaladas
if [ ! -f "venv/lib/python*/site-packages/flask/__init__.py" ]; then
    echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Error al instalar dependencias"
        exit 1
    fi
    echo "✅ Dependencias instaladas"
fi

# Verificar si existe el archivo .env
if [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  No se encontró el archivo .env"
    echo "   Ejecutando script de configuración..."
    echo ""
    python setup.py
    
    if [ ! -f ".env" ]; then
        echo ""
        echo "❌ No se pudo crear el archivo .env"
        echo "   Por favor, crea manualmente un archivo .env con:"
        echo "   SPOTIFY_CLIENT_ID=tu_client_id"
        echo "   SPOTIFY_CLIENT_SECRET=tu_client_secret"
        exit 1
    fi
fi

# Iniciar la aplicación
echo ""
echo "🚀 Iniciando servidor..."
echo ""
python app.py
