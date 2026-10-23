import requests, random, os
from urllib.parse import quote

TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID") or "@promolarachadinhos"
LINK = "https://meli.la/2aXmCyr"

temas = ["organizador cozinha", "air fryer", "escova secadora"]

tema = random.choice(temas)
url = f"https://api.mercadolibre.com/sites/MLB/search?q={quote(tema)}&limit=10"

try:
    r = requests.get(url, timeout=15)
    dados = r.json()
    lista = dados.get("results", [])
    
    if not lista:
        raise ValueError("sem resultados")
    
    prod = random.choice(lista)
    titulo = prod.get("title", tema)
    preco = prod.get("price", 49.90)
    texto = f"🔥 ACHADINHO DA LARA\n\n{titulo}\n\n💰 R$ {preco}\n\n👉 {LINK}"
    
except:
    # se a API falhar, posta mesmo assim sem quebrar
    texto = f"🔥 ACHADINHO DA LARA\n\n{tema} em oferta que amamos!\n\n👉 {LINK}"

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data={"chat_id": CHAT_ID, "text": texto})
print("OK postado")
