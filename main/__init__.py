from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID, "13675555", cast=int)
API_HASH = config("API_HASH", "c0da9c346d2c45dbc7ec49a05da9b2b6")
BOT_TOKEN = config("BOT_TOKEN", "5412174097:AAEWgz85kkVTV2CR7uqEox66baoAyv7j0fo")
BOT_UN = config("BOT_UN", None)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
