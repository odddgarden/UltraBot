import discord
from discord.ext import commands
import os

class Disc2mbti(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

        self._MBTI_STRINGS = {
            # index 0: I/E
            "I": "Introverted",
            "E": "Extraverted",
            # index 1: N/S
            "N": "Intuitive",
            "S": "Sensing",
            # index 2: T/F
            "T": "Thinking",
            "F": "Feeling",
            # index 3: J/P
            "P": "Prospecting",
            "J": "Judging"
        }
        self._CONSTRUCT = "{0} *({1}, {2}, {3}, and {4})*"

    @commands.slash_command(title="disc2mbti", description="Converts your Indigo DISC scores into MBTI personality types!")
    async def disc2mbti(self, ctx, d: discord.Option(int, description="Your Dominance Score"), i: discord.Option(int, description="Your Influence Score"), s: discord.Option(int, description="Your Steadiness Score"), c: discord.Option(int, description="Your Compliance Score")):
        await ctx.respond("Your MBTI is:")
        
        currentMbti = [None, None, None, None] # initalize empti mbti
        if i >= 50:
            currentMbti[0] = "E"
        else:
            currentMbti[0] = "I"
        
        if c >= 50:
            currentMbti[1] = "S"
        else:
            currentMbti[1] = "N"
        
        if d >= 50:
            currentMbti[2] = "T"
        else:
            currentMbti[2] = "F"
        
        if s >= 50:
            currentMbti[3] = "J"
        else:
            currentMbti[3] = "P"

        await ctx.respond(self._CONSTRUCT.format("".join(currentMbti),
                                                 self._MBTI_STRINGS[currentMbti[0]],
                                                 self._MBTI_STRINGS[currentMbti[1]],
                                                 self._MBTI_STRINGS[currentMbti[2]],
                                                 self._MBTI_STRINGS[currentMbti[3]]))



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Disc2mbti(bot)) # add the cog to the bot