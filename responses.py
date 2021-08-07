import datetime
import sqlite3

date = 'None'
def sample_responses(input_text):
    user_msg = str(input_text).lower()

def register_name(input_name):
    user_msg = str(input_name).lower()
    loc = 'unavailable'
    date = 'unavailable'
    time = 'unavailable'
    public = sqlite3.connect('public_details.db')
    cursor = public.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS details(name TEXT, location TEXT, date TEXT, time TEXT)')
    cursor.execute('INSERT INTO details VALUES("{}","{}","{}","{}")'.format(user_msg,loc,date,time))
    public.commit()
    public.close()
    return "Please enter location"

def register_loc(person_name,input_loc):
    user_loc = str(input_loc).lower()
    public = sqlite3.connect('public_details.db')
    cursor = public.cursor()
    # cursor.execute('CREATE TABLE IF NOT EXISTS details(name TEXT,location TEXT)')
    #cursor.execute('INSERT INTO details VALUES("{}")'.format(user_loc))
    cursor.execute('UPDATE details SET "location" = "{}" WHERE "name" = "{}"'.format(user_loc,person_name))
    public.commit()
    public.close()
    curr_date = datetime.datetime.now()
    dates = 'Please choose date\nreply with\n'
    for i in range(1,4):
        curr_date += datetime.timedelta(days=1)
        dates = dates+str(i)+' for '+str(curr_date)[0:11]+'\n'
    return dates

def register_date(person_name,input_date):
    global date
    dates = []
    curr_date = datetime.datetime.now()
    for i in range(1,4):
        curr_date += datetime.timedelta(days=1)
        dates.append(str(curr_date))
    if input_date =="1":
        input_date = dates[0][0:11]
        input_time = dates[0][11:16]
    elif input_date =="2":
        input_date = dates[1][0:11]
        input_time = dates[1][11:16]
    elif input_date =="3":
        input_date = dates[2][0:11]
        input_time = dates[2][11:16]
    
    user_date = str(input_date).lower()
    public = sqlite3.connect('public_details.db')
    cursor = public.cursor()
    cursor.execute('UPDATE details SET "date" = "{}" WHERE "name" = "{}"'.format(user_date,person_name))
    public.commit()
    public.close()
    date = input_date
    reply = "To Book time slot Please reply with\n1   for 9 to 12\n2   for 12 to 3\n3   for 3 to 6"
    return reply

def register_time(person_name,input_time):
    time = ['9 to 12','12 to 3','3 to 6']
    global date
    if input_time =="1":
        input_time = time[0]
    elif input_time =="2":
        input_time = time[1]
    elif input_time =="3":
        input_time = time[2]
    user_time = str(input_time).lower()
    public = sqlite3.connect('public_details.db')
    cursor = public.cursor()
    cursor.execute('UPDATE details SET "time" = "{}" WHERE "name" = "{}"'.format(user_time,person_name))
    public.commit()
    public.close()
    return 'Congratulations your slot is booked on '+date+' and between '+input_time+" O'"+'Clock.'
