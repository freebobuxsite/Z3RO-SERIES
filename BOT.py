import discord, json, asyncio, keyboard, pyautogui, colorama, dhooks
from dhooks import Webhook, Embed
from pyautogui import alert
from discord.ext import commands
from colorama import Fore, Back, Style


with open('no file tree/selfbot_config.json') as f:
    config = json.load(f)

configDict = {
    'token':  config.get("token"),
    'prefix':  config.get("prefix"),
    'stop_bind':  config.get("stop bind"),
    'sleep_delete':  config.get("sleep delete"),
    'bot_reaction':  config.get("bot reaction"),
    'start bind': config.get("start bind")
}


Z3RO = commands.Bot(description="Z3RO Self bot", command_prefix=configDict['prefix'], self_bot=True)



@Z3RO.event
async def on_ready():
    alert(text="Thank you for using Z3RO self bot!")
    print("Status code: 200")
    print("Bot Online - developer: \ndiscord: zemult#0001 \nyoutube: zemult")

@Z3RO.command()
async def about(ctx):
    try:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001", color=0x992d22)
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
    except:
        await ctx.message.delete()
        message = await ctx.send(f"**ZERO SB** \n**Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001")
        await message.add_reaction("✅")
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
        await message.delete()
        

@Z3RO.command()
async def spam(ctx, amount : int=None, *, msg : str=None):
    if amount is None:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Spam Amount returns : null", color=0x992d22)
        embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
    elif msg is None:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Message Arguement returns : null", color=0x992d22)
        embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
    else:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="ZERO SB", description="Successful command. Spamming is 3 seconds...", color=0x992d22)
            embed.add_field(name="Bind", value=f"Press {configDict['stop_bind']} to stop the spam!")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embed)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            for i in range(amount):
                await ctx.send(msg)
                if keyboard.is_pressed(configDict['stop_bind']):
                    break
        except:
            message = await ctx.send(f"**ZERO SB** \nSpamming in 3 seconds... \n**Bind:**\n**Press {configDict['stop_bind']} to stop spamming.&**")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            for i in range(amount):
                await ctx.send(msg)
                await asyncio.sleep(0.5)
                if keyboard.is_pressed(configDict['stop_bind']):
                    break        
@Z3RO.command()
async def massreact(ctx, reactionID=None):
    if reactionID == None:
        try:
            embed = discord.Embed(title="Z3RO SB", description="Reaction ID returns : null", color=0x992d22)
            embed.add_field(name="Reason", value="You must give a reaction value.")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction("✅")
        except:
            await ctx.message.delete()
            message = await ctx.send(f"**Z3RO SB \n**Reactions return : null** \n**Reason:** \n**You must give a reaction value.**")
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
    else:
        try:
            
            embed = discord.Embed(title="Z3RO SB", description="Starting react spam in 3 seconds....")
            message = await ctx.send(embed=embed)
            await message.add_reaction("✅")
            await asyncio.sleep([configDict['sleep_delete']])
            await message.delete()
        except:
            await ctx.message.delete()
            message = await ctx.send(f"**Z3RO SB** \n**Starting react spam in 3 seconds...**")
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            
        messages = await ctx.message.channel.history(limit=20).flatten()
        for mesisage in messages:
            await mesisage.add_reaction(reactionID)

                
        
@Z3RO.command()
async def quickdel(ctx):
    embed = discord.Embed(title="Z3RO SB", description=f"Press {configDict['start bind']} to start quick del and {configDict['stop_bind']} to pause quick del")
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await asyncio.sleep(configDict['sleep_delete'])
    await message.delete()
    
    while True:
        if keyboard.is_pressed(configDict['start bind']):
            while True:
                messages = await ctx.message.channel.history(limit=20).flatten()
                for i in messages:
                    if i.author == ctx.message.author:
                        
                        await i.delete()
                
                if keyboard.is_pressed(configDict['stop_bind']):
                    break

import discord, pyautogui, json, asyncio, keyboard
from pyautogui import alert
from discord.ext import commands

with open("no file tree/selfbot_config.json") as f:
    config = json.load(f)
    
count = 0

@Z3RO.event
async def on_ready():
    alert(text="Thank you for using Z3RO self bot!")
    print("Status code: 200")
    print("Bot Online - developer: \ndiscord: zemult \nyoutube: zemult")
    
