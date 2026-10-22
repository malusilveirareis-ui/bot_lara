import requests, random, os
TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "@promolarachadinhos"
LINK = "https://meli.la/2aXmCyr"

temas = ["organizador cozinha", "kit potes hermeticos", "organizador banheiro"]
tema = random.choice(temas)
r = requests.get(f"https://api.mercadolibre.com/sites/MLB/search?q={tema}&limit=20")
prod = random.choice(r.json()['results'])

texto = f"""🔥 ACHADINHO DA LARA - {tema.upper()}!

{prod['title']}

💰 R$ {prod['price']} com entrega FULL

👉 MEU LINK: {LINK}

#achados #larachadinhos"""

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto", data={"chat_id": CHAT_ID, "photo": prod['thumbnail'], "caption": texto})
