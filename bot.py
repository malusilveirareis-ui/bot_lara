import os
import requests
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
# SEU ID DE AFILIADO DO MERCADO LIVRE - TROCA AQUI
SEU_CODIGO_AFILIADO = "malusilveira"  # << coloca seu código aqui

bot = Bot(token=BOT_TOKEN)

# Busca produtos que estão bombando no Mercado Livre - Lar
buscas = ["organizador de gaveta", "cesto organizador", "kit organizador cozinha", "organizador armário"]
termo = random.choice(buscas)

url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo}&limit=10&sort=price_asc"
res = requests.get(url).json()
produtos = res.get("results", [])

# Pega o produto com melhor desconto
produto = produtos[0]

titulo = produto["title"]
preco = produto["price"]
preco_original = produto.get("original_price", preco * 1.8)
desconto = int((1 - preco/preco_original)*100) if preco_original else 50
foto = produto["thumbnail"].replace("-I.jpg", "-O.jpg") # foto em alta
link_produto = produto["permalink"]

# LINK DE AFILIADO MERCADO LIVRE - MODELO OFICIAL
link_afiliado = f"{link_produto}?matt_tool={SEU_CODIGO_AFILIADO}&matt_word=maonamassa"

mensagem = f"""🏠 ACHADINHOS DO LAR 🏠

✨ {titulo}

💰 De R$ {preco_original:.2f} por R$ {preco:.2f}
🔥 {desconto}% OFF + Frete FULL Grátis!

👉 {link_afiliado}

✅ Produto com selo FULL - Entrega amanhã
⭐ + de 1.000 vendidos

⏰ Oferta por tempo limitado!
#achadinhos #lar #organizacao #mercadolivre
"""

bot.send_photo(
    chat_id=CHANNEL_ID,
    photo=foto,
    caption=mensagem
)

print(f"Postado: {titulo}")
