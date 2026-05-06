from bot import app, Server_Control, is_owner
from mcstatus import JavaServer
from time import sleep
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
import shutil, psutil



async def server_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if Server_Control.process is None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Server Isn't Running!\nStart Server Using /start_server Command.")
    else:
        while True:
            try:
                server = JavaServer.lookup("localhost:25565")
                status = server.status()
                if status:
                    break
            except ConnectionRefusedError:
                sleep(2)
        
        ram = psutil.virtual_memory()
        ram_used = ram.used // (1024 ** 3)
        ram_total = ram.total // (1024 ** 3)

        
        disk = shutil.disk_usage("/")
        disk_used = disk.used // (1024 ** 3)
        disk_total = disk.total // (1024 ** 3)
        
        
        
        message = ("<b>🟢 Server Status</b>\n"
            "━━━━━━━━━━━━━━━\n"
            f"👥 <b>Players:</b> {status.players.online}/{status.players.max}\n"
            f"📦 <b>Version:</b> {status.version.name}\n"
            f"📡 <b>Latency:</b> {round(status.latency)} ms\n\n"

            "<b>💻 System Usage</b>\n"
            "━━━━━━━━━━━━━━━\n"
            f"🧠 <b>RAM:</b> {ram_used}GB / {ram_total}GB\n"
            f"💾 <b>Disk:</b> {disk_used}GB / {disk_total}GB")
        
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode="HTML")
        

async def start_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
            return await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry Buddy You Don't Have Permission To Use This Command!\nUse /status To Feel Good!")

    if Server_Control.process is None :
        message = await context.bot.send_message(chat_id=update.effective_chat.id, text="Starting The Server!")
        Server_Control.start_server()
        sleep(5)
        while True:
            try:
                server = JavaServer.lookup("localhost:25565")
                status = server.status()
                if status:
                    break
            except ConnectionRefusedError:
                sleep(2)
        edit = await context.bot.edit_message_text(text = "Server Started Successfully!", chat_id= message.chat.id, message_id=message.message_id)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Server Is Already Running!\nStop Server Using /stop_server Command.")
        
async def stop_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_owner(update):
            return await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry Buddy You Don't Have Permission To Use This Command!\nUse /status To Feel Good!")

    if Server_Control.process is not None:
        message = await context.bot.send_message(chat_id=update.effective_chat.id, text="Stopping The Server!")
        Server_Control.stop_server()
        edit = await context.bot.edit_message_text(text = "Server Stopped Successfully!", chat_id= message.chat.id, message_id=message.message_id)
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Server Isn't Running!\nStart Server Using /start_server Command.")

                

 

status_handler = CommandHandler('status', server_status)
start_handler = CommandHandler('start_server', start_server) 
stop_handler = CommandHandler('stop_server', stop_server) 
app.add_handler(status_handler)
app.add_handler(start_handler)
app.add_handler(stop_handler)



