import discord
from discord.ext import commands
import os

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.slash_command(name="avatar", description="Find the avatar of the mentioned user!")
    async def avatar(self, ctx, user: discord.Option(discord.Member, description="Member to get avatar of", required=True)):
      await ctx.respond(user.display_avatar)






def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(utility(bot)) # add the cog to the bot