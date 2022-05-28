from tools import *
import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

TOKEN = "5393212077:AAH70bQQO0LopUHvldmSlp_dmQJQ9Vd4pNA"
bot = telegram.Bot(token=TOKEN)
updater = Updater(TOKEN, use_context=True)

responseQueue = []
id = list()
playersCnt = 0
def start(update: Update, context: CallbackContext):
    if(update.message.chat_id == update.message.from_user.id):
        bot.send_message(chat_id=update.message.chat_id , text = "Start from a group, Please 😄")
    else:
        bot.send_message(chat_id=update.message.chat_id , text = "Welcome to Halal-Trex 😄\nGame Developer: @Nour_Alkaram")
        bot.send_message(chat_id=update.message.chat_id , text = "تعليمات بداية اللعب:\n☝🏼 للانضمام إلى هذه اللعبة اضغط على /register.\n✌🏼 الرجاء الانتباه إلى أن عدد اللاعبين يجب أن يكون 3 أو 4.\n👌🏼 عندما يكتمل تسجيل كل اللاعبين اضغط على  /done.\nبالتوفيق 😁")

def register(update: Update , context: CallbackContext):
    if(len(id)==4):
        bot.send_message(chat_id=update.message.chat_id, text="لقد بلغ عدد اللاعبين الحد الأعظم")    
    else:
        id.append(update.message.from_user.id)
        bot.send_message(chat_id=update.message.chat_id, text=" عدد اللاعبين المسجلين حتى الآن هو: "+str(len(id)))

def done(update: Update, context: CallbackContext):
    if(len(id)<3):
        bot.send_message(chat_id=update.message.chat_id, text="عدد اللاعبين المسجلين غير كاف!")    
    else:
        bot.send_message(chat_id=update.message.chat_id, text=".بدأت المملكة الأولى، سأقوم من الآن فصاعداً بالتواصل مع كل منكم عبر رسائل خاصة")
        playersCnt = len(id)
        sendCards(playersCnt)
    pass

def play(update: Update, context: CallbackContext):
    
    pass

def echo(update: Update, context: CallbackContext):
    responseQueue.append((update.message.text , update.message.from_user.id))
    print(responseQueue)
    pass

def sendCards(playersCnt):
    cardsDst(playersCnt)
    x=1
    for i in id:
        answer = ''
        for j in distCards[str(x)]:
            answer+=str(j[1])+' '+str(j[0])+'\n'
        kbd = ReplyKeyboardMarkup(distCards[str(x)])
        bot.send_message(chat_id=i , text = answer , reply_markup=kbd) 
        
        x=x+1  
    pass

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("register", register))
dp.add_handler(CommandHandler("done", done))
dp.add_handler(CommandHandler("play", play))
dp.add_handler(MessageHandler(Filters.regex(r""), echo))
updater.start_polling()

