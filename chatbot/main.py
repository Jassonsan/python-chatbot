import sys
import time
import random
import datetime
import telepot
import requests
import json

header = {'Content-type': 'application/json'}
url = 'http://172.16.16.60:18081'
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	user = msg['from']['first_name'] + ' ' + msg['from']['last_name']
	payload = '{"chatId" :'+ str(chat_id)+'}'
	r = requests.post(url+'/chat', headers = header, data=payload)
	if chat_id !=  r:
		bot.sendMessage(chat_id,'Hola '+user+'!, No encontramos datos de tu usuario en nuestra base de datos ¿Te quieres registrar en el bot?')
bot = telepot.Bot('946350488:AAFCySrUxncEdgPMxgwIVZy4_ho7SSGJgxE')
bot.message_loop(handle)
print ('Wait for it!')

while 1:
	time.sleep(10)

