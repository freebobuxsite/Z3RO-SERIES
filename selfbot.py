"""
open source
currently in development
"""

import discord, json, asyncio, keyboard, pyautogui
from pyautogui import alert
from discord.ext import commands

with open('./config.json') as f:
    config = json.load(f)

configDict = {
    'token':  config.get("token"),
    'prefix':  config.get("prefix"),
    'stop_bind':  config.get("stop bind"),
    'sleep_delete':  config.get("sleep delete"),
    'bot_reaction':  config.get("bot reaction")
}


bot = commands.Bot(description="Z3RO Self bot", command_prefix=configDict['prefix'], self_bot=True)



@bot.event
async def on_ready():
    alert(text="Thank you for using Z3RO self bot!")
    print("Status code: 200")
    print("Bot Online - developer: \ndiscord: zemult#0001 \nyoutube: zemult")

@bot.command()
async def about(ctx):
    try:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001", color=0x992d22)
        message = await ctx.send(embed=embed)
        await message.add_reaction(configDict['bot_reaction'])
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
    except:
        await ctx.message.delete()
        message = await ctx.send(f"**ZERO SB** \n**Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001")
        await message.add_reaction(configDict['bot_reaction'])
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
        await message.delete()
        

@bot.command()
async def spam(ctx, amount : int=None, *, msg : str=None):
    if amount is None:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Spam Amount returns : null", color=0x992d22)
        embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
        message = await ctx.send(embed=embed)
        await message.add_reaction(configDict['bot_reaction'])
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
    elif msg is None:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Message Arguement returns : null", color=0x992d22)
        embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
        message = await ctx.send(embed=embed)
        await message.add_reaction(configDict['bot_reaction'])
        await asyncio.sleep(configDict['sleep_delete'])
        await message.delete()
    else:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="ZERO SB", description="Successful command. Spamming is 3 seconds...", color=0x992d22)
            embed.add_field(name="Bind", value=f"Press {configDict['stop_bind']} to stop the spam!")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embed)
            await message.add_reaction(config["bot_reaction"])
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
                if keyboard.is_pressed(configDict['stop_bind']):
                    break        
@bot.command()
async def massReaction(ctx, msgid : int=None, msgAmount: int=None, reaction=None):
    if msgid == None:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="Z3RO SB", description="ID Arguement returns : null", color=0x992d22)
            embed.add_field(name="Reason", value="You must give the ID of the message you want to react to.")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction(config["bot_reaction"])
            await message.delete()
        except:
            await ctx.message.delete()
            message = await ctx.send(f"**Z3RO SB \n**ID Arguement returns : null** \n**Reason:** \n*You must give the ID of the message you want to react to.*")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction(config["bot_reaction"])
            await message.delete()
    elif msgAmount == None:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="ZERO SB", description="Message Amount Argument returns : null", color=0x992d22)
            embed.add_field(name="Reason", value='You must give the amount of messages you want to add reactions to.')
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction(config["bot_reaction"])
            await message.delete()
            
        except:
            await ctx.message.delete()
            message = await ctx.send(f"**ZERO SB**\n**Message Amount Argument returns : null**\n**Reason:** \n**You must give the same amount of messages specified in your message amount.**")
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction(config["bot_reaction"])
            await message.delete()
    elif reaction == None:
        try:
            embed = discord.Embed(title="Z3RO SB", description="Reactions return : null", color=0x992d22)
            embed.add_field(name="Reason", value="You must give a reaction value.")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(configDict['sleep_delete'])
            await message.add_reaction
        except:
            return None

bot.run(configDict['token'], bot=False)
