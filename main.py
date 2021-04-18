

import telebot
import time
import datetime
from multiprocessing import *
import schedule
API_TOKEN = 'TOKEN'
bot = telebot.TeleBot(API_TOKEN)
 
 
def start_process():#Запуск Process
    p1 = Process(target=P_schedule.start_schedule, args=()).start()
 
    
class P_schedule(): # Class для работы с schedule
    def start_schedule(): #Запуск schedule
        ######Параметры для schedule######
        schedule.every(1).seconds.do(P_schedule.send_message1)
        schedule.every(1).seconds.do(P_schedule.send_message2)
        
        ##################################
        
        while True: #Запуск цикла
            schedule.run_pending()
            time.sleep(1)
 
  
    def send_message1():
        bot.send_message(916590759, 'Где сотка')
    def send_message2():
        bot.send_message(903532924, 'Сыслам , я хочу тебя')
    
    

 
###Настройки команд telebot#########
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Нажали start')            
#####################
 
    
if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass