import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None



    @commands.slash_command(name="userid", description="Find the ID of a mentioned user")
    async def userid(self, ctx, user: discord.Option(discord.Member, description="Member to find ID of", required="true")):
      await ctx.respond(f"That user's id is " + str(user.id))

    @commands.slash_command(name="ban", description="Bans a user.")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Option(discord.Member, description="User to ban", required=True), 
                  reason: discord.Option(str, description="Reason for ban", required=True)):
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
    async def kick(self, ctx, user: discord.Option(discord.Member, description="User to kick", required=True), 
                  reason: discord.Option(str, description="Reason for ban", required=True)):
      await user.kick(reason = reason)
      embed = discord.Embed(
       title="Kick",
       description="The user " + str(user) + " has been kicked from the server.",
       color=discord.Colour.red(),
    )
      embed.set_footer(text="Reason: " + reason)

      await ctx.respond(embed=embed)

    @commands.slash_command(name="poll", description="Creates a votable yes or no poll!")
    @commands.has_permissions(administrator = True)
    async def poll(self, ctx, title: discord.Option(str, description="Title of poll", required=True), description: discord.Option(str, description="Your yes or no poll description", required=True)):
       embed = discord.Embed(
          title=title,
          description=description,
          color=discord.Colour.blurple(),

       )
       embed.set_footer(text="UltraBot.py poll system")

       
       emoji = '\N{THUMBS UP SIGN}'
       emoji2 = '\N{THUMBS DOWN SIGN}'
       message = await ctx.send(embed=embed)
       await message.add_reaction(emoji)
       await message.add_reaction(emoji2)
    
    @commands.slash_command(name="purge", description="Purges a certain number of messages from a channel")
    @commands.has_permissions(manage_messages = True)
    @commands.has_permissions(read_message_history = True)
    async def purge(self, ctx, number: discord.Option(int, description="Number of messages to purge. Max is 100", required=True)):
       await ctx.channel.purge(limit=number)
       await ctx.respond("**" + str(number) + "** messages have been purged!")
       

    @ban.error
    async def ban_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
          await ctx.respond("You don't have permission to ban members.")

    @kick.error
    async def ban_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
          await ctx.respond("You don't have permission to kick members.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Moderation(bot)) # add the cog to the b
