from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os
import logging



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)
load_dotenv("config.env")




def getConfig(name):
    return os.environ[name]


BOT_TOKEN = getConfig("BOT_TOKEN")
OWNER_ID = getConfig("OWNER_ID")
SERVER_PATH = getConfig("SERVER_PATH")

if not SERVER_PATH:
    SERVER_PATH = f"{os.getcwd()}/server"
    
def is_owner(update: Update):
    return int(OWNER_ID) == int(update.effective_chat.id)

from bot.server_helper import ServerProcess
Server_Control = ServerProcess()
    
    
app = ApplicationBuilder().token(BOT_TOKEN).build()