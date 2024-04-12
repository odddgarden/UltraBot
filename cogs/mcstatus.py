import discord
from discord.ext import commands
import os
import json
import mcstatus
from mcstatus import JavaServer
from mcstatus import BedrockServer

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]

class mcstatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(name="mcjava", description="Get the status of a minecraft java server!")
    async def mcjava(self, ctx, server: discord.Option(str, description="Server URL to get info on.", required=True)):
           await ctx.defer()
           serverjava = JavaServer.lookup(server)
           javastatus = serverjava.status()
           javalatency = serverjava.ping()
           javaonline = javastatus.players.online
           javamaximum = javastatus.players.max
           javaprotocol = javastatus.version.protocol
           javaversion = javastatus.version.name
           
           
           embed = discord.Embed(
                  title="Info for " + server,
                  description="Info on the current minecraft server",
                  color=discord.Colour.green,
           )
           embed.add_field(name="Player(s) Online", value="{0}/{1}".format(javaonline, javamaximum))
           embed.add_field(name="Latency", value=f"{javalatency} ms")
           embed.add_field(name="Version/Protocol", value="{0} (Protocol {1})".format(javaversion, javaprotocol))
           embed.add_field(name="Secure Chat?", value=str(javastatus.enforces_secure_chat))
           
           
           await ctx.respond(embed=embed)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(mcstatus(bot)) # add the cog to the bot

           
