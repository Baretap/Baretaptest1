from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Play Game", url="https://baretap.github.io/Baretaptest1/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Click the button below to play the game!', reply_markup=reply_markup)

if __name__ == '__main__':
    application = ApplicationBuilder().token('7916996723:AAG8dfY-Mv4sTN607_Ic6Wn2jR_3iGnU3r8').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
