import telebot
import replics
import requests

token = "6819720754:AAEArmC7be4NY3Zwa6onRHLtvA6e_t4h1BQ"
bot = telebot.TeleBot(token=token)

proxies = {'https': 'socks5://198.50.217.202:1080'}

city = 'Самара'
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, '''Привет! Я - бот-визитка. Ты можешь давать мне команды. Например,
    /help - подскажу, как я работаю.
Но можно просто переписываться со мной, как с человеком.''')

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, replics.h)

@bot.message_handler(commands=['about'])
def handle_about(message):
    bot.send_message(message.chat.id, replics.cart)
    bot.send_message(message.chat.id, 'Можешь подробнее узнать про какую-то черту персонажа через соответствующие команды.')
@bot.message_handler(commands=['about_personality'])
def health(message):
    bot.send_message(message.chat.id, replics.cartoon['Характер'])
@bot.message_handler(commands=['about_biography'])
def speed(message):
    bot.send_message(message.chat.id, replics.cartoon['Биография'])
@bot.message_handler(commands=['about_power'])
def power(message):
    bot.send_message(message.chat.id, replics.cartoon['Сила'])
@bot.message_handler(commands=['about_age'])
def age(message):
    bot.send_message(message.chat.id, replics.cartoon['Возраст'])
@bot.message_handler(commands=['questionnaire'])
def handle_about(message):
    bot.send_message(message.chat.id, 'Упс, эта команда пока не работает.')
@bot.message_handler(commands=['weather'])
def weather(message):
    weather_data = requests.get(url).json()
    temperature = str(round(weather_data['main']['temp']))
    temperature_feels = str(round(weather_data['main']['feels_like']))
    bot.send_message(message.chat.id, text='Сейчас в городе '+city+' '+temperature+'°C')
    bot.send_message(message.chat.id, text='Ощущается как '+temperature_feels+'°C')
    wind_speed = round(weather_data['wind']['speed'])
    if wind_speed < 5:
        bot.send_message(message.from_user.id, '✅ Погода хорошая, ветра почти нет')
    elif wind_speed < 10:
        bot.send_message(message.from_user.id, '🤔 На улице ветрено, оденьтесь чуть теплее')
    elif wind_speed < 20:
        bot.send_message(message.from_user.id, '❗️ Ветер очень сильный, будьте осторожны, выходя из дома')
    else:
        bot.send_message(message.from_user.id, '❌ На улице шторм, на улицу лучше не выходить')
    bot.send_message(message.from_user.id, 'Скорость ветра равна '+str(wind_speed))

def if_hello(messege):
    return 'прив' in messege.text.lower()
@bot.message_handler(content_types=['text'], func=if_hello)
def hello(messege):
    bot.send_message(messege.from_user.id, replics._hi_(replics.hi))

def if_by(messege):
    if 'пока' in messege.text.lower() or 'до свидания' in messege.text.lower() or 'до встречи' in messege.text.lower():
        answer = True
    else:
        answer = False
    return answer
@bot.message_handler(content_types=['text'], func=if_by)
def by(messege):
    bot.send_message(messege.from_user.id, replics._by_(replics.by))

def know(messege):
    if 'как' in messege.text.lower() and 'дела' in messege.text.lower():
        answer = True
    else:
        answer = False
    return answer
@bot.message_handler(content_types=['text'], func=know)
def _know_(messege):
    bot.send_message(messege.from_user.id, replics._know_(replics.know))

def if_good(messege):
    if ('норм' in messege.text.lower()) or 'хорошо' in messege.text.lower():
        answer = True
    else:
        answer = False
    return answer
@bot.message_handler(content_types=['text'], func=if_good)
def good(messege):
    bot.send_message(messege.from_user.id, replics._good_(replics.good))

def if_bad(messege):
    if 'плох' in messege.text.lower() or 'ужас' in messege.text.lower():
        answer = True
    else:
        answer = False
    return answer
@bot.message_handler(content_types=['text'], func=if_bad)
def bad(messege):
    bot.send_message(messege.from_user.id, replics._bad_(replics.bad))

def thank(messege):
    if 'спс' in messege.text.lower() or 'спасиб' in messege.text.lower():
        answer = True
    else:
        answer = False
    return answer
@bot.message_handler(content_types=['text'], func=thank)
def thanks(messege):
    bot.send_message(messege.from_user.id, replics._thanks_(replics.thanks))

def if_help(messege):
    return 'помоги' in messege.text.lower()
@bot.message_handler(content_types=['text'], func=if_help)
def help(messege):
    bot.send_message(messege.from_user.id, 'Может тебе обратится за помощью к кому-то по-опытнее или поискать в интернете? Я ещё очень мало знаю')

@bot.message_handler(content_types=['photo'])
def get_photo(messege):
    bot.send_photo(messege.from_user.id, open(replics._photo_(replics.photo), 'rb'), caption = replics._coment_(replics.coments))

@bot.message_handler(content_types=['text', 'voice', 'video', 'animation', 'document'])
def i_dont_know(messege):
    bot.send_message(messege.from_user.id, 'Понял, принял, обработал, промолчал.')

bot.polling()