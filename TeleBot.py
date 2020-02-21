import telebot
import pyowm

bot = telebot.TeleBot("913916239:AAG1l9Ro4IBupzwBuxd14OkeR6y0CyfDZE4")
owm = pyowm.OWM('2eb918ae70add610a3a300273ae1a45a', language="es" )


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answ ="En la ciudad "+ message.text +" ahora hay "+w.get_detailed_status()+"\n"
    answ +="En la ciudad la temperatura es: "+str(temp)+"\n\n"

    if temp<10:
        answ +="Es muy frio vistete muy caliente"
    elif temp<20:
        answ +="Es frio vistete caliente"
    elif temp>20:
        answ +="Esta caliente vistete como quieras"


    bot.send_message(message.chat.id,answ)

bot.polling(none_stop= True)
input()