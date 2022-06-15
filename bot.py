import telegram.ext
import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

PORT = int(os.environ.get('PORT','8443'))



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


TOKEN = '5182094053:AAGCIhTSpMCh3vhLiUy7pPVZQyRY0PpZayI'
APP_NAME = 'https://scientificsociety-bot.herokuapp.com/'
listOfChatsText = dict()
listOfChatsIDs = dict()
listOfSuggestions = dict()
messageIdChatId = dict()

bot = telegram.Bot(TOKEN)



def start(update, context):
    global listOfChatsIDs,listOfChatsText,bot
    listOfChatsIDs[update.message.chat_id] = 0
    id = update.message.chat_id
    listOfChatsIDs[id] = ""
    listOfChatsText[id] = ""
    bot_welcome = """
.با سلام به ربات انجمن علمی مهندسی مواد و متالورژی دانشگاه صنعتی امیرکبیر خوش آمدید
.با تشکر از شما برای زمانی که برای پیشنهادات و انتقادات می‌گذارید
.همچنین از این طریق می‌توانید اگر سوالی دارید نیز بپرسی
.با تشکر

    """
    keyboard = [
        [
            InlineKeyboardButton("پرسش و پاسخ", callback_data='question'),
            InlineKeyboardButton("انتقادات و پیشنهادات", callback_data='suggestion'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(bot_welcome, reply_markup=reply_markup)
    pass

def button(update,context):
    global  listOfChatsIDs
    id = update.callback_query.from_user.id
    query = update.callback_query
    query.answer()
    if query.data == 'question':
        listOfChatsIDs[id] = 'Q_0'
        query.message.reply_text(text="""
.لطفا سوال خود را بفرمایید. در اسرع وقت توسط اعضای انجمن علمی به آن پاسخ داده می‌شود
.لازم به ذکر است که تمامی ارتباطات به صورت ناشناس خواهد بود
.باتشکر """)
    elif query.data == 'suggestion':
        listOfChatsIDs[id] = 'S_0'
        query.message.reply_text(text=""" 
.لطفا انتقاد یا پیشنهاد خود را پیام بعدی با ما در ارتباط بگذارید 
.لازم به ذکر است تمامی ارتباطات به صورت ناشناس خواهد بود
.با تشکر""")
    

def help(update, context):
    update.message.reply_text("""
    به منظور ثبت نظرات ابتدا کامند
    /start
    .را بزنید و سپس با توجه به راهنمای مورد نظر پیام خود را ارسال کنید. با تشکر از همکاری شما 
    """)

def handle_contact(update,context):
    global listOfChatsText,listOfChatsIDs,bot,listOfSuggestions,messageIdChatId

    id = update.message.chat_id
    
    if id != -1001610569280 and listOfChatsIDs[id] == 'Q_0' :
        listOfChatsText[id] = (update.message.text).replace("\n"," ")
        message = bot.sendMessage(chat_id = -1001610569280,text ="پرسش \n" + listOfChatsText[id] + "\n id = " + str(id))
        update.message.reply_text("با تشکر پرسش شما با موفقیت دریافت شد. پاسخ آن در اسرع وقت خدمتتان ارسال می‌شود.")
        listOfSuggestions[message.message_id] = message
        messageIdChatId[id] = message.message_id

    if id != -1001610569280 and listOfChatsIDs[id] == 'S_0':
        listOfChatsText[id] = (update.message.text).replace("\n"," ")
        message = bot.sendMessage(chat_id = -1001610569280,text ="انتقادات \n" + listOfChatsText[id]+ "\n id = " + str(id))
        listOfSuggestions[message.message_id] = message
        messageIdChatId[id] = message.message_id
        update.message.reply_text(".با تشکر از ثبت نظر شما در صورت وجود ابهام از طریق همین ربات با شما ارتباط گرفته خواهد شد ")
        listOfChatsText[id] = ""
        listOfChatsIDs[id] = 0

    if id == -1001610569280:
        msg = update.message.reply_to_message
        idForReplying = find_ID(msg.message_id)
        bot.sendMessage(chat_id = idForReplying, text = update.message.text)
        listOfChatsText[idForReplying] = ""
        listOfChatsIDs[idForReplying] = 0

    pass

def find_ID(msg_id):
    global messageIdChatId
    for key in messageIdChatId:
        if messageIdChatId[key] == msg_id:
            return key


def error(update,context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    global TOKEN,APP_NAME,PORT
    
    
    updater = telegram.ext.Updater(TOKEN, use_context=True)

    disp = updater.dispatcher

    disp.add_handler(telegram.ext.CommandHandler("start",start))
    disp.add_handler(telegram.ext.CommandHandler("help",help))
    disp.add_handler(telegram.ext.CallbackQueryHandler(button))
    disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_contact))
    disp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",port = PORT,url_path=TOKEN,webhook_url=APP_NAME + TOKEN)
    #updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
    
