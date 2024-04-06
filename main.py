import discord
import os # default module
from discord.ext import commands
import json
import logging
import cowsay
from discord import Option
from discord import User
from discord import Interaction
from discord import InteractionResponse
from discord import MessageInteraction
from discord import interactions
from discord import InteractionMessage


# Defing bot and bot user intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=';', intents=intents)

#loading cogs
bot.load_extension('cogs.moderation')
bot.load_extension('cogs.fun')


@bot.event
async def on_ready():
    status = discord.Game("in the Python CMD")
    await bot.change_presence(activity=status)
    bot.auto_sync_commands = True
    logging.info("Bot is ready!")


#UltraBot website button for /about
class AboutLinkBloggerView(discord.ui.View):
    def __init__(self):
     super().__init__(timeout=None)

     supportServerButton = discord.ui.Button(label='Learn More!', style=discord.ButtonStyle.gray, url='https://combinesoldier14.blogspot.com/p/ultrabot-links-faq.html')
     self.add_item(supportServerButton)

     supportServerButton = discord.ui.Button(label='GitHub', style=discord.ButtonStyle.gray, url='https://github.com/CombineSoldier14/UltraBot.py')
     self.add_item(supportServerButton)
    
class InviteView(discord.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

      supportServerButton = discord.ui.Button(label="Invite UltraBot.py!", style=discord.ButtonStyle.gray, url="https://discord.com/oauth2/authorize?client_id=1225220764861730867")
      self.add_item(supportServerButton)

#This file main.py can be seen as a cog itself. Only basic commands are here!

@bot.slash_command(name="ping", description="Sends the bot's ping or latency")
async def ping(ctx):
    await ctx.send(f"Pong! Latency or ping is {bot.latency}")

@bot.slash_command(name="helloworld", description="If your program can't say this, don't talk to me")
async def helloworld(ctx):
    await ctx.send("Hello world!")


@bot.slash_command(name="about", description="About the bot")
async def about(ctx):
    embed = discord.Embed(
        title= "About UltraBot.py",
        description= "UltraBot.py is a Python based discord bot created by CombineSoldier14 with commands for moderation and fun!\n UltraBot.py's birthday is **4/5/2024.**",
        color=discord.Colour.yellow(),
    )
    embed.set_thumbnail(url="https://camo.githubusercontent.com/7ebe7e305bde0efefd93829ed13a016cbfcad30985449dd5d54f612174aceb44/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6170702d69636f6e732f313232353232303736343836313733303836372f66363662643462656234663165626565303638356438633563666436343662622e706e673f73697a653d323536")
    embed.add_field(name="**Latest Addition**", value="Added /cowsay command!")
    await ctx.send(embed=embed, view=AboutLinkBloggerView())


# say is intentionally not a slash command.
@bot.command(name="say")
async def _say(ctx, *, args):
    await ctx.send(args)
    await ctx.message.delete()

@bot.slash_command(name="ephemeral", description="Sends an ephemeral message to yourself!")
async def ephemeral(ctx, text):
    await ctx.respond(text, ephemeral="true")
    
@bot.slash_command(name="spoiler", description="Marks your text as a spoiler!")
async def _spoiler(ctx, text):
    
    await ctx.send("||" + text + "||")
    

@bot.slash_command(name="invite", description="Get the invite link for UltraBot.py!")
async def invite(ctx):
   await ctx.send(view=InviteView())

# AutoRun prevention with __name__
if __name__ == "__main__": # import run prevention
    with open("token.json", "r") as f:
      _d = json.load(f)
    bot.run(_d["BOT_TOKEN"])
