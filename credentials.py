import os
from dotenv import load_dotenv


load_dotenv()
BOT_KEY = os.getenv("BOT_KEY")
BOT_NAME = os.getenv("BOT_NAME")

print(BOT_KEY, BOT_NAME)