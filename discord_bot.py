# bot.py
import random
import discord
import requests
from discord.ext import commands
###from discord import Webhook, RequestsWebhookAdapter, File

###api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=a06034d422dcf0221001d54955a5f9d9='

client = commands.Bot(command_prefix = '-')

##webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN,\
##adapter=RequestsWebhookAdapter())
##webhook.send(&quot;Current Temp: &quot; + CURRENT_TEMP)
##webhook.send(file=discord.File(&quot;latest_img.jpg&quot;))


@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    await ctx.send('Hello')

@client.command()
async def time(ctx):
    await ctx.send('https://www.clocktab.com/')

@client.command()
async def TimetoHack(ctx):
    hacks = ['https://www.youtube.com/watch?v=QC2yBbHB7u4','https://www.youtube.com/watch?v=VbIbTT6bHkI','https://www.youtube.com/watch?v=7R91J9aPOuk', 'https://www.youtube.com/watch?v=AMVrIQeXR50']
    await ctx.send(f'Hack: {random.choice(hacks)}')


@client.command(aliases=['Hina'])
async def weather(ctx, *,question):
    if(question == 'weather?'):
        quip =['Here is the weather',
                'I pray for sunshine',
                'Hopefully it is sunny']
        responses =['https://www.accuweather.com/en/ca/burnaby/v5h/hourly-weather-forecast/47172']
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(quip)}\n{responses}')

client.run('Njc1ODI4NTA5NzkyMjcyNDAw.Xj87VA.h13O9JuM-AU5x2wJ-uce-VA331g')
#API key: 6e263e4aeb6f10d95c8509e4654c0da8
