import sys
import time
import logging
from pyrogram import Client
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class env(object):
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    # BOT_TOKEN = str(getenv('BOT_TOKEN'))
    # OWNER_ID = int(getenv('OWNER_ID'))
    # BIN_CHANNEL = int(getenv('BIN_CHANNEL'))
    FQDN = f"https://{getenv('REPL_SLUG')}.{getenv('REPL_OWNER')}.repl.co"

StartTime = time.time()

plugins = dict(
    root = "app/plugins"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format="[%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] %(message)s")

def generate_session():
    with Client("user", api_id=env.API_ID, api_hash=env.API_HASH, in_memory=True) as user:
        user.send_message("me", f"`{user.export_session_string()}`")
        print("\nSet the value as SESSION_STRING.")

if 'SESSION_STRING' not in environ:
    generate_session()
    sys.exit()

user = Client(
    "user",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    session_string=getenv("SESSION_STRING"),
    plugins=plugins
)

with user as first_dive:
    user_dict = first_dive.get_me()
