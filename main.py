from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

import os
from keep_alive import keep_alive
keep_alive()

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hi! I am your bot. How can I help you today?')

async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('You can use /start to start the bot and /help to get this message.')

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    TOKEN = '7026799725:AAG_AQim8Glypyxo2Uz1Otz7fl-UoghLkKU'

    # Create the Application and pass it your bot's token
    application = Application.builder().token(TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Register message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
