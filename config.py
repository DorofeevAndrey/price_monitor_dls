import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("URL")
TARGET_PRICE = int(os.getenv("TARGET_PRICE"))
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))
CHECK_INTERVAL=int(os.getenv("CHECK_INTERVAL"))