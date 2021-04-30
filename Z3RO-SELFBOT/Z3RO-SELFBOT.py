_T='none'
_S='Whitelist Argument returns : null'
_R='Status code: 200'
_Q='Thank you for using Z3RO self bot!'
_P='stop bind'
_O='./selfbot_config.json'
_N='Reason'
_M=True
_L='prefix'
_K='token'
_J='{0}Member {1} failed to be removed from the server'
_I='You must give a white listed user, or give the keyword "none" to show you don\'t want to use whitelist.'
_H='Z3RO RAID TOOL'
_G='Z3RO SB (self bot) was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)'
_F='start bind'
_E='stop_bind'
_D='Z3RO SB'
_C=None
_B='Ã¢Å“â€¦'
_A='sleep_delete'
api_key = "JHC0TV1ARRKT"
lmt = 8
import discord,json,asyncio,keyboard,pyautogui,colorama,time
from pyautogui import alert
from discord.ext import commands
from colorama import Fore,Back,Style
import requests
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("--headless")
import time
import nekos
noted = []

driver = webdriver.Chrome(options=chrome_options)
with open("selfbot_config.json")as f:config=json.load(f)
configDict={_K:config.get(_K),_L:config.get(_L),_E:config.get(_P),_A:config.get('sleep delete'),'bot_reaction':config.get('bot reaction'),_F:config.get(_F)}   

Z3RO=commands.Bot(description='Z3RO Self bot',command_prefix=configDict[_L],self_bot=_M)
@Z3RO.command()
async def about(ctx):
        B=ctx
        try:await B.message.delete();C=discord.Embed(title=_D,description='Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001',color=10038562);A=await B.send(embed=C);await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete()
        except:await B.message.delete();A=await B.send(f"**ZERO SB** \n**Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001");await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete();await A.delete()
        
        
@Z3RO.command()
async def spam(ctx,amount : int=None,*,msg):
        B=ctx
        if amount is _C:await B.message.delete();C=discord.Embed(title=_D,description='Spam Amount returns : null',color=10038562);C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete()
        elif msg is _C:await B.message.delete();C=discord.Embed(title=_D,description='Message Arguement returns : null',color=10038562);C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete()
        else:
                try:
                        await B.message.delete();C=discord.Embed(title='ZERO SB',description='Successful command. Spamming is 3 seconds...',color=10038562);C.add_field(name='Bind',value=f"Press {configDict[_E]} to stop the spam!");C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        for F in range(amount):
                                await B.send(msg)
                                if keyboard.is_pressed(configDict[_E]):break
                except:
                        alert("Spamming in 3 seconds.")
                        for F in range(amount):
                                await B.send(msg);await asyncio.sleep(0.5)
                                if keyboard.is_pressed(configDict[_E]):break
@Z3RO.command()
async def massreact(ctx, reactionID=None, reactAmount : int=None):
        if reactionID == None:
                alert("Yo must give a reaction.")
        elif reactAmount == None:
                alert("Start mass reaction spam in 3 seconds..")
                await asyncio.sleep(3)
                messages = await ctx.message.channel.history(limit=50).flatten()
                for message in messages:
                        await message.add_reaction(reactionID)
        else:
                if reactAmount > 50:
                        alert("You cannot react to more than 50 messages (to stay undetected).")
                else:
                        alert("Start mass reaction spam in 3 seconds..")
                        await asyncio.sleep(3)
                        messages = await ctx.message.channel.history(limit=reactAmount).flatten()
                        for message in messages:
                                await message.add_reaction(reactionID)
@Z3RO.command()
async def quickdel(ctx):
        A=ctx;D=discord.Embed(title=_D,description=f"Press {configDict[_F]} to start quick del and {configDict[_E]} to pause quick del");B=await A.send(embed=D);await B.add_reaction("✅");await asyncio.sleep(configDict[_A]);await B.delete()
        while _M:
                if keyboard.is_pressed(configDict[_F]):
                        while _M:
                                E=await A.message.channel.history(limit=20).flatten()
                                for C in E:
                                        if C.author==A.message.author:await C.delete()
                                if keyboard.is_pressed(configDict[_E]):break
