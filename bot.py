import os
import random
import requests
import asyncio
from telegram import Bot

TOKEN = os.environ.get("BOT_TOKEN") or os.getenv("BOT_TOKEN")
CHANNEL = os.environ.get("CHANNEL_ID") or os.getenv("CHANNEL_ID")
if not TOKEN or not CHANNEL:
    raise SystemExit("Faltou BOT_TOKEN ou CHANNEL_ID")

temas = [
    "organizador cozinha",
    "air fryer",
    "escova secadora",
    "aspirador robo",
    "liquidificador",
    "kit potes hermeticos",
    "cafeteira eletrica",
    "jogo de toalhas",
    "organizador banheiro",
    "bolsa feminina transversal",
    "tapete cozinha",
    "cortina blackout"
]

frases_titulo = [
    "⚡ OFERTA IMPERDÍVEL - ACHADINHOS DO LAR ⚡",
    "🏠 ACHADINHOS DO LAR QUE VOCÊ VAI AMAR 🔥",
    "💥 ACHADINHOS DO LAR - PREÇO BAIXOU MUITO!",
    "✨ O MAIS QUERIDO DO LAR ✨",
    "🚨 PROMOÇÃO RELÂMPAGO - ACHADINHOS DO LAR 🚨",
    "💣 ACHADINHOS DO LAR - QUEIMOU O ESTOQUE!"
]

AFFILIATE_FALLBACK = "https://meli.la/2aXmCyr"

def buscar_produto(tema):
    try:
        url = "https://api.mercadolibre.com/sites/MLB/search"
        headers = {"User-Agent": "Mozilla/5.0"}
        params = {"q": tema, "limit": 15}
        r = requests.get(url, params=params, headers=headers, timeout=15)
        data = r.json()
        results = data.get("results", [])
        if not results:
            return None
        prod = random.choice(results[:8])
        thumb = prod.get("thumbnail", "").replace("-I.jpg", "-O.jpg").replace("-I.webp", "-O.webp")
        return {
            "title": prod.get("title", "Achadinho incrível"),
            "price": prod.get("price"),
            "link": prod.get("permalink", AFFILIATE_FALLBACK),
            "thumb": thumb
        }
    except Exception as e:
        print(f"Erro: {e}")
        return None

async def main():
    tema = random.choice(temas)
    frase = random.choice(frases_titulo)
    prod = buscar_produto(tema)
    bot = Bot(token=TOKEN)
    
    if prod:
        preco = f"R$ {prod['price']:.2f}".replace(".", ",") if prod['price'] else "EM OFERTA"
        legenda = (
            f"{frase}\n\n"
            f"🛍️ {prod['title']}\n\n"
            f"💰 Por apenas {preco}\n"
            f"📦 Enviamos Rápido | 🏠 Achadinhos do Lar\n\n"
            f"👉 Garanta com desconto:\n{prod['link']}\n\n"
            f"⚠️ Estoque limitado!"
        )
        try:
            if prod['thumb']:
                await bot.send_photo(chat_id=CHANNEL, photo=prod['thumb'], caption=legenda)
            else:
                await bot.send_message(chat_id=CHANNEL, text=legenda)
        except:
            await bot.send_message(chat_id=CHANNEL, text=legenda)
    else:
        texto = f"{frase}\n\n🏠 {tema} em oferta que amamos!\n\n👉 {AFFILIATE_FALLBACK}"
        await bot.send_message(chat_id=CHANNEL, text=texto)

asyncio.run(main())
