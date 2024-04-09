import discord
from discord.ext import commands
import os
import random
WORDS = ["rock", "paper", "scissors"]

class Rps(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @commands.slash_command(title="rps", description="Play Rock Paper Scissors with UltraBot!")
    async def rps(self, ctx, choice: discord.Option(str, description="Your choice! Choose either rock, paper, or scissors.")):
        user_choice = choice.lower
        bot_choice = random.choice(WORDS)
        if bot_choice == "rock" and user_choice == "rock":
            win_status = "It's a TIE!"
        
        elif bot_choice == "rock" and user_choice == "paper":
            win_status = "You WON!"

        elif bot_choice == "rock" and user_choice == "scissors":
            win_status = "You LOST!"

        elif bot_choice == "paper" and user_choice == "rock":
            win_status = "You LOST!"

        elif bot_choice == "paper" and user_choice == "paper":
            win_status = "It's a TIE!"

        elif bot_choice == "paper" and user_choice == "scissors":
            win_status = "You WON!"

        elif bot_choice == "scissors" and user_choice == "rock":
            win_status = "You WON!"

        elif bot_choice == "scissors" and user_choice == "paper":
            win_status = "You LOST!"

        elif bot_choice == "scissors" and user_choice == "scissors":
            win_status = "It's a TIE!"

        embed = discord.Embed(
            title=win_status,
            description="You chose " + user_choice + ", UltraBot chose " + bot_choice,
            color=discord.Colour.red(),
        )
        embed.set_footer(text="UltraBot Rock Paper Scissors")

        await ctx.respond(embed=embed)








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Rps(bot)) # add the cog to the bot