import discord,pyautogui,json,asyncio,keyboard
from pyautogui import alert
from discord.ext import commands
with open(_O)as f:config=json.load(f)
count=0
@Z3RO.event
async def on_ready():
        global embeds
        alert("Thank you for using the newest and most imrpoved version of Z3RO self bot! Version: 0.15.0")
        alert(text=_Q + "(check terminal for embed enable/disable)");print(_R)
        print('Bot Online - developer: \ndiscord: zemult \nyoutube: zemult')
        embeds = False
        while True:
                embedInput = int(input("Would you like embeds? \n1: Yes \n2: No"))
                if type(embedInput) == int:
                        if embedInput == 1:
                                embeds = True
                                break
                        elif embedInput == 2:
                                break
                        else:
                                print("Choose between 1 and 2.")
                else:
                        print("Enter a number between 1 and two.")
@Z3RO.command()
async def mcs(ctx,channelName=_C,channelAmount=_C):
        D='**Z3RO RAID TOOL** \n**Channel Amount Argument returns : null** \n**Reason: ** \n**You must give a channel amount.**';E='Z3RO RAID TOOL was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)';F=channelAmount;G=channelName;B=ctx
        if G==_C:
                if embeds:
                        try:await B.message.delete();C=discord.Embed(title=_H,description='Channel Name Argument returns : null',color=10038562);C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)');A=await B.send(embed=C);await A.add_reaciton("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        except:alert("This server does not allow embeds. \nChannel Name Argument returns : null")
                else:
                        alert("Channel arg returns: null")
        elif F==_C:
                if embeds:
                        try:await B.message.delete();C=discord.Embed(title=_H,description='Channel Amount Argument returns : null',color=10038562);C.set_footer(text=E);A=await B.send(embed=C);await A.add_reaciton("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        except:await B.message.delete();A=await B.message.send(D);await A.add_reaciton("✅");await asyncio.sleep(configDict[_A])
        else:
                try:
                        await B.message.delete();C=discord.Embed(title=_H,description='Spamming channels in 3 seconds...',color=10038562);C.set_footer(text=E);A=await B.send(embed=C);await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        for H in range(F):
                                await B.guild.create_text_channel(G)
                                if keyboard.is_pressed(configDict[_P]):break
                except:await B.message.delete();A=await B.send(D);await A.add_reaction("✅");await asyncio.sleep(configDict[_A])
@Z3RO.command()
async def mscd(ctx):
        D='Channel {} successfully deleted';E='Destroying all channels in 3 seconds...';A=ctx
        try:
                F=discord.Embed(title=_H,description=E,color=10038562);B=await A.send(embed=F);await B.add_reaction("✅");await asyncio.sleep(3);await B.delete()                
                for C in list(A.guild.channels):await C.delete();print(D.format(C.id))
        except:
                await A.message.delete();B=await A.send('**Z3RO RAID TOOL',description=E);await B.add_reaction("✅");await asyncio.sleep(3);await B.delete()     
                for C in list(A.guild.channels):await C.delete();print(D.format(C.id))
@Z3RO.command()
async def massban(ctx,whitelist):
        G='{0}Member {1} was successfully banned.';E='Starting mass ban in 3 seconds...';F=whitelist;B=ctx;H=list(B.guild.members)
        if F==_C:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=_S,color=10038562);D.add_field(name=_N,text=_I);C=await B.send(embed=D);await C.add_reaction("✅");await asyncio.sleep(configDict[_A])
                except:alert(text=_I)
        elif F.strip().lower()==_T:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=E,color=10038562);C=await B.send(embed=D);await C.add_reaction("✅");await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=E)
                for A in H:
                        try:await A.ban();print(G.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
        else:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=E,color=10038562);C=await B.send(embed=D);await C.add_reaction("✅");await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=E)
                for A in H:
                        try:
                                I=await Z3RO.fetch_user(F)
                                if I==A:print('{0}Member {1} was not banned because he/she was whitelisted.'.format(Fore.RED,A.id))
                                else:await A.ban();print(G.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
@Z3RO.command()
async def masskick(ctx,*,whitelist):
        E='Starting mass kick in 3 seconds...';F=whitelist;B=ctx;G=list(B.guild.members)
        if F==_C:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=_S,color=10038562);D.add_field(name=_N,text=_I);C=await B.send(embed=D);await C.add_reaction("✅");await asyncio.sleep(configDict[_A])
                except:alert(text=_I)
        elif F.strip().lower()==_T:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=E,color=10038562);C=await B.send(embed=D);await C.add_reaction("✅");await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=E)
                for A in G:
                        try:await A.kick();print('{0}Member {1} was successfully kick.'.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
        else:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=E,color=10038562);C=await B.send(embed=D);await C.add_reaction("✅");await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=E)
                for A in G:
                        try:
                                H=await Z3RO.fetch_user(F)
                                if H==A:print('{0}Member {1} was not kicked because he/she was whitelisted.'.format(Fore.RED,A.id))
                                else:await A.kick();print('{0}Member {1} was successfully kicked.'.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
@Z3RO.command()
async def inftype(ctx,time=_C):
        A=ctx;await A.message.delete()
        if time==_C:alert('You must give a time amount. (in seconds)')
        else:
                async with A.typing():await asyncio.sleep(time)
                B=await A.send('done typing lmao');await asyncio.sleep(0.5);await B.delete()
@Z3RO.command()
async def nuke(ctx):
        B=ctx;alert('Nuking server in 3 seconds...')
        try:
                print(Fore.GREEN+'Attempting to ban members.')
                for A in list(B.guild.members):
                        try:await A.ban();print(Fore.GREEN+'{} was successfully banned.'.format(A.id))
                        except:print(Fore.RED+'{} could not be banned.'.format(A.id))
                for A in list(B.guild.members):
                        try:await A.kick();print(Fore.GREEN+'{} was successfully kicked.'.format(A.id))
                        except:print(Fore.RED+'{} could not be kicked'.format(A.id))
                for A in list(B.guild.members):
                        try:
                                C=discord.utils.get(B.guild.roles,name='muted')
                                if C in B.guild.roles:
                                        for A in list(B.guild.members):
                                                try:await A.add_roles(C);print(Fore.GREEN+'{} was successfully muted'.format(A.id))
                                                except:C=discord.utils.get(B.guild.roles,name='Muted');await A.add_roles(C);print(Fore.GREEN+'{} was successfully muted.'.format(A.id))
                        except:return
                for A in list(B.guild.channels):
                        try:await A.delete();print(Fore.GREEN+'Channel {} was successfully deleted'.format(A.id))
                        except:print(Fore.GREEN+'Channel {} could not be deleted'.format(A.id))
                        
                for i_ in list(ctx.guild.roles):
                        try:
                                await i_.delete()
                                print(Fore.GREEN + "Role {} was successfully deleted.".format(i_.id))
                        except:
                                print(Fore.GREEN + "Role {} could not be deleted.".format(i_.id))

        except:print(Fore.RED+'Failed to access to the server: {}.'.format(B.guild.id))
        
@Z3RO.command()
async def poll(ctx, *, pollMsg=None):
        if pollMsg == None:
                alert("You must give a message for the poll.")
        else:
                poll = await ctx.send(pollMsg)
                await poll.add_reaction("👍")                
@Z3RO.command()
async def massdm(ctx, userID : int=None, amount : int=None, *, msg : str=None):
        if userID == None:
                if embeds:
                        try:await ctx.message.delete();C=discord.Embed(title=_H,description='User ID Argument returns : null',color=10038562);C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)');A=await B.send(embed=C);await A.add_reaciton("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        except:alert("This server does not allow embeds. \nUser ID arg returns : null")
                else:alert("This server does not allow embeds. \nUser ID arg returns : null")
        elif msg == None:
                return
        elif amount == None:
                if embeds:
                        try:await ctx.message.delete();C=discord.Embed(title=_H,description='Message Amount Argument returns : null',color=10038562);C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)');A=await B.send(embed=C);await A.add_reaciton("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        except:alert("This server does not allow embeds. \Message Amount arg returns : null")
                else:alert("Message Amount arg returns : null")
        else:
                try:
                        user = await Z3RO.fetch_user(userID);
                        for _MS in range(amount):
                                await user.send(msg)
                except:alert("Message failed to send")
        

