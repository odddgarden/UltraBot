import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import random

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
     
    @commands.slash_command(name="rng", description="Get a random number between 2 values!")
    async def rng(self, ctx, min: discord.Option(int, description="The minimum value", required=True), max: discord.Option(int, description="The maximum value", required=True)):
        await ctx.respond(str(random.randint(min, max)))
    
    @commands.slash_command(name="add", description="Adds 2 numbers together")
    async def add(self, ctx, value1: discord.Option(int, description="The first number to add", required=True), value2: discord.Option(int, description="The second number to add", required=True)):
        await ctx.respond(str(value1 + value2))

    @commands.slash_command(name="multiply", description="Multiplies 2 numbers together")
    async def multiply(self, ctx, value1: discord.Option(int, description="The first number to multiply", required=True), value2: discord.Option(int, description="The second number to multiply", required=True)):
        await ctx.respond(str(value1 * value2))

    @commands.slash_command(name="divide", description="Divides 2 numbers")
    async def divide(self, ctx, value1: discord.Option(int, description="The first number to divide", required=True), value2: discord.Option(int, description="The second number to divide", required=True)):
        await ctx.respond(str(value1 / value2))

    








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Calc(bot)) # add the cog to the b