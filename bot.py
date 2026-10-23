import os
import requests
import random
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
SEU_CODIGO = "malusilveira" # troca pelo seu

bot = Bot(token=BOT_TOKEN)

# PRODUTOS FIXOS DO MERCADO LIVRE - SE A API FALHAR USA ESSES
fallback = [
    {
        "title": "Kit 3 Cestos Organizadores Dobráveis Multiuso",
        "price": 39.90,
        "original_price": 89.90,
        "foto": "https://http2.mlstatic.com/D_NQ_NP_2X_771945-MLB79911111_092024-F.webp",
        "link": "https://www.mercadolivre.com.br/kit-3-cestos-organizadores-dobraveis"
    },
    {
        "title": "Organizador de Gavetas 6 Divisórias",
        "price": 19.90,
        "original_price": 59.90,
        "foto": "https://http2.mlstatic.com/D_NQ_NP_2X_882345-MLB1234567890_123456-F.webp",
        "link": "https://www.mercadolivre.com.br/organizador-de-gavetas-6-divisorias"
    }
]

produto = None
try:
    termo = random.choice(["organizador", "cesto organizador", "organizador cozinha"])
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={termo}&limit=5"
    r = requests.get(url, timeout=10).json()
    lista = r.get("results", [])
    if lista:
        p = lista[0]
        produto = {
            "title": p["title"],
            "price": p["price"],
            "original_price": p.get("original_price", p["price"]*1.8),
            "foto": p["thumbnail"].replace("-I.jpg", "-O.jpg"),
            "link": p["permalink"]
        }
except:
    pass

# Se falhar, usa o fixo
if not produto:
    produto = random.choice(fallback)

desconto = int((1 - produto["price"]/produto["original_price"])*100)
link_afiliado = f"{produto['link']}?matt_tool={SEU_CODIGO}"

mensagem = f"""🏠 ACHADINHOS DO LAR 🏠

✨ {produto['title']}

💰 De R$ {produto['original_price']:.2f} por R$ {produto['price']:.2f}
🔥 {desconto}% OFF + Frete FULL Grátis!

👉 {link_afiliado}

✅ Selo FULL - Entrega amanhã ⭐
⏰ Oferta por tempo limitado!
"""

bot.send_photo(chat_id=CHANNEL_ID, photo=produto["foto"], caption=mensagem)
print("Postado com sucesso!")
