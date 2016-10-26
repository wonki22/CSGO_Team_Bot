#!usr/bin/env python

"""
	This is a bot that helps to create and organize teams of CSGO in telegram.
	The bot make it easier to people to get ready and wait for the others while
	letting them know that you're ready and waiting.
"""

import telebot
from token import *

bot = telebot.TeleBot(TOKEN, threaded=False)
bot.skip_pending = True

ppl_ready = {}
ppl_ready_id = {}
ppl_ready_0 = ['Empty','Empty','Empty','Empty','Empty',0]
ppl_ready_id_0 = ['Empty','Empty','Empty','Empty','Empty']
ver = 1.0

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Hello, this is the CSGO Team Bot')
	global ppl_ready
	global ppl_ready_id
	ppl_ready[message.chat.id] = [x for x in ppl_ready_0]
	ppl_ready_id[message.chat.id] = [x for x in ppl_ready_id_0]

@bot.message_handler(commands=['ready'])
def ready_status(message):
	global ppl_ready
	global ppl_ready_id
	if message.from_user.id in ppl_ready_id[message.chat.id]:
		bot.reply_to(message, 'You can\'t be ready twice')
	else:
		ppl_ready[message.chat.id][5] += 1
		if ppl_ready[message.chat.id][5] == 1:
			bot.reply_to(message, 'You are ready\n' + str(ppl_ready[message.chat.id][5]) + ' person ready.')
			ppl_ready_id[message.chat.id][ppl_ready_id[message.chat.id].index('Empty')] = message.from_user.id
			if message.from_user.username is not None:
				ppl_ready[message.chat.id][ppl_ready[message.chat.id].index('Empty')] = message.from_user.username
			else:
				ppl_ready[message.chat.id][ppl_ready[message.chat.id].index('Empty')] = message.from_user.first_name
		elif ppl_ready[message.chat.id][5] == 5:
			bot.reply_to(message, 'You are ready\n' + 'The team is full')
			ppl_ready_id[message.chat.id][ppl_ready_id[message.chat.id].index('Empty')] = message.from_user.id
			if message.from_user.username is not None:
				ppl_ready[message.chat.id][ppl_ready[message.chat.id].index('Empty')] = message.from_user.username
			else:
				ppl_ready[message.chat.id][ppl_ready[message.chat.id].index('Empty')] = message.from_user.first_name		
		elif ppl_ready[message.chat.id][5] > 5:
			bot.reply_to(message, 'The team is already full\n' + 'You\'re not in')
			ppl_ready[message.chat.id][5] = 5
		else:
			bot.reply_to(message, 'You are ready\n' + str(ppl_ready[message.chat.id][5]) + ' people ready')
			ppl_ready_id[message.chat.id][ppl_ready_id[message.chat.id].index('Empty')] = message.from_user.id
			if message.from_user.username is not None:
				ppl_ready[message.chat.id][ppl_ready[message.chat.id].index('Empty')] = message.from_user.username
			else:
				ppl_ready[message.chat.id][ppl_ready[message.chat.id].index('Empty')] = message.from_user.first_name

@bot.message_handler(commands=['notready'])
def notready_status(message):
	global ppl_ready
	global ppl_ready_id
	if message.from_user.id in ppl_ready_id[message.chat.id]:
		ppl_ready[message.chat.id][5] -= 1
		ppl_ready_id[message.chat.id][ppl_ready_id[message.chat.id].index(message.from_user.id)] = 'Empty'
		if message.from_user.username is not None:
			ppl_ready[message.chat.id][ppl_ready[message.chat.id].index(message.from_user.username)] = 'Empty'
		else:
			ppl_ready[message.chat.id][ppl_ready[message.chat.id].index(message.from_user.first_name)] = 'Empty'		
		if ppl_ready[message.chat.id][5] == 1:
			bot.reply_to(message, 'You aren\'t ready anymore\n' + str(ppl_ready[message.chat.id][5]) + ' person ready.')
		elif ppl_ready[message.chat.id][5] <= 0:
			ppl_ready[message.chat.id][5] = 0
			bot.reply_to(message, 'You aren\'t ready anymore\n' + str(ppl_ready[message.chat.id][5]) + ' people ready')
		else:
			bot.reply_to(message, 'You aren\'t ready anymore\n' + str(ppl_ready[message.chat.id][5]) + ' people ready')
	else:
		if ppl_ready[message.chat.id][5] == 1:
			bot.reply_to(message, 'You weren\'t ready\n' + str(ppl_ready[message.chat.id][5]) + ' person ready')
		else:
			bot.reply_to(message, 'You weren\'t ready\n' + str(ppl_ready[message.chat.id][5]) + ' people ready')

@bot.message_handler(commands=['status'])
def team_status(message):
	global ppl_ready
	global ppl_ready_id
	if ppl_ready[message.chat.id][5]==1:
		bot.reply_to(message, str(ppl_ready[message.chat.id][5]) +' person is ready.')
	elif ppl_ready[message.chat.id][5] >= 5:
		bot.reply_to(message, 'The team is full')
		ppl_ready[message.chat.id][5] = 5
	else:
		bot.reply_to(message, str(ppl_ready[message.chat.id][5]) + ' people ready')

@bot.message_handler(commands=['reset'])
def reset_team(message):
	global ppl_ready
	global ppl_ready_id
	global ppl_ready_0
	global ppl_ready_id_0
	ppl_ready[message.chat.id] = [x for x in ppl_ready_0]
	ppl_ready_id[message.chat.id] = [x for x in ppl_ready_id_0]
	bot.reply_to(message, 'Team reset')

@bot.message_handler(commands=['ver'])
def show_ver(message):
	global ver
	bot.reply_to(message, str(ver))

@bot.message_handler(commands=['list'])
def show_list(message):
	global ppl_ready
	global ppl_ready_id
	bot.reply_to(message, ppl_ready[message.chat.id][0]+'\n'+
			ppl_ready[message.chat.id][1]+'\n'+
			ppl_ready[message.chat.id][2]+'\n'+
			ppl_ready[message.chat.id][3]+'\n'+
			ppl_ready[message.chat.id][4])
	print(ppl_ready)

@bot.message_handler(commands=['idlist'])
def show_list(message):
	global ppl_ready
	global ppl_ready_id
	print(ppl_ready_id)

bot.polling()