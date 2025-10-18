# 🚀 Despliegue en Railway - Guía Completa

Esta guía te ayudará a desplegar tu aplicación en Railway paso a paso.

## 🔧 Archivos de Configuración Creados

### ✅ `railway.json`
Configuración específica para Railway:
- Builder: NIXPACKS
- Comando de inicio: `python app.py`
- Healthcheck en la ruta raíz
- Política de reinicio automático

### ✅ `nixpacks.toml`
Configuración del proceso de build:
- Instala Python 3 y FFmpeg
- Instala dependencias de requirements.txt
- No instala spotdl ni npm

### ✅ `runtime.txt`
Especifica Python 3.11.0

### ✅ `app.py` (Actualizado)
- Detecta variables de entorno de Railway
- Usa PORT y HOST de Railway automáticamente
- Configuración optimizada para producción

## 🚀 Pasos para Desplegar

### 1️⃣ **Crear Repositorio en GitHub**
1. Ve a [github.com](https://github.com)
2. Crea nuevo repositorio: `spotify-playlist-downloader`
3. **Marca como Public**
4. **NO agregues README, .gitignore o licencia**

### 2️⃣ **Subir Código a GitHub**
```bash
# Conectar repositorio local con GitHub
git remote add origin https://github.com/TU_USUARIO/spotify-playlist-downloader.git

# Subir código
git push -u origin main
```

### 3️⃣ **Desplegar en Railway**
1. **Ve a [Railway.app](https://railway.app)**
2. **Haz clic en "Login"**
3. **Selecciona "Login with GitHub"**
4. **Autoriza Railway** para acceder a tus repositorios
5. **Haz clic en "New Project"**
6. **Selecciona "Deploy from GitHub repo"**
7. **Elige tu repositorio** `spotify-playlist-downloader`
8. **Railway detectará automáticamente** la configuración

### 4️⃣ **Configurar Variables de Entorno**
1. **Ve a la pestaña "Variables"**
2. **Agrega estas variables:**
   ```
   SPOTIFY_CLIENT_ID=tu_client_id_aqui
   SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui
   ```
3. **Haz clic en "Save"**

### 5️⃣ **¡Desplegar!**
1. **Railway comenzará automáticamente** el despliegue
2. **Espera 2-5 minutos** a que termine
3. **Obtén tu URL pública** en la pestaña "Deployments"
4. **¡Listo!** Tu app estará disponible en internet

## 🔍 Verificar el Despliegue

### 1. **Probar la URL**
- Abre tu URL pública en el navegador
- Verifica que la página cargue correctamente
- Prueba con una playlist de Spotify

### 2. **Verificar Logs**
- Ve a la pestaña "Deployments" > "View Logs"
- Busca errores en los logs si algo no funciona

### 3. **Solucionar Problemas Comunes**

**Error: "Module not found"**
- Verifica que `requirements.txt` esté actualizado
- Asegúrate de que todas las dependencias estén listadas

**Error: "Invalid credentials"**
- Verifica que las variables de entorno estén configuradas
- Comprueba que los valores sean correctos

**Error: "Port not found"**
- Railway asigna puertos automáticamente
- La aplicación detecta el puerto automáticamente

## 📊 Configuración Optimizada

### **Variables de Entorno Necesarias:**
```bash
SPOTIFY_CLIENT_ID=tu_client_id_aqui
SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui
```

### **Variables Opcionales:**
```bash
DEBUG=False
HOST=0.0.0.0
PORT=5000
SECRET_KEY=tu_secret_key_aqui
```

## 🎯 Características del Despliegue

### ✅ **Configuración Automática**
- Railway detecta automáticamente que es una aplicación Python
- Instala FFmpeg automáticamente
- Configura el puerto automáticamente

### ✅ **Optimizaciones**
- No instala dependencias innecesarias (spotdl, npm)
- Configuración de producción por defecto
- Healthcheck automático

### ✅ **Monitoreo**
- Logs en tiempo real
- Reinicio automático en caso de fallo
- Métricas de uso

## 💡 Consejos para el Despliegue

### **Antes del Despliegue:**
1. **Prueba localmente** que todo funcione
2. **Verifica las credenciales** de Spotify
3. **Asegúrate de que el repositorio** esté actualizado

### **Después del Despliegue:**
1. **Prueba la URL** inmediatamente
2. **Verifica los logs** si hay problemas
3. **Comparte la URL** con tus amigos

### **Para Uso Intensivo:**
- **Railway**: 500 horas/mes gratis
- **Para más uso**: Considera un plan de pago ($5/mes)

## 🎉 ¡Felicidades!

Una vez desplegado, tu aplicación estará disponible para:
- ✅ **Cualquier persona** en internet
- ✅ **24/7** sin interrupciones
- ✅ **Gratis** para uso personal
- ✅ **Fácil de compartir** con amigos

### **Compartir tu Aplicación:**
- **Envía la URL** a tus amigos
- **Comparte en redes sociales**
- **Usa un dominio personalizado** (opcional)

---

**¡Disfruta tu aplicación en internet!** 🌐🎵
