import telebot
import pyowm

bot = telebot.TeleBot("the api of your bot")
owm = pyowm.OWM('your weather api', language="es" )


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    answ ="Քաղաքի ջերմաստիճանը : "+str(w.get_temperature('celsius')["temp"])+"\nՔաղաքի խոնավությունը : "+str(w.get_humidity())+"%\nԱյսորվա ամենաբարձր ջերմաստիճանը : "+str(w.get_temperature('celsius')["temp_max"])+"\nԱյսորվա ամենացածր ջերմաստիճանը : "+str(w.get_temperature('celsius')["temp_min"])+"\nՔաղաքի օդային ճնշումը : "+str(w.get_pressure()["press"])+"\n"
   

    bot.send_message(message.chat.id,answ)

bot.polling(none_stop= True)
