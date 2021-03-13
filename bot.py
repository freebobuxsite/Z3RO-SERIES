# currently in development

import discord, json, asyncio, keyboard
from discord.ext import commands

with open('./config.json') as f:
    config = json.load(f)

token = config.get("token")
prefix = config.get("prefix")
stop_bind = config.get("stop_bind")
bot = commands.Bot(description="Z3RO Self bot", command_prefix="zero ", self_bot=True)
bot.remove_command('help')



@bot.event
async def on_ready():
    print("Status code: 200")
    print("Bot Online - developer: \ndiscord: zemult#0001 \nyoutube: zemult")

@bot.command()
async def about(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Z3RO SB", description="Z3RO Selfbot was developed by: \nyoutube: zemult \ndiscord: zemult#0001", color=0x992d22)
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await asyncio.sleep(2.5)
    await message.delete()
@bot.command()
async def spam(ctx, amount : int=None, *, msg : str=None):
    if amount is None:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Spam Amount returns : null", color=0x992d22)
        embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler :)")
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await asyncio.sleep(2.5)
        await message.delete()
    elif msg is None:
        await ctx.message.delete()
        embed = discord.Embed(title="Z3RO SB", description="Message Arguement returns : null", color=0x992d22)
        embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler :)")
        message = await ctx.send(embed=embed)
        await message.add_reaction("✅")
        await asyncio.sleep(2.5)
        await message.delete()
    else:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="ZERO SB", description="Successful command. Spamming is 3 seconds...", color=0x992d22)
            embed.add_field(name="Bind", value=f"Press {stop_bind} to stop the spam!")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler :)")
            message = await ctx.send(embed=embed)
            await message.add_reaction("✅")
            await asyncio.sleep(3)
            await message.delete()
            for i in range(amount):
                await ctx.send(msg)
                if keyboard.is_pressed(stop_bind):
                    break;
        except:
            message = await ctx.send(f"**ZERO SB** \nSpamming in 3 seconds... \n**Bind:**\n**Press {stop_bind} to stop spamming.&**")
            await asyncio.sleep(3)
            await message.delete()
            for i in range(amount):
                await ctx.send(msg)
                if keyboard.is_pressed(stop_bind):
                    break;
            
@bot.command()
async def spam_reaction(ctx, msgid : int=None, reactAmount: int=None, reaction=None):
    if msgid == None:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="Z3RO SB", description="ID Arguement returns : null", color=0x992d22)
            embed.add_field(name="Reason", value="You must give the ID of the message you want to react to.")
            embed.set_footer(text="Z3RO SB (self bot) was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler :)")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(2.5)
            await message.add_reaction("✅")
            await message.delete()
bot.run(token, bot=False)
