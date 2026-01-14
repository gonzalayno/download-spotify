from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import threading
import uuid
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from pathlib import Path
import shutil
import yt_dlp
from config import Config, print_config_errors

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Configuración
DOWNLOAD_FOLDER = Config.DOWNLOAD_FOLDER
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Estado de descargas
download_status = {}

# Configuración de yt-dlp
def get_ytdl_opts(output_dir):
    return {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'extract_flat': False,
        'writethumbnail': False,
        'writeinfojson': False,
        'extractor_args': {'youtube': {'player_client': ['android', 'web']}},
        'paths': {'home': output_dir},
    }

# Función para cancelar descarga
def cancel_download(download_id):
    """Cancelar una descarga en progreso"""
    if download_id in download_status:
        download_status[download_id]['status'] = 'cancelled'
        download_status[download_id]['message'] = 'Descarga cancelada por el usuario'

def get_spotify_client():
    """Inicializar cliente de Spotify"""
    if not Config.SPOTIFY_CLIENT_ID or not Config.SPOTIFY_CLIENT_SECRET:
        return None
    
    try:
        auth_manager = SpotifyClientCredentials(
            client_id=Config.SPOTIFY_CLIENT_ID,
            client_secret=Config.SPOTIFY_CLIENT_SECRET
        )
        return spotipy.Spotify(auth_manager=auth_manager)
    except Exception as e:
        print(f"Error al inicializar cliente de Spotify: {e}")
        return None

def download_playlist(playlist_url, download_id, custom_folder=None):
    """Función para descargar playlist en segundo plano"""
    try:
        download_status[download_id]['status'] = 'processing'
        download_status[download_id]['message'] = 'Iniciando descarga...'
        
        # Usar carpeta personalizada si se proporciona, sino usar la carpeta por defecto
        if custom_folder and custom_folder.strip():
            # Validar y crear la carpeta personalizada
            custom_folder = os.path.abspath(custom_folder.strip())
            if not os.path.exists(custom_folder):
                os.makedirs(custom_folder, exist_ok=True)
            base_folder = custom_folder
        else:
            base_folder = DOWNLOAD_FOLDER
        
        # Crear carpeta específica para esta descarga
        download_path = os.path.join(base_folder, download_id)
        os.makedirs(download_path, exist_ok=True)
        
        # Guardar la ruta de descarga en el estado para poder acceder a los archivos después
        download_status[download_id]['download_path'] = download_path
        
        # Configurar spotdl con la nueva API
        # Configuración completada
        
        # Obtener información de la playlist usando Spotify API
        download_status[download_id]['message'] = 'Obteniendo información de la playlist...'
        
        # Usar Spotify API para obtener canciones
        sp = get_spotify_client()
        if not sp:
            raise Exception("No se pudo conectar a Spotify API")
        
        # Extraer ID de la playlist
        if 'playlist/' in playlist_url:
            playlist_id = playlist_url.split('playlist/')[1].split('?')[0]
        else:
            raise Exception("URL de playlist inválida")
        
        # Obtener canciones de la playlist (con paginación para obtener todas)
        playlist = sp.playlist(playlist_id)
        songs = []
        
        # Obtener todas las canciones usando paginación
        results = playlist['tracks']
        while results:
            for track in results['items']:
                if track['track'] and track['track']['name']:
                    song_info = {
                        'name': track['track']['name'],
                        'artist': ', '.join([artist['name'] for artist in track['track']['artists']]),
                        'url': f"ytsearch:{track['track']['name']} {', '.join([artist['name'] for artist in track['track']['artists']])}"
                    }
                    songs.append(song_info)
            
            # Obtener siguiente página si existe
            if results['next']:
                results = sp.next(results)
            else:
                break
        
        total_songs = len(songs)
        download_status[download_id]['total'] = total_songs
        download_status[download_id]['current'] = 0
        
        # Descargar canciones con la nueva API
        for idx, song in enumerate(songs, 1):
            # Verificar si la descarga fue cancelada
            if download_status[download_id]['status'] == 'cancelled':
                break
                
            download_status[download_id]['message'] = f'Descargando: {song["name"]} - {song["artist"]}'
            download_status[download_id]['current'] = idx
            download_status[download_id]['current_song'] = f'{song["name"]} - {song["artist"]}'
            
            try:
                # Usar yt-dlp para descargar
                ytdl_opts = get_ytdl_opts(download_path)
                with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
                    ydl.download([song['url']])
                
                # Buscar archivos descargados en todo el directorio (incluyendo subdirectorios)
                files_in_dir = []
                for root, dirs, files in os.walk(download_path):
                    for file in files:
                        if file.endswith(('.mp3', '.m4a', '.webm')):
                            file_path = os.path.join(root, file)
                            # Mover archivo al directorio principal si está en subdirectorio
                            if root != download_path:
                                new_path = os.path.join(download_path, file)
                                if not os.path.exists(new_path):
                                    shutil.move(file_path, new_path)
                                files_in_dir.append(file)
                            else:
                                files_in_dir.append(file)
                
                if files_in_dir:
                    download_status[download_id]['message'] = f'Completado: {song["name"]} - {song["artist"]}'
                else:
                    download_status[download_id]['message'] = f'Advertencia: {song["name"]} no se descargó correctamente'
                
            except Exception as e:
                download_status[download_id]['message'] = f'Error descargando {song["name"]}: {str(e)}'
                continue
        
        # Verificar archivos descargados (incluyendo subdirectorios)
        files_in_dir = []
        for root, dirs, files in os.walk(download_path):
            for file in files:
                if file.endswith(('.mp3', '.m4a', '.webm')):
                    files_in_dir.append(file)
        
        download_status[download_id]['message'] = f'Descarga completada - {len(files_in_dir)} canciones listas'
        download_status[download_id]['downloaded_files'] = files_in_dir
        
        if download_status[download_id]['status'] != 'cancelled':
            download_status[download_id]['status'] = 'completed'
            download_status[download_id]['can_cancel'] = False
        
    except Exception as e:
        if download_status[download_id]['status'] != 'cancelled':
            download_status[download_id]['status'] = 'error'
            download_status[download_id]['message'] = f'Error: {str(e)}'
            download_status[download_id]['can_cancel'] = False

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/playlist-info', methods=['POST'])
def get_playlist_info():
    """Obtener información de la playlist"""
    try:
        data = request.json
        playlist_url = data.get('playlist_url')
        
        if not playlist_url:
            return jsonify({'error': 'URL de playlist requerida'}), 400
        
        # Extraer ID de la playlist
        if 'playlist/' in playlist_url:
            playlist_id = playlist_url.split('playlist/')[1].split('?')[0]
        else:
            return jsonify({'error': 'URL de playlist inválida'}), 400
        
        # Obtener información de Spotify
        sp = get_spotify_client()
        if sp:
            playlist = sp.playlist(playlist_id)
            return jsonify({
                'name': playlist['name'],
                'owner': playlist['owner']['display_name'],
                'tracks': playlist['tracks']['total'],
                'image': playlist['images'][0]['url'] if playlist['images'] else None,
                'description': playlist.get('description', '')
            })
        else:
            # Si no hay credenciales, devolver error
            return jsonify({'error': 'Credenciales de Spotify no configuradas'}), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download', methods=['POST'])
