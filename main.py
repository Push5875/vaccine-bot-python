import constants as keys
from telegram.ext import *
import responses as R

print('Bot Started')
data = 'None'
person_name = 'None'
def instruction(update, context):
    global data
    update.message.reply_text('Welcome to vaccine booking bot...')
    update.message.reply_text('Please type in your Full name?')
    if data=='None':
        data = 'Name'

def wrong(update, context):
    global data
    update.message.reply_text('Please reply with /book to proceed...')


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
        if data == 'time':
            data = 'None'                   
    elif data =='Name':    
        text = str(update.message.text).lower()
        name = R.register_name(text)
        person_name = text
        update.message.reply_text(name)
        if name == 'Please enter location':
            data = 'location'
    else:
        update.message.reply_text('Please type in your Full name?')
        if data=='None':
            data = 'Name'

def error(update, context):
    print(f"Update{update} caused error{context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context= True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',wrong))
    start_value = CommandHandler('Book',instruction)
    dp.add_handler(start_value)
    dp.add_handler(MessageHandler(Filters.text, handle_name_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

main()

