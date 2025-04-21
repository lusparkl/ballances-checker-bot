import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = f"https://ballances-checker-bot-production.up.railway.app/{TOKEN}"  # <- add https://

response = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}")
print(response.text)
