# bot.py
import random
import discord
import requests
from discord.ext import commands

api_url = "you url"

json_data = requests.get(api_url).json()

cityname = json_data["location"]["name"]
temp = json_data["current"]["temperature"]
weather_des = json_data["current"]["weather_descriptions"][0]

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def hello(ctx):
    await ctx.send('Hello')

@client.command(aliases=['Name'])
async def weather(ctx, *,question):
    if(question == 'weather?'):
        quip1 ='In'
        quip2 ='the weather calls for'
        quip3 ='with temperature being'
        quip4 ='degrees celcius'
        responses_des = weather_des
        responses_temp = temp
        responses_city = cityname
        await ctx.send(f'Question: {question}\nAnswer: {quip1} {responses_city} {quip2} {responses_des} {quip3} {responses_temp} {quip4}')

client.run('Token')
