import logging
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def start_bot(update: Updater, context: CallbackContext):
    mytext = f'''Hello {update.message.chat.first_name}
    
    i have only /start command! =)'''
    update.message.reply_text(mytext)

def chat(update: Updater, context: CallbackContext):
    text = update.message.text
    logging.info(text)

    update.message.reply_text(text)

def main():
    updtr = Updater('6321694321:AAFErzmd5crdo9VeHTUFp7lNaI-4xwDu6wo')

    updtr.dispatcher.add_handler(CommandHandler('start', start_bot))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

    updtr.start_polling()
    updtr.idle()

if __name__ == '__main__':
    logging.info('Bot started!')
    main()