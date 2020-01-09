import sys
import time
import random
import datetime
import telepot
import requests
import json

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	user = msg['from']['first_name'] + ' ' + msg['from']['last_name']
	print(' from id ', chat_id)
	print('got msg from ',chat_id)
	print ('got the msg', command)
	r = requests.put('http://172.16.16.56:18180/chat', data = {'chatId', chat_id})
	if chat_id !=  r:
		bot.sendMessage(chat_id,'Te quieres quieres registrar '+user+ '?')
bot = telepot.Bot('946350488:AAFCySrUxncEdgPMxgwIVZy4_ho7SSGJgxE')
bot.message_loop(handle)
print ('Wait for it!')

while 1:
	time.sleep(10)

