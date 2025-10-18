#!/usr/bin/env python3
"""
Script de configuración para Spotify Downloader
Este script ayuda a configurar las credenciales de Spotify
"""

import os
from pathlib import Path

def create_env_file():
    """Crear archivo .env con credenciales de Spotify"""
    print("🎵 Configuración de Spotify Downloader")
    print("=" * 50)
    print()
    print("Para usar esta aplicación, necesitas credenciales de Spotify API.")
    print("Sigue estos pasos:")
    print()
    print("1. Ve a: https://developer.spotify.com/dashboard")
    print("2. Inicia sesión con tu cuenta de Spotify")
    print("3. Haz clic en 'Create an App'")
    print("4. Completa el formulario y crea la aplicación")
    print("5. Copia el 'Client ID' y 'Client Secret'")
    print()
    
    # Verificar si ya existe .env
    env_file = Path(".env")
    if env_file.exists():
        overwrite = input("Ya existe un archivo .env. ¿Deseas sobrescribirlo? (s/N): ")
        if overwrite.lower() not in ['s', 'si', 'sí', 'yes', 'y']:
            print("Configuración cancelada.")
            return
    
    # Solicitar credenciales
    print()
    client_id = input("Ingresa tu SPOTIFY_CLIENT_ID: ").strip()
    client_secret = input("Ingresa tu SPOTIFY_CLIENT_SECRET: ").strip()
    
    if not client_id or not client_secret:
        print("❌ Error: Debes proporcionar ambas credenciales.")
        return
    
    # Crear archivo .env
    with open(".env", "w") as f:
        f.write("# Credenciales de Spotify API\n")
        f.write("# Generado automáticamente por setup.py\n\n")
        f.write(f"SPOTIFY_CLIENT_ID={client_id}\n")
        f.write(f"SPOTIFY_CLIENT_SECRET={client_secret}\n")
    
    print()
    print("✅ Archivo .env creado correctamente!")
    print()
    print("Ahora puedes ejecutar la aplicación con: python app.py")

def check_dependencies():
    """Verificar que todas las dependencias estén instaladas"""
    print("\n🔍 Verificando dependencias...")
    
    dependencies = [
        'flask',
        'flask_cors',
        'spotdl',
        'spotipy',
        'dotenv'
    ]
    
    missing = []
    for dep in dependencies:
        try:
            __import__(dep if dep != 'dotenv' else 'dotenv')
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ❌ {dep} - NO INSTALADO")
            missing.append(dep)
    
    if missing:
        print("\n⚠️  Dependencias faltantes. Instálalas con:")
        print("  pip install -r requirements.txt")
        return False
    else:
        print("\n✅ Todas las dependencias están instaladas!")
        return True

def check_ffmpeg():
    """Verificar que FFmpeg esté instalado"""
    print("\n🔍 Verificando FFmpeg...")
    import subprocess
    
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, 
                              text=True)
        if result.returncode == 0:
            print("  ✅ FFmpeg está instalado")
            return True
        else:
            print("  ❌ FFmpeg no está instalado correctamente")
            return False
    except FileNotFoundError:
        print("  ❌ FFmpeg no está instalado")
        print("\n  Instala FFmpeg:")
        print("  - Ubuntu/Debian: sudo apt install ffmpeg")
        print("  - macOS: brew install ffmpeg")
        print("  - Windows: https://ffmpeg.org/download.html")
        return False

if __name__ == "__main__":
    print()
    
    # Verificar dependencias
    deps_ok = check_dependencies()
    
    # Verificar FFmpeg
    ffmpeg_ok = check_ffmpeg()
    
    if deps_ok and ffmpeg_ok:
        print("\n" + "=" * 50)
        create_env_file()
    else:
        print("\n⚠️  Por favor, resuelve los problemas anteriores antes de continuar.")

