# 🌐 Guía de Despliegue Gratuito

Esta guía te ayudará a poner tu aplicación en internet **completamente gratis** para que cualquier persona pueda usarla.

## 🎯 Opciones Gratuitas

### 1️⃣ Railway (Recomendado) ⭐

**Ventajas:**
- ✅ Más fácil de usar
- ✅ Despliegue automático
- ✅ Variables de entorno simples
- ✅ Logs en tiempo real

**Pasos:**
1. **Fork este repositorio** en GitHub
2. **Ve a [Railway.app](https://railway.app)**
3. **Conéctate con GitHub**
4. **Selecciona tu fork** del repositorio
5. **Configura las variables de entorno:**
   - `SPOTIFY_CLIENT_ID`: Tu Client ID de Spotify
   - `SPOTIFY_CLIENT_SECRET`: Tu Client Secret de Spotify
6. **¡Despliega!** - Railway manejará todo automáticamente
7. **Obtén tu URL pública** (ej: `https://tu-app.railway.app`)

### 2️⃣ Render

**Ventajas:**
- ✅ Más estable
- ✅ Mejor para producción
- ✅ Configuración detallada

**Pasos:**
1. **Fork este repositorio** en GitHub
2. **Ve a [Render.com](https://render.com)**
3. **Conéctate con GitHub**
4. **Crea un nuevo Web Service**
5. **Configura:**
   - **Repository**: Tu fork del repositorio
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Variables de entorno:**
     - `SPOTIFY_CLIENT_ID`: Tu Client ID
     - `SPOTIFY_CLIENT_SECRET`: Tu Client Secret
6. **¡Despliega!** - Render creará tu URL pública

### 3️⃣ Heroku (Limitado)

**Ventajas:**
- ✅ Muy conocido
- ✅ Buena documentación

**Limitaciones:**
- ❌ Plan gratuito limitado
- ❌ Aplicaciones se "duermen" después de 30 minutos de inactividad

**Pasos:**
1. **Instala Heroku CLI**
2. **Crea un archivo `Procfile`:**
   ```
   web: python app.py
   ```
3. **Despliega:**
   ```bash
   heroku create tu-app-nombre
   heroku config:set SPOTIFY_CLIENT_ID=tu_id
   heroku config:set SPOTIFY_CLIENT_SECRET=tu_secret
   git push heroku main
   ```

### 4️⃣ Vercel (Para desarrollo)

**Ventajas:**
- ✅ Muy rápido
- ✅ Integración con GitHub

**Limitaciones:**
- ❌ Mejor para aplicaciones estáticas
- ❌ Limitaciones en tiempo de ejecución

**Pasos:**
1. **Instala Vercel CLI:**
   ```bash
   npm i -g vercel
   ```
2. **Despliega:**
   ```bash
   vercel --prod
   ```

## 🔧 Configuración para Despliegue

### Variables de Entorno Necesarias

```bash
SPOTIFY_CLIENT_ID=tu_client_id_aqui
SPOTIFY_CLIENT_SECRET=tu_client_secret_aqui
```

### Archivos Necesarios

Asegúrate de que estos archivos estén en tu repositorio:
- ✅ `app.py` - Aplicación principal
- ✅ `requirements.txt` - Dependencias
- ✅ `templates/index.html` - Interfaz web
- ✅ `config.py` - Configuración
- ✅ `.env.example` - Plantilla de variables

## 🚀 Pasos Detallados para Railway

### 1. Preparar el Repositorio
```bash
# Asegúrate de que todos los archivos estén en GitHub
git add .
git commit -m "Preparado para despliegue"
git push origin main
```

### 2. Configurar Railway
1. **Ve a [Railway.app](https://railway.app)**
2. **Haz clic en "Login"**
3. **Selecciona "Login with GitHub"**
4. **Autoriza Railway** para acceder a tus repositorios
5. **Haz clic en "New Project"**
6. **Selecciona "Deploy from GitHub repo"**
7. **Elige tu fork** del repositorio
8. **Railway detectará automáticamente** que es una aplicación Python

### 3. Configurar Variables de Entorno
1. **Ve a la pestaña "Variables"**
2. **Agrega las siguientes variables:**
   - `SPOTIFY_CLIENT_ID`: Tu Client ID de Spotify
   - `SPOTIFY_CLIENT_SECRET`: Tu Client Secret de Spotify
3. **Haz clic en "Save"**

### 4. Desplegar
1. **Railway comenzará automáticamente** el despliegue
2. **Espera a que termine** (puede tardar 2-5 minutos)
3. **Obtén tu URL pública** en la pestaña "Deployments"
4. **¡Listo!** Tu app estará disponible en internet

## 🎯 Pasos Detallados para Render

### 1. Preparar el Repositorio
```bash
# Asegúrate de que todos los archivos estén en GitHub
git add .
git commit -m "Preparado para despliegue"
git push origin main
```

### 2. Configurar Render
1. **Ve a [Render.com](https://render.com)**
2. **Haz clic en "Get Started"**
3. **Selecciona "Sign up with GitHub"**
4. **Autoriza Render** para acceder a tus repositorios
5. **Haz clic en "New +"**
6. **Selecciona "Web Service"**
7. **Conecta tu repositorio**

### 3. Configurar el Servicio
1. **Nombre**: `spotify-downloader` (o el que prefieras)
2. **Build Command**: `pip install -r requirements.txt`
3. **Start Command**: `python app.py`
4. **Variables de entorno:**
   - `SPOTIFY_CLIENT_ID`: Tu Client ID
   - `SPOTIFY_CLIENT_SECRET`: Tu Client Secret

### 4. Desplegar
1. **Haz clic en "Create Web Service"**
2. **Render comenzará** el despliegue automáticamente
3. **Espera a que termine** (puede tardar 3-7 minutos)
4. **Obtén tu URL pública** en el dashboard
5. **¡Listo!** Tu app estará disponible en internet

## 🔍 Verificar el Despliegue

### 1. Probar la URL
- **Abre tu URL pública** en el navegador
- **Verifica que la página cargue** correctamente
- **Prueba con una playlist** de Spotify

### 2. Verificar Logs
- **Railway**: Ve a la pestaña "Deployments" > "View Logs"
- **Render**: Ve a la pestaña "Logs"
- **Busca errores** en los logs si algo no funciona

### 3. Solucionar Problemas Comunes

**Error: "Module not found"**
- Verifica que `requirements.txt` esté actualizado
- Asegúrate de que todas las dependencias estén listadas

**Error: "Invalid credentials"**
- Verifica que las variables de entorno estén configuradas
- Comprueba que los valores sean correctos

**Error: "Port not found"**
- Asegúrate de que la aplicación use el puerto correcto
- Railway y Render asignan puertos automáticamente

## 💡 Consejos para el Despliegue

### ✅ Mejores Prácticas
- **Usa Railway** para principiantes (más fácil)
- **Usa Render** para producción (más estable)
- **Mantén las credenciales seguras** (nunca las compartas)
- **Prueba localmente** antes de desplegar
- **Monitorea los logs** después del despliegue

### ⚠️ Limitaciones Gratuitas
- **Railway**: 500 horas/mes gratis
- **Render**: 750 horas/mes gratis
- **Heroku**: 550 horas/mes gratis
- **Vercel**: 100GB bandwidth/mes gratis

### 🎯 Para Uso Intensivo
Si planeas usar la aplicación mucho:
- **Considera un plan de pago** (muy barato)
- **Railway**: $5/mes por recursos ilimitados
- **Render**: $7/mes por recursos ilimitados

## 🎉 ¡Felicidades!

Una vez desplegado, tu aplicación estará disponible para:
- ✅ **Cualquier persona** en internet
- ✅ **24/7** sin interrupciones
- ✅ **Gratis** para uso personal
- ✅ **Fácil de compartir** con amigos

### Compartir tu Aplicación
- **Envía la URL** a tus amigos
- **Comparte en redes sociales**
- **Usa un dominio personalizado** (opcional)

---

**¡Disfruta tu aplicación en internet!** 🌐🎵
