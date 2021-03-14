import discord, pyautogui, json, asyncio
from pyautogui import alert
from discord.ext import commands

with open("selfbot_config.json") as f:
    config = json.load(f)
    
count = 0


configDict = {
    'token': config.get("token"),
    'prefix':  config.get("prefix"),
    'sleep_delete':  config.get("sleep delete"),
    'bot_reaction':  config.get("bot reaction")
}

raidtool = commands.Bot(command_prefix=configDict['prefix'], description="Z3RO raid tool", self_bot=True)

@raidtool.event
async def on_ready():
    alert(text="Thank you for using Z3RO self bot!")
    print("Status code: 200")
    print("Bot Online - developer: \ndiscord: zemult#0001 \nyoutube: zemult")
    
@raidtool.command()
async def mass_channel(ctx, channelName : str=None, channelAmount : int=None):
    if channelName == None:
        try:
            ctx.message.delete()
            embedVar = discord.Embed(title="Z3RO RAID TOOL", description="Channel Name Argument returns : null", color=0x992d22)
            embedVar.set_footer(text="Z3RO RAID TOOL was programmed by zemult#0001, donate him at https://paypal.me/mekhibatchler1 :)")
            message = await ctx.send(embed=embedVar)
            await message.add_reaciton(configDict['bot_reaction'])
            await asyncio.sleep(configDict['sleep_delete'])
            await message.delete()

raidtool.run(configDict['token'], bot=False)    
    
