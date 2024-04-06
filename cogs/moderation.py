import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



    @commands.slash_command(name="userid", description="Find the ID of a mentioned user")
    async def userid(self, ctx, user: discord.Option(discord.Member, description="Member to find ID of", required="true")):
      await ctx.respond(f"That user's id is " + str(user.id))

    @commands.slash_command(name="ban", description="Bans a user.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Option(discord.Member, description="User to ban", required="true"), reason: discord.Option(str, description="Reason for ban", required="true")):
      await user.ban(reason = reason)
      embed = discord.Embed(
       title="Ban",
       description="The user " + str(user) + " has been banned from the server.",
       color=discord.Colour.red(),
    )
      embed.set_footer(text="Reason: " + reason)

      await ctx.respond(embed=embed)
    
    @commands.slash_command(name="kick", description="Kicks a user.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Option(discord.Member, description="User to kick", required="true"), reason: discord.Option(str, description="Reason for ban", required="true")):
      await user.kick(reason = reason)
      embed = discord.Embed(
       title="Kick",
       description="The user " + str(user) + " has been kicked from the server.",
       color=discord.Colour.red(),
    )
      embed.set_footer(text="Reason: " + reason)

      await ctx.respond(embed=embed)

    @ban.error
    async def ban_error(self, ctx, error):
     if isinstance(error, MissingPermissions):
          await ctx.send("You don't have permission to ban members.")

    @kick.error
    async def ban_error(self, ctx, error):
      if isinstance(error, MissingPermissions):
          await ctx.send("You don't have permission to kick members.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Moderation(bot)) # add the cog to the bot
