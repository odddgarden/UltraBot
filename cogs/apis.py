import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import requests
import json
import random
from random import uniform

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]


r = requests.get("https://official-joke-api.appspot.com/random_joke")
j = json.loads(r.text)

class Apis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.slash_command(name="dadjoke", description="Get a random dad joke!")
    async def dadjoke(self, ctx):
        await ctx.respond("{0} {1}".format(j["setup"], j["punchline"]))
    
    @commands.slash_command(name="xkcd", description="Get a random XKCD comic!")
    async def xkcd(self, ctx):
        xkcdlink = requests.get("https://xkcd.com/" + str(random.randint(1, 2916)) + "/info.0.json")
        xkcdjson = json.loads(xkcdlink.text)
            
        embed = discord.Embed(
            
            
            title="#" + str(xkcdjson["num"]) + " - " + xkcdjson["title"],
            description=xkcdjson["alt"],
            color=discord.Colour.blurple(),
            
            
        )
        embed.set_image(url=xkcdjson["img"])
        embed.set_footer(text="Year: " + str(xkcdjson["year"]) + ", Month " + str(xkcdjson["month"]) + ", Day " + str(xkcdjson["day"]))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name="dogpics", description="Random picture of a dog!")
    async def dogpics(self, ctx):
        doglink = requests.get("https://dog.ceo/api/breeds/image/random")
        dogjson = json.loads(doglink.text)

        embed = discord.Embed(
            title="Dog",
            color=discord.Colour.blurple(),
        )
        embed.set_image(url=dogjson["message"])
        embed.set_author(name="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")
        await ctx.respond(embed=embed)
        

        








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Apis(bot)) # add the cog to the bot
