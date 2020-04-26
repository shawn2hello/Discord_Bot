# bot.py
import random
import discord
import requests
from discord.ext import commands

api_url = "http://api.weatherstack.com/current?access_key=96b61cb41acaad6fe3b5d8b31465a586&query=vancouver"

json_data = requests.get(api_url).json()

cityname = json_data["location"]["name"]
temp = json_data["current"]["temperature"]
weather_des = json_data["current"]["weather_descriptions"][0]

print(f'\nCity: {city_name}') # f string, this way is a lot easier to concatenate together
print(f'Temperature is {temperature} degrees celcius.')
print(f'{weather_description}\n')

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    await ctx.send('Hello')

#@client.command()
#async def time(ctx):
    #await ctx.send('https://www.clocktab.com/')

#@client.command()
#async def TimetoHack(ctx):
    #hacks = ['https://www.youtube.com/watch?v=QC2yBbHB7u4','https://www.youtube.com/watch?v=VbIbTT6bHkI','https://www.youtube.com/watch?v=7R91J9aPOuk', 'https://www.youtube.com/watch?v=AMVrIQeXR50']
    #await ctx.send(f'Hack: {random.choice(hacks)}')


@client.command(aliases=['Hina'])
async def weather(ctx, *,question):
    if(question == 'weather?'):
        quip =['Here is the weather',
                'I pray for sunshine',
                'Hopefully it is sunny']
        responses =[weather_des]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(quip)}\n{responses}')

client.run('Njc1ODI4NTA5NzkyMjcyNDAw.Xj87VA.h13O9JuM-AU5x2wJ-uce-VA331g')
