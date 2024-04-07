import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import cowsay
import nltk
import random
nltk.download('words')

word_list = ["Heads", "Tails"]
random_word = random.choice(word_list)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.slash_command(name="cowsay", description="The cowsay command from Linux!")
    async def cowsay(self, ctx, text=discord.Option(str, description="Text for cow to say", required=True), 
                     character=discord.Option(str, description="Character for cowsay to use."), 
                     choices=cowsay.char_names, default="cow"):
        await ctx.respond("```\n{0}\n```".format(cowsay.get_output_string(character, text))),
    
    @commands.slash_command(name="randomword", description="Gives you a random English word!")
    async def randomword(self, ctx):
        await ctx.respond("Your Random Word: `" + random.choice(nltk.corpus.words.words()) + "`")
    
    @commands.slash_command(name="coinflip", description="Flip a coin!")
    async def coinflip(self, ctx):
        await ctx.respond(":coin: **" + random_word + "**")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot)) # add the cog to the bot
