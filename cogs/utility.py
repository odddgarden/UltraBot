import discord
from discord.ext import commands
import os
import time
import json

with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]




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

    @commands.slash_command(name="thread", description="Create a new basic thread")
    @commands.has_permissions(create_public_threads=True)
    async def thread(self, ctx, title: discord.Option(str, description="Title of thread", required=True), startmsg: discord.Option(str, description="Starting message in thread", required=True)):
        message = await ctx.send(startmsg)
        await message.create_thread(name=title)
        await ctx.respond("Your thread, **{0}**, has been created!".format(title))

    @commands.slash_command(name="gettime", description="Returns the current date and time.")
    async def gettime(self, ctx):
        await ctx.respond(time.ctime)

    @commands.slash_command(name="timestop", description="Stop time in a server JJBA style")
    @commands.has_permissions(manage_channels=True)
    async def timestop(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(
            title="ZA WARUDO!",
            description="Time has been stopped! No messages can be sent except for admins.",
            color=discord.Colour.red(),
        )
        embed.set_footer(text="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")
        embed.set_image(url="https://i.redd.it/05vtn9chak101.gif")
        await ctx.respond(embed=embed)

    @commands.slash_command(name="resume", description="Resumes time in a server")
    @commands.has_permissions(manage_channels=True)
    async def resume(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        await ctx.respond("Time has been resumed!")
    
    @commands.slash_command(name="userinfo", description="Gets info on a user in the server!")
    async def userinfo(self, ctx, user: discord.Option(discord.Member, description="User to get info of", required=True)):
        if user.bot == True:
         embed = discord.Embed(
             title="Info on {0}".format(user),
             description="""
             **ID:** {0}
             **Joined Discord:** {1}
             **Discriminator:** {2} 
             **Is A Bot?:** {3} 
             """.format(user.id, user.created_at, user.discriminator, user.bot),
             color=user.color,
          
         )
         embed.set_footer(text="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")
         embed.set_thumbnail(url=user.avatar)
        
        if user.bot == False:
    
         embed = discord.Embed(
             title="Info on {0}".format(user),
             description="""
             **ID:** {0}
             **Joined Discord:** {1} 
             **Is A Bot?:** {2} 
             """.format(user.id, user.created_at, user.bot),
             color=user.color,
          
         )
         embed.set_footer(text="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")
         embed.set_thumbnail(url=user.avatar)
        await ctx.respond(embed=embed)
          

    @commands.slash_command(name="botinfo", description="Info about UltraBot!")
    async def botinfo(self, ctx):
         embed = discord.Embed(
              title="Bot Info",
              description="""
              **Bot Name:** UltraBot
              **Bot Owner:** @combinesoldier14
              **Creation Date:** 4/5/2024
              **Server Count:** Unavailable
              **Library**: Py-cord {0}
              """.format(discord.__version__),
              color=discord.Colour.og_blurple(),
         )
         embed.set_footer(text="UltraBot " + VERSION, icon_url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")
         embed.set_thumbnail(url="https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256")
         await ctx.respond(embed=embed)








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(utility(bot)) # add the cog to the bot
