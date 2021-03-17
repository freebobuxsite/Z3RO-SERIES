


_T='none'
_S='Whitelist Argument returns : null'
_R='Status code: 200'
_Q='Thank you for using Z3RO self bot!'
_P='stop bind'
_O='no file tree/selfbot_config.json'
_N='Reason'
_M=True
_L='prefix'
_K='token'
_J='{0}Member {1} failed to be removed from the server'
_I='You must give a white listed user, or give the keyword "none" to show you don\'t want to use whitelist.'
_H='Z3RO RAID TOOL'
_G='Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)'
_F='start bind'
_E='stop_bind'
_D='Z3RO SB'
_C=None
_B='âœ…'
_A='sleep_delete'
import discord,json,asyncio,keyboard,pyautogui,colorama,dhooks
from dhooks import Webhook,Embed
from pyautogui import alert
from discord.ext import commands
from colorama import Fore,Back,Style
with open(_O)as f:config=json.load(f)
configDict={_K:config.get(_K),_L:config.get(_L),_E:config.get(_P),_A:config.get('sleep delete'),'bot_reaction':config.get('bot reaction'),_F:config.get(_F)}
Z3RO=commands.Bot(description='Z3RO Self bot',command_prefix=configDict[_L],self_bot=_M)
@Z3RO.event
async def on_ready():alert(text=_Q);print(_R);print(f'{Fore.GREEN}Bot Online - developer: \ndiscord: zemult#0001 \nyoutube: zemult')
@Z3RO.command()
async def about(ctx):
        B=ctx
        try:await B.message.delete();C=discord.Embed(title=_D,description='Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001',color=10038562);A=await B.send(embed=C);await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
        except:await B.message.delete();A=await B.send(f"**ZERO SB** \n**Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001");await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete();await A.delete()
@Z3RO.command()
async def spam(ctx,amount=_C,*,msg=_C):
        E=msg;D=amount;B=ctx
        if D is _C:await B.message.delete();C=discord.Embed(title=_D,description='Spam Amount returns : null',color=10038562);C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
        elif E is _C:await B.message.delete();C=discord.Embed(title=_D,description='Message Arguement returns : null',color=10038562);C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
        else:
                try:
                        await B.message.delete();C=discord.Embed(title='ZERO SB',description='Successful command. Spamming is 3 seconds...',color=10038562);C.add_field(name='Bind',value=f"Press {configDict[_E]} to stop the spam!");C.set_footer(text=_G);A=await B.send(embed=C);await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
                        for F in range(D):
                                await B.send(E)
                                if keyboard.is_pressed(configDict[_E]):break
                except:
                        A=await B.send(f"**ZERO SB** \nSpamming in 3 seconds... \n**Bind:**\n**Press {configDict[_E]} to stop spamming.&**");await asyncio.sleep(configDict[_A]);await A.delete()
                        for F in range(D):
                                await B.send(E);await asyncio.sleep(0.5)
                                if keyboard.is_pressed(configDict[_E]):break
@Z3RO.command()
async def massreact(ctx,reactionID=_C):
        D=reactionID;B=ctx
        if D==_C:
                try:C=discord.Embed(title=_D,description='Reaction ID returns : null',color=10038562);C.add_field(name=_N,value='You must give a reaction value.');C.set_footer(text=_G);A=await B.send(embed=C);await asyncio.sleep(configDict[_A]);await A.add_reaction(_B)
                except:await B.message.delete();A=await B.send(f"**Z3RO SB \n**Reactions return : null** \n**Reason:** \n**You must give a reaction value.**");await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
        else:
                try:C=discord.Embed(title=_D,description='Starting react spam in 3 seconds....');A=await B.send(embed=C);await A.add_reaction(_B);await asyncio.sleep([configDict[_A]]);await A.delete()
                except:await B.message.delete();A=await B.send(f"**Z3RO SB** \n**Starting react spam in 3 seconds...**");await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
                E=await B.message.channel.history(limit=20).flatten()
                for F in E:await F.add_reaction(D)
