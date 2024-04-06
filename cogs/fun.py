import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import cowsay

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.slash_command(name="cowsay", description="The cowsay command from Linux!")
    async def cowsay(self, ctx, text=discord.Option(str, description="Text for cow to say", required="true")):
        await ctx.respond(f"``` \n" + cowsay.get_output_string(f'cow', str(text)) + "\n ```")



    

    

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot)) # add the cog to the bot