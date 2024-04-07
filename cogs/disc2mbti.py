import discord
from discord.ext import commands
import os

class Disc2mbti(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.slash_command(title="disc2mbti", description="Converts your Indigo DISC scores into MBTI personality types!")
    async def disc2mbti(self, ctx, d: discord.Option(int, description="Your Dominance Score"), i: discord.Option(int, description="Your Influence Score"), s: discord.Option(int, description="Your Steadiness Score"), c: discord.Option(int, description="Your Compliance Score")):
        await ctx.respond("Your MBTI is:")
        
        if i >= 50:
            await ctx.send("E")
        else:
            await ctx.send("I")
        
        if c >= 50:
            await ctx.send("S")
        else:
            await ctx.send("N")
        
        if d >= 50:
            await ctx.send("T")
        else:
            await ctx.send("F")
        
        if s >= 50:
            await ctx.send("J")
        else:
            await ctx.send("P")






def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Disc2mbti(bot)) # add the cog to the bot