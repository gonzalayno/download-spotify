# 🔑 Cómo Obtener Credenciales de Spotify API

Esta guía te ayudará a obtener las credenciales necesarias para usar el Spotify Downloader.

## Paso 1: Ir al Dashboard de Desarrolladores

1. Abre tu navegador web
2. Ve a: **https://developer.spotify.com/dashboard**
3. Si no has iniciado sesión, haz clic en "Log In" e inicia sesión con tu cuenta de Spotify
   - Si no tienes cuenta de Spotify, crea una gratis en https://www.spotify.com/signup

## Paso 2: Crear una Aplicación

1. Una vez en el dashboard, haz clic en el botón verde **"Create app"** (Crear aplicación)

2. Completa el formulario con la siguiente información:
   ```
   App name: Spotify Downloader
   App description: Aplicación para descargar playlists de Spotify
   Website: http://localhost:5000
   Redirect URIs: http://localhost:5000/callback
   ```

3. Marca las casillas de verificación:
   - ✅ Acepto los Términos de Servicio de Spotify
   - ✅ Entiendo que el uso de la API está sujeto a las Políticas de Desarrolladores

4. Haz clic en **"Save"** (Guardar)

## Paso 3: Obtener las Credenciales

1. Después de crear la app, serás redirigido a la página de configuración de tu aplicación

2. Verás dos campos importantes:
   - **Client ID**: Una cadena de caracteres única (ej: `a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6`)
   - **Client Secret**: Haz clic en "Show Client Secret" para verla

3. **IMPORTANTE**: Guarda estas credenciales de forma segura:
   - ⚠️ No compartas tu Client Secret con nadie
   - ⚠️ No las subas a repositorios públicos de Git

## Paso 4: Configurar la Aplicación

### Opción A: Usando el Script de Configuración (Recomendado)

1. Ejecuta el script de configuración:
   ```bash
   python setup.py
   ```

2. Cuando se te solicite, pega:
   - Tu Client ID
   - Tu Client Secret

3. El script creará automáticamente el archivo `.env`

### Opción B: Manualmente

1. Crea un archivo llamado `.env` en la carpeta del proyecto

2. Añade las siguientes líneas (reemplaza con tus credenciales reales):
   ```
   SPOTIFY_CLIENT_ID=tu_client_id_real_aqui
   SPOTIFY_CLIENT_SECRET=tu_client_secret_real_aqui
   ```

3. Guarda el archivo

## Paso 5: Verificar la Configuración

1. Inicia el servidor:
   ```bash
   python app.py
   ```

2. Si todo está bien, verás:
   ```
   ✅ Configuración válida
   📍 Servidor iniciando en: http://0.0.0.0:5000
   ```

3. Si hay un error, verás:
   ```
   ❌ SPOTIFY_CLIENT_ID no está configurado
   ```
   En ese caso, revisa que hayas copiado correctamente las credenciales.

## Solución de Problemas

### Error: "Invalid client"
- Verifica que hayas copiado correctamente el Client ID y Client Secret
- Asegúrate de no haber incluido espacios al principio o al final

### Error: "Client credentials not found"
- Confirma que el archivo `.env` esté en la carpeta raíz del proyecto
- Verifica que el archivo se llame exactamente `.env` (sin extensión adicional)

### No puedo ver el archivo .env
- En Linux/macOS, los archivos que empiezan con `.` son ocultos
- Usa `ls -la` en la terminal para verlos
- O habilita "Mostrar archivos ocultos" en tu explorador de archivos

## Límites de la API de Spotify

La API de Spotify tiene límites de uso:
- **Rate Limit**: Aproximadamente 100 peticiones por segundo
- **Cuota diaria**: Varía según el tipo de cuenta

Para uso personal normal, estos límites son más que suficientes.

## Seguridad

**IMPORTANTE**: 
- ❌ NUNCA compartas tu Client Secret públicamente
- ❌ NUNCA subas el archivo `.env` a Git (ya está en `.gitignore`)
- ✅ Si crees que tu secret ha sido comprometido, regenera una nueva en el dashboard
- ✅ Trata estas credenciales como contraseñas

## Más Información

- Documentación oficial de Spotify API: https://developer.spotify.com/documentation/web-api
- Guía de autenticación: https://developer.spotify.com/documentation/general/guides/authorization/

---

¿Necesitas ayuda? Verifica que:
1. ✅ Hayas iniciado sesión en Spotify
2. ✅ Hayas creado una aplicación en el dashboard
3. ✅ Hayas copiado correctamente Client ID y Client Secret
4. ✅ El archivo `.env` exista y tenga el formato correcto
5. ✅ Python 3.8+ esté instalado
6. ✅ Todas las dependencias estén instaladas (`pip install -r requirements.txt`)

