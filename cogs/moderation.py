import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction
import json
import datetime

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]

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
       embed.set_footer(text="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")

       
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


    @commands.slash_command(name="timeout", description="Timeout a user.")
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, time: discord.Option(int, description="Amount of minutes to time out user", required=True), user: discord.Option(discord.Member, description="User to timeout", required=True)):
        await user.timeout_for(datetime.timedelta(minutes=time))
        await ctx.respond("{0} has been timed out for **{1}**.".format(user, time))



    @commands.slash_command(name="untimeout", description="Removes a timeout from a user.")
    @commands.has_permissions(moderate_members=True)
    async def untimeout(self, ctx, user: discord.Option(discord.Member, description="User to untimeout", required=True)):
        await user.remove_timeout()
        await ctx.respond("{0} has had their timeout removed!".format(user))


    @commands.slash_command(name="createchannel", description="Creates a basic text channel")
    @commands.has_permissions(manage_channels=True)
    async def createchannel(self, ctx, name: discord.Option(str, description="Name of channel"), guild: discord.Option(discord.Guild, description="Name of server to make channel in. Case sensitive!")):
        await guild.create_text_channel('{0}'.format(name))
        await ctx.respond("The channel **#{0}** has been created!".format(name))

    @commands.slash_command(name="createvoicechannel", description="Creates a basic voice channel")
    @commands.has_permissions(manage_channels=True)
    async def createchannel(self, ctx, name: discord.Option(str, description="Name of channel"), guild: discord.Option(discord.Guild, description="Name of server to make channel in. Case sensitive!")):
        await guild.create_voice_channel('{0}'.format(name))
        await ctx.respond("The channel **#{0}** has been created!".format(name))


    

    
       

    @ban.error
    async def ban_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
          await ctx.respond("You don't have permission to ban members.")

    @kick.error
    async def kick_error(self, ctx, error):
      if isinstance(error, commands.MissingPermissions):
          await ctx.respond("You don't have permission to kick members.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Moderation(bot)) # add the cog to the bot


