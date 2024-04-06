import discord
import os # default module
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)



#This file main.py can be seen as a cog itself. Only basic commands are here!

@bot.event
async def on_ready():
    print("UltraBot.py is up and running!")

@bot.command(description="Sends the bot's ping or latency")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency or ping is {bot.latency}")

@bot.command(description="If your program can't say this, don't talk to me")
async def helloworld(ctx):
    await ctx.respond("Hello world!")

#Don't worry, the french people joke is an inside joke with my friend
@bot.command(name="say")
async def _say(ctx, text):
    
    await ctx.send(text)
    await ctx.message.delete()


import json
with open("token.json", "r") as f:
  _d = json.load(f)
bot.run(_d["BOT_TOKEN"])