@Z3RO.command()
async def ttsSpam(ctx, amount : int=None, *, message):
        d = amount
        message = C
        if D == _C:
                if embeds:
                        try:
                                await ctx.message.delete();C=discord.Embed(title=_H,description='Message Amount Argument returns : null',color=10038562)
                                C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)')
                                A=await B.send(embed=C);await A.add_reaciton("✅")
                                await asyncio.sleep(configDict[_A])
                                await A.delete()
                        except:
                                alert("This server does not allow embeds. \nMessage Amount Arg returns : null")
                else:
                        alert("Message amount arg returns : null")
        if C == _C:
                if embeds:
                        try:
                                await ctx.message.delete()
                                C=discord.Embed(title=_H,description='Message Argument returns : null',color=10038562)
                                C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)')
                                A=await B.send(embed=C)
                                await A.add_reaciton("✅")
                                await asyncio.sleep(configDict[_A])
                                await A.delete()
                        except:
                                alert("This server does not allow embeds. \nMessage Arg returns : null")
                else:
                        alert("Message Arg returns : null")
        else:
                if embeds:
                        try:await B.message.delete();C=discord.Embed(title='ZERO SB',description='Successful command. Spamming is 3 seconds...',color=10038562);C.add_field(name='Bind',value=f"Press {configDict[_E]} to stop the spam!");C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction("✅");await asyncio.sleep(configDict[_A]);await A.delete()
                        except:alert("This server does not allow embeds. \nStarting tts spam in 3 seconds... \nPress {} to stop the spamming.").format(configDict[_E]);await asyncio.sleep(configDict[_A])
                        for _XM in range(D):
                                while True:
                                        if keyboard.is_pressed(configDict[_E]):
                                                break
                                await ctx.send(message, tts=True)
                else:
                        alert("This server does not allow embeds. \nStarting tts spam in 3 seconds... \nPress {} to stop the spamming.").format(configDict[_E]);await asyncio.sleep(configDict[_A])
                        for _XM in range(D):
                                while True:
                                        if keyboard.is_pressed(configDict[_E]):
                                                break
                                await ctx.send(message, tts=True)            

