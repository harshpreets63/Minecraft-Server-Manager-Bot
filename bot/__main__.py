from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from bot import app
from bot.commands import server_control
from telegram import BotCommand

async def set_commands(app):
    await app.bot.set_my_commands([
        BotCommand("start", "Start the bot"),
        BotCommand("start_server", "Start Minecraft server"),
        BotCommand("stop_server", "Stop Minecraft server"),
        BotCommand("status", "Show server status"),
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a Minecraft Server Management bot, Created By @perunoob")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Pong Pong")


start_handler = CommandHandler('start', start)
start_handler = CommandHandler('ping', ping)
app.add_handler(start_handler)
app.post_init = set_commands
app.run_polling()

