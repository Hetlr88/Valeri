import logging
import sqlite3
import time
from logging import INFO, basicConfig, getLogger, handlers
from os import getenv

from dotenv import load_dotenv
from pymongo import MongoClient
from telethon import TelegramClient

basicConfig(
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
    level=INFO,
)

handler = handlers.RotatingFileHandler(
    "logs.txt", maxBytes=10 * 1024 * 1024, backupCount=10
)
handler.setLevel(INFO)
handler.setFormatter(
    logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
)
getLogger("").addHandler(handler)


StartTime = time.time()
help_dict = {}

# Load .env file
load_dotenv()

log = getLogger("- valeri ->")
# Environment variables
TOKEN = getenv("TOKEN","7397532645:AAH7R46hDIQ95j9-5kyVgySCa-A6cHQy6vE")
API_KEY = getenv("API_KEY","26187560")
API_HASH = getenv("API_HASH","b82ed5ce892177f1229f75ac2f93c874")
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://mrhex86:mrhex86@cluster0.8pxiirj.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "6169288210"))
TMDB_KEY = getenv("TMDB_KEY")  # required for !imdb
OPENAI_API_KEY = getenv("OPENAI_API_KEY")

# clients
bot = TelegramClient(
    "bot", api_id=API_KEY, api_hash=API_HASH, device_model="iPhone XS", lang_code="en"
)

if MONGO_DB != "":
    log.info("Using MongoDB database")
    db = MongoClient(MONGO_DB, connect=True)
else:
    log.info("Using SQLite database")
    db = sqlite3.connect("bot.db")