@Z3RO.command()
async def quickdel(ctx):
        A=ctx;D=discord.Embed(title=_D,description=f"Press {configDict[_F]} to start quick del and {configDict[_E]} to pause quick del");B=await A.send(embed=D);await B.add_reaction(_B);await asyncio.sleep(configDict[_A]);await B.delete()
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
async def on_ready():alert(text=_Q);print(_R);print('Bot Online - developer: \ndiscord: zemult \nyoutube: zemult')
@Z3RO.command()
async def mcs(ctx,channelName=_C,channelAmount=_C):
        G='**Z3RO RAID TOOL** \n**Channel Amount Argument returns : null** \n**Reason: ** \n**You must give a channel amount.**';F='Z3RO RAID TOOL was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)';E=channelAmount;D=channelName;B=ctx
        if D==_C:
                try:await B.message.delete();C=discord.Embed(title=_H,description='Channel Name Argument returns : null',color=10038562);C.set_footer(text='Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)');A=await B.send(embed=C);await A.add_reaciton(_B);await asyncio.sleep(configDict[_A]);await A.delete()
                except:await B.message.delete();A=await B.send('**Z3RO RAID TOOL** \n**Channel Name Argument returns : null** \n**Reason: ** \n**You must give a channel name.**');await asyncio.sleep(configDict[_A]);await A.add_reaction(_B);await A.delete()
        elif E==_C:
                try:await B.message.delete();C=discord.Embed(title=_H,description='Channel Amount Argument returns : null',color=10038562);C.set_footer(text=F);A=await B.send(embed=C);await A.add_reaciton(_B);await asyncio.sleep(configDict[_A]);await A.delete()
                except:await B.message.delete();A=await B.message.send(G);await A.add_reaciton(_B);await asyncio.sleep(configDict[_A])
        else:
                try:
                        await B.message.delete();C=discord.Embed(title=_H,description='Spamming channels in 3 seconds...',color=10038562);C.set_footer(text=F);A=await B.send(embed=C);await A.add_reaction(_B);await asyncio.sleep(configDict[_A]);await A.delete()
                        for H in range(E):
                                await B.guild.create_text_channel(D)
                                if keyboard.is_pressed(configDict[_P]):break
                except:await B.message.delete();A=await B.send(G);await A.add_reaction(_B);await asyncio.sleep(configDict[_A])
@Z3RO.command()
async def mscd(ctx):
        F='Channel {} successfully deleted';E='Destroying all channels in 3 seconds...';A=ctx
        try:
                D=discord.Embed(title=_H,description=E,color=10038562);B=await A.send(embed=D);await B.add_reaction(_B);await asyncio.sleep(3);await B.delete()
                for C in list(A.guild.channels):await C.delete();print(F.format(C.id))
        except:
                await A.message.delete();B=await A.send('**Z3RO RAID TOOL',description=E);await B.add_reaction(_B);await asyncio.sleep(3);await B.delete()
                for C in list(A.guild.channels):await C.delete();print(F.format(C.id))
@Z3RO.command()
async def massban(ctx,whitelist):
        I='{0}Member {1} was successfully banned.';F='Starting mass ban in 3 seconds...';E=whitelist;B=ctx;G=list(B.guild.members)
        if E==_C:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=_S,color=10038562);D.add_field(name=_N,text=_I);C=await B.send(embed=D);await C.add_reaction(_B);await asyncio.sleep(configDict[_A])
                except:alert(text=_I)
        elif E.strip().lower()==_T:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=F,color=10038562);C=await B.send(embed=D);await C.add_reaction(_B);await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=F)
                for A in G:
                        try:await A.ban();print(I.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
        else:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=F,color=10038562);C=await B.send(embed=D);await C.add_reaction(_B);await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=F)
                for A in G:
                        try:
                                H=await Z3RO.fetch_user(E)
                                if H==A:print('{0}Member {1} was not banned because he/she was whitelisted.'.format(Fore.RED,A.id))
                                else:await A.ban();print(I.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
@Z3RO.command()
async def masskick(ctx,*,whitelist):
        F='Starting mass kick in 3 seconds...';E=whitelist;B=ctx;G=list(B.guild.members)
        if E==_C:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=_S,color=10038562);D.add_field(name=_N,text=_I);C=await B.send(embed=D);await C.add_reaction(_B);await asyncio.sleep(configDict[_A])
                except:alert(text=_I)
        elif E.strip().lower()==_T:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=F,color=10038562);C=await B.send(embed=D);await C.add_reaction(_B);await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=F)
                for A in G:
                        try:await A.kick();print('{0}Member {1} was successfully kick.'.format(Fore.GREEN,A.id))
                        except:print(_J.format(Fore.RED,A.id))
        else:
                await B.message.delete()
                try:D=discord.Embed(title=_D,description=F,color=10038562);C=await B.send(embed=D);await C.add_reaction(_B);await asyncio.sleep(configDict[_A]);await C.delete()
                except:alert(text=F)
                for A in G:
                        try:
                                H=await Z3RO.fetch_user(E)
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
                
Z3RO.run(configDict[_K],bot=False)
