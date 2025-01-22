import discord
import requests
import asyncio
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

# Cargar variables desde el archivo .env
load_dotenv()

# Token del bot de Discord
TOKEN = os.getenv("BOT_TOKEN")

# ID del canal de Discord al que quieres enviar los mensajes
CANAL_ID = int(os.getenv("CHANNEL_ID"))

# URL para verificar la disponibilidad del servidor RISE-S en OVH
URL_OVH = "https://www.ovhcloud.com/es/bare-metal/prices/?localization=Fr|de|pl|uk"

class MiCliente(discord.Client):
    async def on_ready(self):
        print(f'{self.user} ha iniciado sesión.')
        
        # Intentar obtener el canal
        canal = self.get_channel(CANAL_ID)
        if canal is None:
            print(f"Error: No se pudo encontrar el canal con ID {CANAL_ID}. Verifica el ID y los permisos.")
            return
        
        print(f"Canal encontrado: {canal.name}")
        
        # Bucle para verificar la disponibilidad cada 5 minutos
        while True:
            disponibilidad = self.chequear_disponibilidad()
            if disponibilidad:
                await canal.send("🎉 **El servidor RISE-S está disponible para comprar en OVH!**")
            else:
                print("Servidor no disponible.")
            
            # Esperar 5 minutos antes de verificar nuevamente
            await asyncio.sleep(300)

    def chequear_disponibilidad(self):
        try:
            # Hacer la solicitud a la página de precios
            respuesta = requests.get(URL_OVH)
            soup = BeautifulSoup(respuesta.text, 'html.parser')

            # Buscar el div que contiene el servidor RISE-S
            bloque_rise_s = soup.find("div", {"data-product-id": "RISE-S-|-AMD-RYZEN-7-9700x"})
            if not bloque_rise_s:
                print("No se encontró el bloque del servidor RISE-S.")
                return False

            # Buscar el bloque con clase "ods-card--all-server__unavailable" dentro del servidor
            bloque_no_disponible = bloque_rise_s.find("div", class_="ods-card--all-server__unavailable")
            if bloque_no_disponible:
                print("Servidor RISE-S no disponible (bloque de no disponibilidad encontrado).")
                return False

            # Si el bloque "ods-card--all-server__unavailable" no está presente, está disponible
            print("Servidor RISE-S disponible (bloque de no disponibilidad no encontrado).")
            return True

        except Exception as e:
            print(f"Error al chequear la disponibilidad: {e}")
        return False

# Configurar intents para asegurar que el bot tiene acceso a los datos necesarios
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Inicializar el cliente de Discord con los intents configurados
client = MiCliente(intents=intents)
client.run(TOKEN)
