# Bot de Discord para Notificaciones de Disponibilidad en OVH

Este bot de Discord está diseñado para monitorear la disponibilidad de servidores específicos en OVH y enviar notificaciones en un canal de Discord cuando estén disponibles. Actualmente, el bot está configurado para rastrear la disponibilidad del servidor **RISE-S**.

---

## Características

- **Monitoreo automático:** Verifica la disponibilidad del servidor en intervalos regulares.
- **Notificaciones en Discord:** Envía un mensaje en un canal específico cuando el servidor está disponible.
- **Configuración segura:** Las claves sensibles como el token del bot y el ID del canal se manejan mediante un archivo `.env`.

---

## Requisitos

- Python 3.10 o superior
- Una cuenta de Discord con permisos para crear un bot
- Un canal en Discord donde el bot enviará las notificaciones

---

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Mirt-one/bot-ovh-availability-discord.git
cd bot-ovh-availability-discord
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Crea y activa un entorno virtual:

```bash
# En Linux/macOS
python3 -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

Instala las bibliotecas necesarias:

```bash
pip install -r requirements.txt
```

### 4. Configurar el archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
BOT_TOKEN=TU_TOKEN_DEL_BOT
CHANNEL_ID=TU_ID_DEL_CANAL
```

- **BOT_TOKEN**: El token de tu bot de Discord.
- **CHANNEL_ID**: El ID del canal de Discord donde quieres recibir las notificaciones.

---

## Uso

Ejecuta el bot con:

```bash
python bot.py
```

El bot se conectará a Discord y comenzará a monitorear la disponibilidad del servidor **RISE-S** en OVH. Si el servidor está disponible, enviará un mensaje al canal configurado.

---

## Personalización

### Monitorear otros servidores

1. Abre `bot.py`.
2. Busca la línea donde se define el ID del servidor RISE-S:
   ```python
   bloque_rise_s = soup.find("div", {"data-product-id": "RISE-S-|-AMD-RYZEN-7-9700x"})
   ```
3. Sustituye `RISE-S-|-AMD-RYZEN-7-9700x` con el ID del servidor que quieres monitorear (este ID se puede encontrar inspeccionando el HTML de la página de OVH).

### Ajustar el intervalo de monitoreo

Por defecto, el bot verifica la disponibilidad cada 5 minutos. Para cambiarlo:

1. Busca la línea en el bucle principal:
   ```python
   await asyncio.sleep(300)
   ```
2. Cambia `300` (en segundos) al valor deseado.

---

## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o encuentras un problema, por favor abre un issue o crea un pull request en el repositorio.

---

## Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

---

## Autor

Creado por [Mirt-one](https://github.com/Mirt-one).
