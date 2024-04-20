import discord
from discord.ext import commands
import os




class Mbti(commands.Cog):
    group = discord.SlashCommandGroup(name="mbti", description="Commands relating to the Myers-Briggs Type Indicator personality system")
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        

       

    @group.command(title="disc2mbti", description="Converts your Indigo DISC scores into MBTI personality types!")
    async def disc2mbti(self, ctx, d: discord.Option(int, description="Your Dominance Score"), i: discord.Option(int, description="Your Influence Score"), s: discord.Option(int, description="Your Steadiness Score"), c: discord.Option(int, description="Your Compliance Score")):
        
       
        if i >= 50:
            IE = "E"
            longIE = "Extraverted"
        else:
            IE = "I"
            longIE = "Introverted"
        
        if c >= 50:
            SN = "S"
            longSN = "Sensing"
        else:
            SN = "N"
            longSN = "Intuitive"
        
        if d >= 50:
            TF = "T"
            longTF = "Thinking"
        else:
            TF = "F"
            longTF = "Feeling"
        
        if s >= 50:
            PJ = "J"
            longPJ = "Judging"
        else:
            PJ = "P"
            longPJ = "Perceiving"

        await ctx.respond("Your MBTI is: {0}{1}{2}{3}".format(IE, SN, TF, PJ))
        await ctx.send("_({0}, {1}, {2}, and {3})_".format(longIE, longSN, longTF, longPJ))

    @group.command(title="mbtitest", description="Take a test to figure out your MBTI personality type!")
    async def mbtitest(self, ctx, 
                       
                       #I or E questions
                       question1: discord.Option(str, description="I prefer to be around others usually.", choices=["yes", "no"]),
                       question2: discord.Option(str, description="I get more energy from my close friends than other people.", choices=["yes", "no"]),
                       question3: discord.Option(str, description="I always love when I'm the center of attention.", choices=["yes", "no"]),
                       question4: discord.Option(str, description="I get anxious and overwhelmed if I'm in a crowd of people for long enough.", choices=["yes", "no"]),
                       question5: discord.Option(str, description="I am quite popular in my respective social group.", choices=["yes", "no"]),
                       

                       
                       #S or N questions
                       question6: discord.Option(str, description="I like to participate in sports.", choices=["yes", "no"]),
                       question7: discord.Option(str, description="I'm always thinking about other things when I do things.", choices=["yes", "no"]),
                       question8: discord.Option(str, description="I'm able to think quickly in intense situations.", choices=["yes", "no"]),
                       question9: discord.Option(str, description="I like to make up stories and realities in my head.", choices=["yes", "no"]),
                       question10: discord.Option(str, description="I can tell very well what other people are thinking just by looking at them.", choices=["yes", "no"]),
                       question11: discord.Option(str, description="I honor tradition.", choices=["yes", "no"]),
                       question12: discord.Option(str, description="I prefer to use trusted methods then innovate.", choices=["yes", "no"]),
                       question13: discord.Option(str, description="I like to come up with a lot of ideas", choices=["yes", "no"]),


                       #T vs F questions
                       question14: discord.Option(str, description="I am good at puzzles.", choices=["yes", "no"]),
                       question15: discord.Option(str, description="My emotions control me more than I control them.", choices=["yes", "no"]),
                       question16: discord.Option(str, description="I tend to feel insecure/depressed often.", choices=["yes", "no"]),
                       question17: discord.Option(str, description="I like to focus on science and the facts rather than my own beliefs.", choices=["yes", "no"]),
                       question18: discord.Option(str, description="I always need someone to rely on for things.", choices=["yes", "no"]),
                       question19: discord.Option(str, description="I like solutions that are efficient rather then ones that make people happy.", choices=["yes", "no"]),

                       #P vs J questions
                       question20: discord.Option(str, description="I like to make a lot of backup plans to make sure there's a way for everything.", choices=["yes", "no"]),
                       question21: discord.Option(str, description="I like to just do whatever I feel like doing instead of having a schedule.", choices=["yes", "no"]),
                       question22: discord.Option(str, description="I am always organized with access to everything.", choices=["yes", "no"]),
                       question23: discord.Option(str, description="I get distracted very easily.", choices=["yes", "no"]),
                       question24: discord.Option(str, description="I usually do the bare minimum needed for things and not put in extra effort.", choices=["yes", "no"]),
                      
                       ):
     inumber = 0
     enumber = 0
     snumber = 0
     nnumber = 0
     tnumber = 0
     fnumber = 0
     pnumber = 0
     jnumber = 0

     if question1 == "yes":
         enumber += 1
     else:
         inumber += 1

     if question2 == "yes":
         inumber += 1
     else:
         enumber += 1

     if question3 == "no":
         inumber += 1
     else:
         enumber += 1

     if question4 == "yes":
         inumber += 1
     else:
         enumber += 1

     if question5 == "no":
         inumber += 1
     else:
         enumber += 1

     if question6 == "yes":
         snumber += 1
     else:
         nnumber += 1

     
     if question7 == "no":
         nnumber += 1
     else:
         snumber += 1

     if question8 == "yes":
         snumber += 1
     else:
         nnumber += 1

     if question9 == "no":
         snumber += 1
     else:
         nnumber += 1

     if question10 == "yes":
         snumber += 1
     else:
         nnumber += 1

     if question11 == "yes":
         snumber += 1
     else:
         nnumber += 1

     if question12 == "yes":
         snumber += 1
     else:
         nnumber += 1

     

     if question13 == "no":
         snumber += 1
     else:
         nnumber += 1

     if question14 == "yes":
         tnumber += 1
     else:
         fnumber += 1

     if question15 == "no":
         tnumber += 1
     else:
         fnumber += 1

     if question16 == "no":
         tnumber += 1
     else:
         fnumber += 1

     if question17 == "yes":
         tnumber += 1
     else:
         fnumber += 1

     if question18 == "no":
         tnumber += 1
     else:
         fnumber += 1

     if question19 == "yes":
         tnumber += 1
     else:
         fnumber += 1

     if question20 == "no":
         pnumber += 1
     else:
         jnumber += 1

     if question21 == "yes":
         pnumber += 1
     else:
         jnumber += 1

     if question22 == "no":
         pnumber += 1
     else:
         jnumber += 1

     if question23 == "yes":
         pnumber += 1
     else:
         jnumber += 1

     if question24 == "yes":
         pnumber += 1
     else:
         jnumber += 1
         
     

     #now for percentages

     iperc1 = inumber / 5
     eperc1 = enumber / 5
     sperc1 = snumber / 8
     nperc1 = nnumber / 8
     tperc1 = tnumber / 6
     fperc1 = fnumber / 6
     pperc1 = pnumber / 5
     jperc1 = jnumber / 5
     iperc2 = iperc1 * 100
     eperc2 = eperc1 * 100
     sperc2 = sperc1 * 100
     nperc2 = nperc1 * 100
     tperc2 = tperc1 * 100
     fperc2 = fperc1 * 100
     pperc2 = pperc1 * 100
     jperc2 = jperc1 * 100
     iperc3 = round(iperc2, 0)
     eperc3 = round(eperc2, 0)
     sperc3 = round(sperc2, 0)
     nperc3 = round(nperc2, 0)
     tperc3 = round(tperc2, 0)
     fperc3 = round(fperc2, 0)
     pperc3 = round(pperc2, 0)
     jperc3 = round(jperc2, 0)


     if iperc3 > eperc3:
         iestatus = "I"
         ielong = "Introverted"
         

     else:
         iestatus = "E"
         ielong = "Extroverted"

     if snumber > nnumber:
         snstatus = "S"
         snlong = "Sensing"
     

     
    
    
     else:
         snstatus = "N"
         snlong = "Intuitive"

     if tnumber > fnumber:
         tfstatus = "T"
         tflong = "Thinking"
     else:
         tfstatus = "F"
         tflong = "Feeling"

     if pnumber > jnumber:
         pjstatus = "P"
         pjlong = "Perceiving"
     else:
         pjstatus = "J"
         pjlong = "Judging"

     


     

     embed = discord.Embed(
         title="Your MBTI: {0}{1}{2}{3}".format(iestatus, snstatus, tfstatus, pjstatus),
         description="""
         _{0}, {1}, {2}, and {3}_

         **Percentages:**
         {4}% Introverted, {5}%. Extroverted
         {6}% Sensing, {7}% Intuitive
         {8}% Thinking, {9}%, Feeling
         {10}% Perceiving, {11}% Judging
         """.format(ielong, snlong, tflong, pjlong, str(iperc3), str(eperc3), str(sperc3), str(nperc3), str(tperc3), str(fperc3), str(pperc3), str(jperc3)),
         color=discord.Colour.red()
     )
     embed.set_footer(text="Learn more about this type: https://www.16personalities.com/{0}{1}{2}{3}-personality".format(iestatus.lower(), snstatus.lower(), tfstatus.lower(), pjstatus.lower()))
     await ctx.respond(embed=embed)

    @group.command(name="mostmbti", description="A command to find what the most (blank) MBTI is!")
    async def mostmbti(self, ctx, most1: discord.Option(str, description="The first option to find what the most (blank) (blank) MBTI is!", choices=["introverted", "extroverted", "intuitive", "sensing", "thinking", "feeling", "perceiving", "judging"]), most2: discord.Option(str, description="The second option to find what the most (blank) (blank) MBTI is!", choices=["introvert", "extrovert", "intuitive", "senser", "thinker", "feeler", "perceiver", "judger"])):
        mbti = "undefined"
        if most1 == "introverted" and most2 == "introvert" or most1 == "introverted" and most2 == "judger" or most1 == "introverted" and most2 == "intuitive" or most1 == "introverted" and most2 == "thinker":
            mbti = "INTJ"

        if most1 == "introverted" and most2 == "senser":
            mbti = "ISTJ"

        if most1 == "introverted" and most2 == "extrovert":
            mbti = "ENFP"

        if most1 == "introverted" and most2 == "feeler":
            mbti = "INFP"

        if most1 == "introverted" and most2 == "perceiver":
            mbti = "INTP"

        if most1 == "extroverted" and most2 == "extrovert" or most1 == "extroverted" and most2 == "sensor" or most1 == "extroverted" and most2 == "thinker" or most1 == "extroverted" and most2 == "perceiver":
            mbti = "ESTP"

        if most1 == "extroverted" and most2 == "intuitive" or most1 == "extroverted" and most2 == "judger":
            mbti = "ENFJ"

        if most1 == "extroverted" and most2 == "feeler":
            mbti = "ESFP"

        if most1 == "intuitive" and most2 == "intuitive" or most1 == "introverted" and most2 == "":
            mbti = "INFJ"

        

        

        

        await ctx.respond("The most {0} {1} is **{2}**".format(most1, most2, mbti))
        




     



        
     


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Mbti(bot)) # add the cog to the bot
