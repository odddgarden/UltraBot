import discord
from discord.ext import commands
import os
from discord import default_permissions
from discord import permissions
from discord import Permissions
from discord import PermissionOverwrite
import requests
import json
import random
from random import uniform

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
            icon = "https://cdn.discordapp.com/app-icons/1227477531461025854/85f59950e14cca56e4b1bcefd911ca23.png?size=256"

if dev_status == "false":
            name = "UltraBot"
            game = "Ace Attorney: Dual Destinies"
            icon = "https://cdn.discordapp.com/app-icons/1225220764861730867/f66bd4beb4f1ebee0685d8c5cfd646bb.png?size=256"





class Apis(commands.Cog):
    group = discord.SlashCommandGroup(name="api", description="Commands that use online APIs made by other people")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    @group.command(name="dadjoke", description="Get a random dad joke!")
    async def dadjoke(self, ctx):
        r = requests.get("https://official-joke-api.appspot.com/random_joke")
        j = json.loads(r.text)
        await ctx.respond("{0} {1}".format(j["setup"], j["punchline"]))
    
    @group.command(name="xkcd", description="Get a random XKCD comic!")
    async def xkcd(self, ctx):
        xkcdlink = requests.get("https://xkcd.com/" + str(random.randint(1, 2916)) + "/info.0.json")
        xkcdjson = json.loads(xkcdlink.text)
            
        embed = discord.Embed(
            
            
            title="#" + str(xkcdjson["num"]) + " - " + xkcdjson["title"],
            description=xkcdjson["alt"],
            color=discord.Colour.blurple(),
            
            
        )
        embed.set_image(url=xkcdjson["img"])
        embed.set_footer(text="Year: " + str(xkcdjson["year"]) + ", Month " + str(xkcdjson["month"]) + ", Day " + str(xkcdjson["day"]))
        await ctx.respond(embed=embed)
    
    @group.command(name="dogpics", description="Random picture of a dog!")
    async def dogpics(self, ctx):
        doglink = requests.get("https://dog.ceo/api/breeds/image/random")
        dogjson = json.loads(doglink.text)

        embed = discord.Embed(
            title="Dog",
            color=discord.Colour.blurple(),
        )
        embed.set_image(url=dogjson["message"])
        embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
        await ctx.respond(embed=embed)
    
    @group.command(name="shakespeare", description="Translate english text to Shakespeare english!")
    async def shakespeare(self, ctx, text: discord.Option(str, description="Text to translate", required=True)):
         rshake = requests.get("https://api.funtranslations.com/translate/shakespeare.json?text={0}".format(text))
         jshake = json.loads(rshake.text)

         embed = discord.Embed(
              title = jshake["contents"]["translated"],
              description = jshake["contents"]["text"],
              color = discord.Colour.orange(),
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         embed.set_thumbnail(url="https://hips.hearstapps.com/hmg-prod/images/william-shakespeare-194895-1-402.jpg")
         await ctx.respond(embed=embed)


    @group.command(name="jojostand", description="Get a random jojo stand and its info!")
    async def jojostand(self, ctx):
         id = random.randint(1, 155)
         rstand = requests.get("https://stand-by-me.herokuapp.com/api/v1/stands/{0}".format(str(id)))
         jstand = json.loads(rstand.text)

         embed = discord.Embed(
              title=jstand["name"],
              description="""
              **Alternate name:** {0}
              **Japanese name:** {1}
              **Chapter:** {2}
              **Abilities:** {3}
              **Battle Cry:** {4}

               """.format(jstand["alternateName"], jstand["japaneseName"], jstand["chapter"], jstand["abilities"], jstand["battlecry"]),
               color=discord.Colour.blurple()
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         embed.set_image(url="https://jojos-bizarre-api.netlify.app/assets/{0}".format(jstand["image"]))

         await ctx.respond(embed=embed)


    @group.command(name="jojocharacter", description="Get a random jojo character and their info!")
    async def jojocharacter(self, ctx):
         ctx.defer()
         id = random.randint(1, 175)
         rchar = requests.get("https://stand-by-me.herokuapp.com/api/v1/characters/{0}".format(str(id)))
         jchar = json.loads(rchar.text)

         embed = discord.Embed(
              title=jchar["name"],
              description="""
              **Japanese name:** {0}
              **Abilities:** {1}
              **Nationality:** {2}
              **Catchphrase:** {3}
              **Family:** {4}
              **Chapter:** {5}
              **Still alive?** ||{6}||
              **Is human?** {7}

               """.format(jchar["japaneseName"], 
                          jchar["abilities"], 
                          jchar["nationality"], 
                          jchar["catchphrase"], 
                          jchar["family"], 
                          jchar["chapter"], 
                          ("yes" if jchar["living"] else "no"),
                          jchar["isHuman"]),
               color=discord.Colour.blurple()
         )
         embed.set_footer(text="{0} v{1}".format(name, VERSION), icon_url=icon)
         embed.set_image(url="https://jojos-bizarre-api.netlify.app/assets/{0}".format(jchar["image"]))
         await ctx.respond(embed=embed)
         
    @group.command(name="meme", description="Get a random meme from Reddit!")
    async def meme(self, ctx):
         rmeme = requests.get("https://meme-api.com/gimme")
         jmeme = json.loads(rmeme.text)
         
         embed = discord.Embed(
              title = jmeme["title"],
              description = "Upvote score: {0}".format(jmeme["ups"]),
              color = discord.Colour.blurple(),
         )
         embed.set_image(url=jmeme["url"])
         embed.set_footer(text="Posted in r/{0} by u/{1}".format(jmeme["subreddit"], jmeme["author"]))

         await ctx.respond(embed=embed)

    @group.command(name="randombreed", description="Get a random dog breed!")
    async def randombreeed(self, ctx):
               rbreed = requests.get("https://dog.ceo/api/breeds/list/all")
               breeds = list(json.loads(rbreed.text)["message"].keys())
               randbreed = random.choice(breeds)
               
               await ctx.respond(f":dog: `{randbreed}`")

    @group.command(name="urlshort", description="Shortens a given URL")
    async def urlshort(self, ctx, url: discord.Option(str, description="URL to shorten. Must begin with http(s)://")):
           
           rurl = requests.post("https://csclub.uwaterloo.ca/~phthakka/1pt-express/addURL", params={"long": url})
           jurl = json.loads(rurl.text)
           await ctx.respond("Your Shortened URL: https://1pt.co/{0}".format(jurl["short"]))
    
         
         
         
        

        








def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Apis(bot)) # add the cog to the bot
