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
import json
nltk.download('words')

word_list = ["Heads", "Tails"]
eightball_list = ["It is certain.", "It is decidedly so", "Without a doubt", "Yes - definitely", "You may rely on it", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again", "Ask again later", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
with open("version.json", "r") as f:
            _r = json.load(f)
            VERSION = _r["VERSION"]

with open("dev.json", "r") as f:
            _r = json.load(f)
            dev_status = _r["DEV_STATUS"]


#The Dev status is meant for if UltraBot is running in DEV mode which changes some names and icons.


if dev_status == "true":
            name = "UltraBot Development Edition"
            game = "with unstable ass commands"
            icon = "https://cdn.discordapp.com/avatars/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=1024"

if dev_status == "false":
            name = "UltraBot"
            game = "in the Python CMD"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"


class Fun(commands.Cog):
    group = discord.SlashCommandGroup(name="fun", description="Commands made for having fun!")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @group.command(name="cowsay", description="The cowsay command from Linux!")
    async def cowsay(self, ctx, text=discord.Option(str, description="Text for cow to say", required=True), 
                     character=discord.Option(str, description="Character for cowsay to use."), 
                     choices=cowsay.char_names, default="cow"):
        await ctx.respond("```\n{0}\n```".format(cowsay.get_output_string(character, text))),
    
    @group.command(name="randomword", description="Gives you a random English word!")
    async def randomword(self, ctx):
        await ctx.respond("Your Random Word: `" + random.choice(nltk.corpus.words.words()) + "`")
    
    @group.command(name="coinflip", description="Flip a coin!")
    async def coinflip(self, ctx):
        await ctx.respond(":coin: **" + random.choice(word_list) + "**")

    @group.command(name="8ball", description="The Magic 8 Ball answers your question!")
    async def _8ball(self, ctx, text=discord.Option(str, description="Question to ask the 8 ball")):
        embed = discord.Embed(
            title="Magic 8 Ball: " + text,
            description=random.choice(eightball_list),
            color=discord.Colour.darker_gray(),
            
        )
        embed.set_thumbnail(url="https://icons.iconarchive.com/icons/barkerbaggies/pool-ball/256/Ball-8-icon.png")
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
        await ctx.respond(embed=embed)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Fun(bot)) # add the cog to the bot

