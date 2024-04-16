import discord
from discord.ext import commands
import os




class Disc2mbti(commands.Cog):
    group = discord.SlashCommandGroup(name="fun", description="Non-serious commands for fun and enjoyment")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        

       

    @group.command(title="disc2mbti", description="Converts your Indigo DISC scores into MBTI personality types!")
    async def disc2mbti(self, ctx, d: discord.Option(int, description="Your Dominance Score"), i: discord.Option(int, description="Your Influence Score"), s: discord.Option(int, description="Your Steadiness Score"), c: discord.Option(int, description="Your Compliance Score")):
        
       
        if i >= 50:
            IE = "E"
            longIE = "Extraverted"
        else:
            IE = "I"
            longIE = "Introverted"
        
        if c >= 50:
            SN = "S"
            longSN = "Sensing"
        else:
            SN = "N"
            longSN = "Intuitive"
        
        if d >= 50:
            TF = "T"
            longTF = "Thinking"
        else:
            TF = "F"
            longTF = "Feeling"
        
        if s >= 50:
            PJ = "J"
            longPJ = "Judging"
        else:
            PJ = "P"
            longPJ = "Perceiving"

        await ctx.respond("Your MBTI is: {0}{1}{2}{3}".format(IE, SN, TF, PJ))
        await ctx.send("_({0}, {1}, {2}, and {3})_".format(longIE, longSN, longTF, longPJ))


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Disc2mbti(bot)) # add the cog to the bot