@Z3RO.command()
async def mcs(ctx, channelName : str=None, channelAmount : int=None):
    if channelName == None:
        try:
            await ctx.message.delete()
            embedVar = discord.Embed(title="Z3RO RAID TOOL", description="Channel Name Argument returns : null", color=0x992d22)
            embedVar.set_footer(text="Z3RO RAID TOOL was programmed by zemult, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embedVar)
            await message.add_reaciton("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
        except:
            await ctx.message.delete()
            message = await ctx.send("**Z3RO RAID TOOL** \n**Channel Name Argument returns : null** \n**Reason: ** \n**You must give a channel name.**")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction("✅")
            await message.delete()
            
    elif channelAmount == None:
        try:
            await ctx.message.delete()
            embedVar = discord.Embed(title="Z3RO RAID TOOL", description="Channel Amount Argument returns : null", color=0x992d22)
            embedVar.set_footer(text="Z3RO RAID TOOL was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embedVar)
            await message.add_reaciton("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
        except:
            await ctx.message.delete()
            message = await ctx.message.send('**Z3RO RAID TOOL** \n**Channel Amount Argument returns : null** \n**Reason: ** \n**You must give a channel amount.**')
            await message.add_reaciton("✅")
            await asyncio.sleep(configDict['sleep_delete'])
    else:
        try:
            await ctx.message.delete()
            embedVar = discord.Embed(title="Z3RO RAID TOOL", description="Spamming channels in 3 seconds...", color=0x992d22)
            embedVar.set_footer(text="Z3RO RAID TOOL was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embedVar)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            for i in range(channelAmount):
                await ctx.guild.create_text_channel(channelName)
                if keyboard.is_pressed(configDict['stop bind']):
                    break
            
        except:
            await ctx.message.delete()
            message = await ctx.send('**Z3RO RAID TOOL** \n**Channel Amount Argument returns : null** \n**Reason: ** \n**You must give a channel amount.**')
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])

@Z3RO.command()
async def mscd(ctx):
    try:
        embed = discord.Embed(title="Z3RO RAID TOOL", description="Destroying all channels in 3 seconds...", color=0x992d22)
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await asyncio.sleep(3)
        await message.delete()
        for i in list(ctx.guild.channels):
            await i.delete()
            print("Channel {} successfully deleted".format(i.id))
        
    except:
        await ctx.message.delete()
        message = await ctx.send("**Z3RO RAID TOOL", description="Destroying all channels in 3 seconds...")
        await message.add_reaction("✅")
        await asyncio.sleep(3)
        await message.delete()
        for i in list(ctx.guild.channels):
            await i.delete()
            print("Channel {} successfully deleted".format(i.id))
@Z3RO.command()
async def massban(ctx, whitelist):
    users = list(ctx.guild.members)
    if whitelist == None:
        await ctx.message.delete()
        try:
            em = discord.Embed(title="Z3RO SB", description="Whitelist Argument returns : null", color=0x992d22)
            em.add_field(name="Reason", text="You must give a white listed user, or give the keyword \"none\" to show you don't want to use whitelist.")
            message = await ctx.send(embed=em)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
        except:
            alert(text="You must give a white listed user, or give the keyword \"none\" to show you don't want to use whitelist.")
    elif whitelist.strip().lower() == "none": 
        await ctx.message.delete()    
        try:
            em = discord.Embed(title="Z3RO SB", description="Starting mass ban in 3 seconds...", color=0x992d22)
            message = await ctx.send(embed=em)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            

        except:
            alert(text="Starting mass ban in 3 seconds...")
            
        for i in users:
            try:
                await i.ban()
                print("{0}Member {1} was successfully banned.".format(Fore.GREEN, i.id))
            except:
                print("{0}Member {1} failed to be removed from the server".format(Fore.RED, i.id))
    else:
        await ctx.message.delete()    
        try:
            em = discord.Embed(title="Z3RO SB", description="Starting mass ban in 3 seconds...", color=0x992d22)
            message = await ctx.send(embed=em)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            
        except:
            alert(text="Starting mass ban in 3 seconds...")
            
        for i in users:
            try:
                whitelsitedUser = await Z3RO.fetch_user(whitelist)
                if whitelsitedUser == i:
                    print("{0}Member {1} was not banned because he/she was whitelisted.".format(Fore.RED, i.id))
                else:
                    await i.ban()
                    print("{0}Member {1} was successfully banned.".format(Fore.GREEN, i.id))
            except:
                print("{0}Member {1} failed to be removed from the server".format(Fore.RED, i.id))

@Z3RO.command()
async def masskick(ctx, *, whitelist):
    users = list(ctx.guild.members)

    if whitelist == None:
        await ctx.message.delete()
        try:
            em = discord.Embed(title="Z3RO SB", description="Whitelist Argument returns : null", color=0x992d22)
            em.add_field(name="Reason", text="You must give a white listed user, or give the keyword \"none\" to show you don't want to use whitelist.")
            message = await ctx.send(embed=em)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
        except:
            alert(text="You must give a white listed user, or give the keyword \"none\" to show you don't want to use whitelist.")
    elif whitelist.strip().lower() == "none": 
        await ctx.message.delete()    
        try:
            em = discord.Embed(title="Z3RO SB", description="Starting mass kick in 3 seconds...", color=0x992d22)
            message = await ctx.send(embed=em)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            
        except:
            alert(text="Starting mass kick in 3 seconds...")
            
        for i in users:
            try:
                await i.kick()
                print("{0}Member {1} was successfully kick.".format(Fore.GREEN, i.id))
            except:
                print("{0}Member {1} failed to be removed from the server".format(Fore.RED, i.id))
    else:
        await ctx.message.delete()    
        try:
            em = discord.Embed(title="Z3RO SB", description="Starting mass kick in 3 seconds...", color=0x992d22)
            message = await ctx.send(embed=em)
            await message.add_reaction("✅")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()
            
        except:
            alert(text="Starting mass kick in 3 seconds...")
            
        for i in users:
            try:
                whitelsitedUser = await Z3RO.fetch_user(whitelist)
                if whitelsitedUser == i:
                    print("{0}Member {1} was not kicked because he/she was whitelisted.".format(Fore.RED, i.id))
                else:
                    await i.kick()
                    print("{0}Member {1} was successfully kicked.".format(Fore.GREEN, i.id))
            except:
                print("{0}Member {1} failed to be removed from the server".format(Fore.RED, i.id))

@Z3RO.command()
async def inftype(ctx, time : int=None):
    await ctx.message.delete()
    if time == None:
        alert("You must give a time amount. (in seconds)")
    else:
        async with ctx.typing():
            await asyncio.sleep(time)
        message = await ctx.send("done typing lmao")
        await asyncio.sleep(.5)
        await message.delete()



Z3RO.run(configDict['token'], bot=False)