@Z3RO.command(name="happy thoughts")
async def HT(ctx):
    happy_list = ['Don\'t be sad, you have so much to do!', 'Don\'t forget your goals. Focus on those instead of being sad!', 'You know, God put you on this earth for a reason. Don\'t waste any time sulking around.']
    happyThought = random.choice(happy_list);happy_ThoughtMSG = await ctx.send(happyThought);happy_ThoughtMSG.add_reaction("👍")

@Z3RO.command()
async def numbers(ctx, channel : int):
        alert("Sending in 3 seconds.")
        await asyncio.sleep(3)

        channel = await Z3RO.fetch_channel(channel)
        await asyncio.sleep(1)
        count = 11617
        for i in range(100):
                count += 1
                await channel.send(count)
                await asyncio.sleep(2)
@Z3RO.command()
async def massadvert(ctx, *, message=None):
        await ctx.message.delete()
        if (message == None):
                if embeds:
                        try:
                                embed = discord.Embed(title="Error", description="Message argument returns : null", color=10038562)
                                embed.add_field(name="Reason:", value="You must give a message to mass advert.")
                                message = await ctx.send(embed=embed)
                                await asyncio.sleep(1.5)
                                await message.delete()
                                
                        except:
                                alert("Server does not allow embeds. \nYou must give a message to mass advert.")
                else:
                        alert("You must give a message to mass advert.")
        else:
                alert("Mass dming everyone in server this message: {}".format(message))
                members = ctx.guild.members
                for user in members:
                        try:
                                await user.send(message)
                        except:
                                print("rip")
@Z3RO.command()
async def gcspam(ctx, *, name : str=None):
        if isinstance(ctx.message.channel, discord.GroupChannel):
                if (name == None):
                        if embeds:
                                await ctx.message.delete()
                                C=discord.Embed(title=_H,description='Name Argument returns : null',color=10038562)
                                C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)')
                                await ctx.send(embed=C)
                        else:
                                alert("Name argument returns : null")
                else:
                        wt = ''
                        for x in name:
                                nm = x + name
                                await ctx.message.channel.edit(name=nm)
        else:
                if embeds:
                                await ctx.message.delete()
                                C=discord.Embed(title=_H,description='You must be in a group chat channel.',color=10038562)
                                C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)')
                                await ctx.send(embed=C)
                else:
                        alert("You must be in a group chat channel.")


