import requests, random, os
from urllib.parse import quote
TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID") or "@promolarachadinhos"
LINK = "https://meli.la/2aXmCyr"
temas = ["organizador cozinha","air fryer","escova secadora"]
tema = random.choice(temas)
url = f"https://api.mercadolibre.com/sites/MLB/search?q={quote(tema)}&limit=10"
r = requests.get(url, timeout=15)
dados = r.json()
if 'results' not in dados or len(dados['results'])==0:
    print("Sem resultados")
    exit(0)
prod = random.choice(dados['results'])
texto = f"🔥 ACHADINHO DA LARA - {tema}\n\n{prod['title']}\n\n💰 R$ {prod['price']}\n\n👉 MEU LINK: {LINK}"
requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": texto})
print("OK")
