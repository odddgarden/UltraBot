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
     
    @commands.slash_command(name="dndrng", description="Get a random number between 2 values and roll DND dice!")
    async def dndrng(self, ctx, 
                  d4: discord.Option(int, description="How many times to roll the D4 dice", required=False, default=0), 
                  d6: discord.Option(int, description="How many times to roll the D6 dice", required=False, default=0),
                  d8: discord.Option(int, description="How many times to roll the D8 dice", required=False, default=0),
                  d10: discord.Option(int, description="How many times to roll the D10 dice", required=False, default=0),
                  d12: discord.Option(int, description="How many times to roll the D12 dice", required=False, default=0),
                  d20: discord.Option(int, description="How many times to roll the D20 dice", required=False, default=0),
                  custommax: discord.Option(int, description="A custom maximum.", required=False, default=0),
                  custommin: discord.Option(int, description="A custom minimum. MUST be accompanied by a custom maximum!!!", required=False, default=0),
                  customamount: discord.Option(int, description="How many times to do the custom min/max", required=False, default=0)):
        total = 0
        for _d4 in range(d4):
            total += random.randint(1, 4)
        
        for _d6 in range(d6):
            total += random.randint(1, 6)

        for _d8 in range(d8):
            total += random.randint(1, 8)

        for _d10 in range(d10):
            total += random.randint(1, 10)

        for _d12 in range(d12):
            total += random.randint(1, 12)

        for _d20 in range(d20):
            total += random.randint(1, 20)

        for _custom in range(customamount):
            total += random.randint(custommin, custommax)

        await ctx.respond(str(total))


        

        
        
        
    
    @commands.slash_command(name="add", description="Adds 2 numbers together")
    async def add(self, ctx, value1: discord.Option(int, description="The first number to add", required=True), value2: discord.Option(int, description="The second number to add", required=True)):
        await ctx.respond(str(value1 + value2))

    @commands.slash_command(name="multiply", description="Multiplies 2 numbers together")
    async def multiply(self, ctx, value1: discord.Option(int, description="The first number to multiply", required=True), value2: discord.Option(int, description="The second number to multiply", required=True)):
        await ctx.respond(str(value1 * value2))

    @commands.slash_command(name="divide", description="Divides 2 numbers")
    async def divide(self, ctx, value1: discord.Option(int, description="The first number to divide", required=True), value2: discord.Option(int, description="The second number to divide", required=True)):
        await ctx.respond(str(value1 / value2))

    
