from discord.ext import commands 
import os
import random 
import discord
import requests

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)
bot.videos = ['https://www.youtube.com/watch?v=XmoKM4RunZQ', 'https://www.youtube.com/watch?v=qTmjKpl2Jk0', 'https://www.youtube.com/watch?v=hY7m5jjJ9mM']
bot.happylist = []

with open("api_key.txt", "r") as api_file:
  api_key = api_file.read()

@bot.command()
async def hello(ctx):
  await ctx.send("hello " + ctx.author.display_name)

@bot.command()
async def cat(ctx):
  await ctx.send(random.choice(bot.videos))

@bot.command()
async def happy(ctx, *, item):
  await ctx.send("Awesome!")
  bot.happylist.append(item)
  print(bot.happylist)

@bot.command()
async def sad(ctx):
  await ctx.send("Hope this makes you feel better!")
  await ctx.send(random.choice(bot.happylist))

@bot.command()
async def calc(ctx, x: float, fn: str, y: float):
  if fn == '+':
    await ctx.send(x + y)
  elif fn == '-':
    await ctx.send(x - y)
  elif fn == '*':
    await ctx.send(x * y)
  elif fn == '/':
    await ctx.send(x / y)
  else:
    await ctx.send("We only support 4 function operations")

@bot.command()
async def football_matches(ctx, *, input):
  url = "https://weatherapi-com.p.rapidapi.com/sports.json"

  querystring = {"q":input}

  headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)
  result = response.json()
  for i in range(len(result['football'])):
    await ctx.send("Stadium: " + result['football'][i]['stadium'])
    await ctx.send("Match: " + result['football'][i]['match'])
    await ctx.send("Start date and time: " + result['football'][i]['start'])

@bot.command()
async def translate(ctx, *, input):
  url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

  array = input.split()
  target = array[-1]
  source = array[-2]
  inp = ""
  for i in range(len(array)-2):
    inp += array[i]

  payload = {
    "q": inp,
    "target": target,
    "source": source
  }
  headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "d5422ad743mshb5838fa3f0ad240p147b26jsn0cc3de604996",
    "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
  }

  response = requests.post(url, data=payload, headers=headers)
  result = response.json()
  await ctx.send(result['data']['translations'][0]['translatedText'])


with open("bot_token.txt", "r") as token_file:
  TOKEN = token_file.read()
  print("Token file read")
  bot.run(TOKEN)