@Z3RO.command()
async def pingsite(ctx, site : str=None):
        mh = "https://"
        if (site == None):
                if embeds:

                        await ctx.message.delete()
                        C=discord.Embed(title=_H,description='\"https://\" must be in your site, so we can ping it.',color=10038562)
                        C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)')
                        await ctx.send(embed=C)       
                else:
                        alert("'https://' must be in your site, so we can ping it.")
        if (site[0] == mh[0]) and (site[1] == mh[1]) and (site[2] == mh[2]) and (site[3] == mh[3]) and (site[4] == mh[4]) and (site[5] == mh[5]) and (site[6] == mh[6]) and (site[7] == mh[7]):
                alert("Pinging site ({}) and sending status code in current channel.".format(site))
                r = requests.get(site)
                if r.status_code == 200:
                        message = await ctx.send("{0} status code: {1} (OK)".format(site, r.status_code))
                elif r.status_code == 400:
                        message = await ctx.send("{0} status code: {1} (BAD)".format(site, r.status_code))
                
        else:
                if embeds:

                        await ctx.message.delete()
                        C=discord.Embed(title=_H,description='\"https://\" must be in your site, so we can ping it.',color=10038562)
                        C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)')
                        await ctx.send(embed=C)       
                else:
                        alert("'https://' must be in your site, so we can ping it.")


@Z3RO.command()
async def namegen(ctx):
        with open("usernames.json") as f:
                v = json.load(f)
                if embeds:
                        embed = discord.Embed(title="Username", description="Generated username: {}".format(random.choice(v)), color=10038562)
                        await ctx.send(embed=embed)
                else:
                        await ctx.send("Generated username: {}".format(random.choice(v)))
@Z3RO.command()
async def passwordgen(ctx, length: int=None):
        if (length == None):
                if embeds:
                        embed = discord.Embed(title="Password", description="Generated password: {}".format(''.join(random.choice(string.ascii_lowercase) for x in range(random.randint(5, 15)))), color=10038562)
                        await ctx.send(embed=embed)
        else:
                password = await ctx.send('Generated password: {}'.format(''.join(random.choice(string.ascii_lowercase) for x in range(length))))

@Z3RO.command()
async def spammer(ctx):
        await ctx.message.delete()
        alert("Go to the terminal for the rest of the command.")
        tokens = []

        am = int(input("Enter the amount of tokens you have/want to use."))
        amn = am + 1
        for y in range(1, amn):
                token = str(input("Token {}: ".format(y)))
                tokens.append(token)

        qu = int(input("Do you want to join a specific server? \n1: Yes \n2: No"))
        if (qu == 1):
                invite = input("Enter server invite : ")

                def join():
                        global auth
                        for auth in tokens:
                                header = {
                                        'authorization': auth
                                }

                                requests.post("https://discord.com/api/v8/invites/{}".format(invite), headers=header)
                                print("Successfully server with {}".format(auth))

                join()
                print("Enter message: ")
                message = input()
                print("Enter channel ID")
                chanID = input()
                payload = {
                        'content': message
                }

                while True:
                        t = random.choice(tokens)

                        header = {
                                'authorization': t
                        }
                        url = 'https://discord.com/api/v8/channels/{}/messages'.format(chanID)
                        requests.post(url, headers=header, data=payload)

        else:
                print("Enter message: ")
                message = input()
                print("Enter channel ID")
                chanID = input()
                payload = {
                        'content': message
                }
                while True:
                        t = random.choice(tokens);
                        header = {"authorization": t}
                        header = {
                                'authorization': t
                        }
                        url = 'https://discord.com/api/v8/channels/{}/messages'.format(chanID)
                        requests.post(url, headers=header, data=payload)
