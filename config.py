"""
Configuración de la aplicación
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    """Configuración de la aplicación"""
    
    # Spotify API
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID', '')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET', '')
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    
    # Descargas
    DOWNLOAD_FOLDER = os.getenv('DOWNLOAD_FOLDER', 'downloads')
    MAX_PLAYLIST_SIZE = int(os.getenv('MAX_PLAYLIST_SIZE', 500))  # Máximo de canciones
    
    # Audio
    AUDIO_FORMAT = os.getenv('AUDIO_FORMAT', 'mp3')
    AUDIO_BITRATE = os.getenv('AUDIO_BITRATE', '320k')
    
    @staticmethod
    def validate():
        """Validar que la configuración sea correcta"""
        errors = []
        
        if not Config.SPOTIFY_CLIENT_ID:
            errors.append("SPOTIFY_CLIENT_ID no está configurado")
        
        if not Config.SPOTIFY_CLIENT_SECRET:
            errors.append("SPOTIFY_CLIENT_SECRET no está configurado")
        
        return errors

def print_config_errors():
    """Imprimir errores de configuración si los hay"""
    errors = Config.validate()
    
    if errors:
        print("\n⚠️  ERRORES DE CONFIGURACIÓN:")
        for error in errors:
            print(f"  ❌ {error}")
        print("\n📖 Para configurar las credenciales:")
        print("  1. Ejecuta: python setup.py")
        print("  2. O crea un archivo .env con tus credenciales")
        print("  3. Obtén credenciales en: https://developer.spotify.com/dashboard")
        print()
        return False
    
    return True

