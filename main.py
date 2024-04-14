@bot.slash_command(name="about", description="About the bot")
async def about(ctx):
    embed = discord.Embed(
        title= "About UltraBot v" + VERSION,
        description= "UltraBot is a Python based discord bot created by CombineSoldier14 with commands for moderation and fun!\n UltraBot's birthday is **4/5/2024.**",
        color=discord.Colour.yellow(),
    )
    embed.set_thumbnail(url="https://camo.githubusercontent.com/7ebe7e305bde0efefd93829ed13a016cbfcad30985449dd5d54f612174aceb44/68747470733a2f2f63646e2e646973636f72646170702e636f6d2f6170702d69636f6e732f313232353232303736343836313733303836372f66363662643462656234663165626565303638356438633563666436343662622e706e673f73697a653d323536")
    embed.add_field(name="**Latest Addition**", value="Added /botinfo!")
    await ctx.respond(embed=embed, view=AboutLinkBloggerView())


# say is intentionally not a slash command.
#The french people joke is an inside joke with my friends. I'm not racist! :)
@bot.command(name="say")
async def _say(ctx, *, args):
    if ctx.author.id == FRENCH:
        await ctx.send(":middle_finger: I don't take orders from French people, bozo!!!")
        await ctx.message.delete()
    else:
      await ctx.send(args)
      await ctx.message.delete()

@bot.slash_command(name="ephemeral", description="Sends an ephemeral message to yourself!")
async def ephemeral(ctx, text):
    await ctx.respond(text, ephemeral="true")
    
@bot.slash_command(name="spoiler", description="Marks your text as a spoiler!")
async def _spoiler(ctx, text):
    
    await ctx.respond("||" + text + "||")
    

@bot.slash_command(name="invite", description="Get the invite link for UltraBot!")
async def invite(ctx):
   await ctx.respond(view=InviteView())

# AutoRun prevention with __name__
if __name__ == "__main__": # import run prevention
    if os.path.isfile("token.json") == True: # check if token.json exists
        with open("token.json", "r") as f:
            _d = json.load(f)
            loadedJSONToken = _d["BOT_TOKEN"]
        if loadedJSONToken.lower() == "yourtokenhere":
            loadedJSONToken = None
    else:
        loadedJSONToken = None
    environToken = os.getenv("BOT_TOKEN")

    if (loadedJSONToken == None) and (environToken == None):
        raise EnvironmentError("No token specified!  Please enter a token via token.json or by passing an environment variable called 'BOT_TOKEN'.  Stop.")
    BOT_TOKEN = (environToken if environToken != None else loadedJSONToken)    
    bot.run(BOT_TOKEN)
