import discord
from discord.ext import commands
import os
from discord import reaction
from discord import Reaction

class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None





    @commands.slash_command(name="addrole", description="Adds a role to a user.")
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: discord.Option(discord.Member, description="User to give role to", required=True), role: discord.Option(discord.Role, description="Role to give user", required=True)):
       await user.add_roles(role, atomic=True)
       await ctx.respond("The role has been added to the user!")

    @commands.slash_command(name="removerole", description="Removes a role from a user.")
    @commands.has_permissions(manage_roles=True)
    async def removerole(self, ctx, user: discord.Option(discord.Member, description="User to remove role from", required=True), role: discord.Option(discord.Role, description="Role to remove", required=True)):
       await user.remove_roles(role, atomic=True)
       await ctx.respond("The role has been removed from the user!")

    @commands.slash_command(name="createrole", description="Creates a basic no perms role.")
    @commands.has_permissions(manage_roles=True)
    async def createrole(self, ctx, name: discord.Option(str, description="Name of role", required=True), server: discord.Option(discord.Guild, description="Name of the server to make role in. Case sensitive!", required=True)):
       await server.create_role(name=name)
       await ctx.respond("The role **" + name + "** has been created.")



def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(role(bot)) # add the cog to the bot
