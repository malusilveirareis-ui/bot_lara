import os
import requests
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
# AGORA COM SEU CANAL CERTO - NÃO PRECISA PEGAR ID NUMÉRICO
CHANNEL_ID = "@promolarachadinhos"

bot = Bot(token=BOT_TOKEN)

# TESTE ACHADINHOS DO LAR - MERCADO LIVRE
mensagem = """🏠 ACHADINHOS DO LAR 🏠

✨ Kit 3 Cestos Organizadores Dobráveis

💰 De R$ 89,90 por R$ 39,90
🔥 55% OFF + Frete FULL Grátis!

👉 https://mercadolivre.com/sec/SEU_LINK_AQUI

✅ Selo FULL - Entrega amanhã ⭐
⏰ Oferta por tempo limitado!
"""

foto = "https://http2.mlstatic.com/D_NQ_NP_2X_771945-MLB79911111_092024-F.webp"

bot.send_photo(chat_id=CHANNEL_ID, photo=foto, caption=mensagem)
print("Postado no @promolarachadinhos com sucesso!")
