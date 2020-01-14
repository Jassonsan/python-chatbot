import sys
import time
import random
import datetime
import telepot
import requests
import json

header = {'Content-type': 'application/json'}
url = 'http://172.16.16.60:18081'
verify_chats = []
def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	user = msg['from']['first_name'] + ' ' + msg['from']['last_name']
	payload = '{"chatId" :'+ str(chat_id)+'}'
	r = requests.get(url+'/chat/'+str(chat_id), headers = header)
	print(r.status_code)
	if r.status_code == 404:
		bot.sendMessage(chat_id,'Hola '+user+'!, No encontramos datos de tu usuario en nuestra base de datos ¿Te quieres registrar en el bot?')
	elif r.status_code == 200:
		bot.sendMessage(chat_id, 'Hola '+user+'!, te encontramos en nuestra base de datos, cuentanos que quieres hacer:')
	elif r.status_code == 505:
		bot.sendMessage(chat_id, 'Hola '+user+'!, tenemos un problema con nuestro servidor en este momento, por favor, verifica nuevamente más tarde.')
bot = telepot.Bot('946350488:AAFCySrUxncEdgPMxgwIVZy4_ho7SSGJgxE')
bot.message_loop(handle)
print ('Wait for it!')

while 1:
	time.sleep(10)




