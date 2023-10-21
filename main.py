import json
import telebot
import requests
from telebot import types
from bs4 import BeautifulSoup as BS


headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}

bot = telebot.TeleBot('6336988795:AAHZQTEWoQoCmc7fbRlenANClIwzQVlqeTI')

blago1 = './img/deti_nashi.png'
blago2 = './img/marxamat.png'
blago3 = './img/gumanitarnoe_deystvie.png'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Фонды")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Здравствуй, {0.first_name}!\nКонтакт моего разработчика:\nhttps://t.me/Pussyeater_228".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    
    if(message.text == "Фонды"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "1 - Дети наши", reply_markup = markup)
        bot.send_message(message.chat.id, "2 - Мархамат", reply_markup = markup)
        bot.send_message(message.chat.id, "3 - Гуманитарное действие", reply_markup = markup)
    
    elif(message.text == "1"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Помочь', url='https://nuzhnapomosh.ru/funds/deti_nashi_1067799022060/')
        btn1 = types.KeyboardButton("Вернуться в меню")

        markup.add(btn_my_site)
        bot.send_photo(message.chat.id, open(blago1, 'rb'), reply_markup = markup)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn1)
        bot.send_message(message.chat.id, "Дети наши - Профилактика социального сиротства, содействие интеграции в общество детей-сирот", reply_markup = markup)
        bot.send_message(message.chat.id, 
                         'Фонд работает с 2005 г.Миссия фонда «Дети наши» — '
                          'профилактика социального сиротства и содействие успешной интеграции в общество детей, '
                          'оставшихся без попечения родителей Цели: — предотвращение попадания и возвратов детей в '
                          'интернатные учреждения; — создание эффективной системы устройства детей в семьи; — оказание '
                          'комплексной поддержки детей, оставшихся без попечения родителей, для успешной интеграции в общество; — '
                          'привлечение общественного внимания к проблемам социального сиротства.', reply_markup = markup)
        
    elif(message.text == "2"):
        
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Помочь', url='https://nuzhnapomosh.ru/funds/marxamat_1100200003584/')
        btn1 = types.KeyboardButton("Вернуться в меню")
        
        markup.add(btn_my_site)
        bot.send_photo(message.chat.id, open(blago2, 'rb'), reply_markup = markup)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn1)
        bot.send_message(message.chat.id, "Мархамат - Помощь детям-инвалидам и детям с ОВЗ", reply_markup = markup)
        bot.send_message(message.chat.id, 
                         'Благотворительный фонд «Мархамат» был создан в сентябре 2010 г. '
                          'для содействия развития благотворительности, оказания комплексной помощи и решения '
                          'проблем полноценного развития детей, включая детей-сирот и детей с ограниченными возможностями '
                           'здоровья на территории Республики Башкортостан. Направления деятельности фонда: — Создание благоприятных '
                            'условий для выявления, развития и поддержки одаренных детей — Комплексное решение проблем детей-сирот и '
                            'детей из семей, находящихся в трудной жизненной ситуации — Комплексное решение проблем профилактики, '
                            'лечения и реабилитации детей.', reply_markup = markup)
            
    elif(message.text == "3"):
        markup = types.InlineKeyboardMarkup()
        btn_my_site = types.InlineKeyboardButton(text='Помочь', url='https://nuzhnapomosh.ru/funds/gumanitarnoe_deystvie_1037858012697/')
        btn1 = types.KeyboardButton("Вернуться в меню")

        markup.add(btn_my_site)
        bot.send_photo(message.chat.id, open(blago3, 'rb'), reply_markup = markup)
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn1)
        bot.send_message(message.chat.id, "Гуманитарное действие - Снижение вреда от наркотиков, профилактика ВИЧ и гепатитов, предотвращение передозировок", reply_markup = markup)
        bot.send_message(message.chat.id, "Благотворительный фонд «Гуманитарное действие» с 2001 года занимается профилактикой ВИЧ-инфекции, вирусных гепатитов и туберкулеза. «Гуманитарное действие» помогает своим клиентам пройти реабилитацию, начать или возобновить прием лекарств от ВИЧ-инфекции, гепатитов или туберкулеза, не погибнуть от передозировки. Программы: — профилактика ВИЧ-инфекции, гепатитов и туберкулеза среди людей, употребляющих наркотики; — мобильная медико-социальная помощь для тяжелобольных людей, живущих с ВИЧ; — ресурсно-методический центр.", reply_markup = markup)
              
    elif (message.text == "Вернуться в меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        markup.add(btn1, btn2, btn3)

        bot.send_message(message.chat.id, "1 - Дети наши", reply_markup = markup)
        bot.send_message(message.chat.id, "2 - Мархамат", reply_markup = markup)
        bot.send_message(message.chat.id, "3 - Гуманитарное действие", reply_markup = markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)