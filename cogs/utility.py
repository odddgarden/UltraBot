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


    @commands.slash_command(name="makeembed", description="Make your own embed!")
    async def makeembed(self, ctx, title: discord.Option(str, description="Title of embed"), description: discord.Option(str, description="Description of embed"), footer: discord.Option(str, description="Footer of embed"), color: discord.Option(int, description="Color of embed in hex format")):
        embed = discord.Embed(
            title=title,
            description=description,
            color=color,
        )
        embed.set_footer(text=footer)
        await ctx.respond(embed=embed)






def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(utility(bot)) # add the cog to the bot
