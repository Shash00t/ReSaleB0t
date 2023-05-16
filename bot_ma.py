import telebot
import json

token='6005566873:AAEArVglZsPVvm2ArTDeUYPf-vU_VZe-YI0'
bot=telebot.TeleBot(token)

with open('cena_lis.json') as f:
  cena_lis = json.load(f)
for i in range(0, len(cena_lis), len(cena_lis)):
  cena_lis=cena_lis[i:i+5]
cena_lis1=[]
for i in range(len(cena_lis)):
  cena=cena_lis[i].replace(' ','')
  cena_lis1.append(cena)

with open('cena_steam.json') as f:
  cena_steam= json.load(f)

with open('nazvania_lis.json') as f:
  nazv= json.load(f)
for i in range(0, len(nazv), len(nazv)):
  nazv=nazv[i:i+5]

@bot.message_handler(commands=['start'])
def start_message(message):
  for i in range(len(cena_lis1)):
    if float(cena_lis1[i])<float(cena_steam[i]):
      ma=str(nazv[i])+' , '+'Цена покупки:'+str(cena_lis1[i])+', '+'Цена продажи: '+str(cena_steam[i])
      bot.send_message(message.chat.id,ma)
bot.infinity_polling()