@Z3RO.command()
async def viewbot(ctx):
        await ctx.message.delete()
        alert("Go to the terminal for the rest of the command.")
        url = str(input("Enter your url \n"))
        views = int(
                input("Enter your view amount \nAnything over 50 will take longer to register, \nas YouTube will catch on. \n"))
        watchTime = int(
                input("Enter the amount of seconds you want the bot to watch your video for. \nAnything below 30 will be detected by YouTube and your video views will take longer to register \nor completely take a pause for a few hours. \n60 is good for a minimum of 100 views."))

        def viewBot():
                driver.get(url)
                print("Loading video...")

                for view in range(views):
                        time.sleep(watchTime)
                        print("[!] View added.")
                        driver.refresh()
                        print("[-]Page refreshed")

        viewBot()


@Z3RO.command()
async def note(ctx, user : discord.Member=None, note : str=None):
        if (user == None):
                if embeds:
                        embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description="User argument is missing! Please use it next time.", color=0x02f2c2)
                        embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_footer(text="this self bot was made zemult!")
                        await ctx.send(embed=embed)
                else:
                        alert("User argument is missing! Please use it next time.")
        elif (note == None):
                if embeds:
                        embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description="In order to use the note command, you need to add a note as part of the command; silly!", color=0x02f2c2)
                        embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_footer(text="this self bot was made zemult!")
                        await ctx.send(embed=embed)
                else:
                        alert("In order to use the note command, you need to add a note as part of the command; silly!")
        else:
                if embeds:
                        embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description=f"I have successfully add a note to {user}!", color=0x02f2c2)
                        embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_footer(text="this self bot was made zemult!")
                        await ctx.send(embed=embed)
                        noted.append(f"{user}'s note: {note}")
                else:
                        noted.append(f"{user}'s note: {note}")
                        alert(f"I have successfully add a note to {user}!")

@Z3RO.command()
async def notes(ctx):
        if embeds:
                embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description="Here are your notes: {}".format(str(noted)), color=0x02f2c2)
                embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                embed.set_footer(text="this self bot was made zemult!")
                await ctx.send(embed=embed)
        else:
                await ctx.send(str(noted))

@Z3RO.command()
async def hentai(ctx):
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        res = r.json()
        em = discord.Embed(title="Z3RO", url="https://zemult.github.io", description="Enjoy your hentai ;)")
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
@Z3RO.command()
async def anime(ctx):
        
        search_term = "anime"

        r = requests.get(
        "https://g.tenor.com/v1/search?q={}&key={}&limit={}".format(search_term, api_key, lmt))
        if r.status_code == 200:
                res = r.json()
                await ctx.send(url=res['url'])

@Z3RO.command()
async def followforfollow(ctx, followAmount : int=None):

        if (followAmount == None):
                if embeds:
                        embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description="You must enter the amount of people you want to follow, silly!", color=0x02f2c2)
                        embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_footer(text="this self bot was made zemult!")
                        await ctx.send(embed=embed)
                else:
                        alert("You must enter the amount of people you want to follow, silly!")
        else:
                if embeds:
                        embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description="Sending follows to {} people.".format(followAmount), color=0x02f2c2)
                        embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_footer(text="this self bot was made zemult!")
                        await ctx.send(embed=embed)
                else:
                        alert("Sending follows to {} people.".format(followAmount))
                with open("instagram_config.json") as f:
                        uxp = json.load(f)
                driver = webdriver.Chrome("./chromedriver")
                driver.get("https://www.instagram.com/explore/people/suggested/")
                time.sleep(3)
                usernameInput = driver.find_element_by_name("username")
                usernameInput.send_keys(uxp.get("email/username"))
                passwordInput = driver.find_element_by_name("password")
                passwordInput.send_keys(uxp.get("password"))
                loginButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]").click()
                time.sleep(10)
                try:
                        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
                except:
                        pass
                for x in range(followAmount):
                        try:
                                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div[{}]/div[3]/button".format(x)).click()
                        except:
                                print("unable")
                                        
                        driver.refresh()
                
                        embed=discord.Embed(title="Z3RO", url="https://zemult.github.io", description="Successfully sent follows to {} people.".format(followAmount), color=0x02f2c2)
                        embed.set_author(name="Made by: zemult", url="https://youtube.com/zemult", icon_url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_thumbnail(url="https://media.discordapp.net/attachments/819917872469639208/837052412798697523/unknown.png")
                        embed.set_footer(text="this self bot was made zemult!")
                        await ctx.send(embed=embed)
Z3RO.run(configDict[_K],bot=False)
