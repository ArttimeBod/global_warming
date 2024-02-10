import discord
from discord.ext import commands
import os
import random
from neyro import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

items={'Потепление': 'Постарайтесь охладить себя максимально,https://rg.ru/2023/11/07/kak-prostoj-chelovek-mozhet-povliiat-na-globalnoe-poteplenie.html',
       "Землетрясение":"Бегите на улицу и попытайтесь уйти от вещей которые могут упасть, https://besafenet.net/ru/hazards/earthquakes/",
       'Разлив рек':'Покинте местность которая была затоплена,https://yandex.ru/pogoda/ru-RU/blog/14_facts_about_the_flood',
       'Разрушение зданий':'Бегите срочно на улицу, https://besafenet.net/ru/hazards/earthquakes/',
       'Похолодание':'Постарайтесь как можно сильнее утеплится,https://properm.ru/news/2024-02-09/poholodanie-do-27-gradusov-kakoy-budet-pogoda-v-permskom-krae-v-eti-vyhodnye-4993557',
       'Пожар':'Накройтесь тряпкой и срочно бегите из дома,https://xn--b1ae4ad.xn--p1ai/enc/pozhar'
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


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(image=f'./{attachment.filename}', model='keras_model.h5', labels='labels.txt'))
    else:
        await ctx.send('Вы забыли прикрепить картинку :(')

        
bot.run("MTEzMjI3NzgyMzEyNjYzNDQ5Nw.GBnSxF.N3iFVNCnEwxeVJ2JgQ7fAaZK9UbGusQ4dfJ_cA")
