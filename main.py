import constants as keys
from telegram.ext import *
import responses as R

print('Bot Started')
data = 'Name'
person_name = 'None'
def book_command(update, context):
    update.message.reply_text('Please type in your Full name?')

def handle_name_message(update, context):
    global data
    global person_name
    if data =='location':
        loc = str(update.message.text).lower()
        loc = R.register_loc(person_name,loc)
        update.message.reply_text(loc)
        if loc != 'Please enter correct location':
            data = 'date'        
    elif data == "date":
        date = str(update.message.text).lower()
        date = R.register_date(person_name,date)
        update.message.reply_text(date)    
        if date != 'please choose correct date':
            data = 'time' 
    elif data == "time":
        time = str(update.message.text).lower()
        time = R.register_time(person_name,time)
        update.message.reply_text(time)              
    elif data =='Name':    
        text = str(update.message.text).lower()
        name = R.register_name(text)
        person_name = text
        update.message.reply_text(name)
        if name == 'Please enter location':
            data = 'location'


def error(update, context):
    print(f"Update{update} caused error{context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context= True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('Book',book_command))
    dp.add_handler(MessageHandler(Filters.text, handle_name_message))
    dp.add_error_handler(error)
    updater.start_polling(1)
    updater.idle()

main()

