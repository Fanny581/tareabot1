import os
import telebot

bot = telebot.TeleBot('') #anadimos el token

@bot.message_handler(commands=['hola', 'hi']) #definimos el comando
def saludo(mensaje):
    bot.reply_to(mensaje, "Hola, soy fanny")
    print("Mandaron saludo")

@bot.message_handler(commands=['Mascota', ]) #definimos el comando
def nombre(mensaje):
    bot.reply_to(mensaje, "Mi Mascota es Santiago")
    print("Mandaron mascota")

@bot.message_handler(commands=['edad', 'age'])
def edad(mensaje):
    bot.reply_to(mensaje, "Tengo 23 años")
    print("Mandaron edad")

@bot.message_handler(commands=['direccion', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "La Lima Cortes")
    print("Mandaron Direccion")

@bot.message_handler(commands=['horario', 'address'])
def direccion(mensaje):
    bot.reply_to(mensaje, "Lunes a Viernes 08:00am a 04:00 pm")
    print("Mandaron Direccion")

bot.polling()