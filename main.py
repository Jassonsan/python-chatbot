import sys
import time
import random
import datetime
import telepot

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	user = msg['from']['first_name'] + ' ' + msg['from']['last_name']
	print(' from id ', chat_id)
	print('got msg from ',chat_id)
	print ('got the msg', command)
	if chat_id == 968761100:
		bot.sendMessage(chat_id,'Checho mk siempre llega tarde a todo')
	else:
		bot.sendMessage(chat_id, 'Hello, '+user)
bot = telepot.Bot('946350488:AAFCySrUxncEdgPMxgwIVZy4_ho7SSGJgxE')
bot.message_loop(handle)
print ('Wait for it!')

while 1:
	time.sleep(10)