def start_download():
    """Iniciar descarga de playlist"""
    try:
        data = request.json
        playlist_url = data.get('playlist_url')
        custom_folder = data.get('custom_folder')  # Carpeta personalizada
        
        if not playlist_url:
            return jsonify({'error': 'URL de playlist requerida'}), 400
        
        # Generar ID único para la descarga
        download_id = str(uuid.uuid4())
        
        # Inicializar estado
        download_status[download_id] = {
            'status': 'queued',
            'message': 'En cola...',
            'current': 0,
            'total': 0,
            'current_song': '',
            'can_cancel': True
        }
        
        # Iniciar descarga en segundo plano
        thread = threading.Thread(
            target=download_playlist,
            args=(playlist_url, download_id, custom_folder)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            'download_id': download_id,
            'message': 'Descarga iniciada'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<download_id>', methods=['GET'])
def get_status(download_id):
    """Obtener estado de la descarga"""
    if download_id not in download_status:
        return jsonify({'error': 'Descarga no encontrada'}), 404
    
    return jsonify(download_status[download_id])

@app.route('/api/cancel/<download_id>', methods=['POST'])
def cancel_download_endpoint(download_id):
    """Cancelar una descarga"""
    try:
        cancel_download(download_id)
        return jsonify({'message': 'Descarga cancelada'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/download-file/<download_id>/<filename>', methods=['GET'])
def download_file(download_id, filename):
    """Descargar archivo individual"""
    try:
        # Obtener la ruta de descarga guardada en el estado
        if download_id in download_status and 'download_path' in download_status[download_id]:
            download_path = download_status[download_id]['download_path']
            file_path = os.path.join(download_path, filename)
        else:
            # Fallback: buscar en la carpeta por defecto
            file_path = os.path.join(DOWNLOAD_FOLDER, download_id, filename)
        
        if not os.path.exists(file_path):
            # Si no está ahí, buscar en todas las subcarpetas
            search_path = download_path if download_id in download_status and 'download_path' in download_status[download_id] else DOWNLOAD_FOLDER
            for root, dirs, files in os.walk(search_path):
                if download_id in root and filename in files:
                    file_path = os.path.join(root, filename)
                    break
        
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename
            )
        else:
            return jsonify({'error': 'Archivo no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    
    print("\n" + "="*60)
    print("🎵  SPOTIFY PLAYLIST DOWNLOADER")
    print("="*60)
    
    # Verificar configuración
    if not print_config_errors():
        print("❌ No se puede iniciar el servidor sin configuración válida.")
        print("   Ejecuta: python setup.py")
        exit(1)
    
    print("\n✅ Configuración válida")
    
    # Configuración para Railway
    port = int(os.environ.get('PORT', Config.PORT))
    host = os.environ.get('HOST', Config.HOST)
    
    print(f"📍 Servidor iniciando en: http://{host}:{port}")
    print(f"🎧 Formato de audio: {Config.AUDIO_FORMAT} @ {Config.AUDIO_BITRATE}")
    print("\n💡 Presiona Ctrl+C para detener el servidor")
    print("="*60 + "\n")
    
    app.run(
        debug=Config.DEBUG,
        host=host,
        port=port
    )

