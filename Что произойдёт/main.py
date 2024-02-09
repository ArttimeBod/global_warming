import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

items={'Потепление': 'Постарайтесь охладить себя максимально',
       "Землетрясение":"Бегите на улицу и попытайтесь уйти от вещей которые могут упасть",
       'Разлив рек':'Покинте местность которая была затоплена',
       'Разрушение зданий':'Бегите срочно на улицу',
       'Похолодание':'Постарайтесь как можно сильнее утеплится',
       'Пожар':'Накройтесь тряпкой и срочно бегите из дома'
}

@bot.command()
async def start(ctx):
    await ctx.send('Приветствую,Чтобы  начать использовать нашего бота надо:1.написать команду /disaster 2.Написать название катастрофы с большой буквы 3.Ждать ответа бота')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def disaster(ctx, item):
    if item in items:
        time_to_disast = items[item]
        await ctx.send(f'{time_to_disast}')
    else:
        await ctx.send('Про такую катастрофу мы либо не знаем либо забыли')
        
bot.run("TOKEN")
