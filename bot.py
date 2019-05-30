import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio

bot = commands.Bot(command_prefix='#')	#change the prefix silly if you want to use commands

@bot.event
async def on_ready():
    print ("I am ready PogChamp")										#change this to whatever you want your bot to say, helps confirm your bot is running as well

custom_emojis = [										#no longer need the ID for emojis YAY!
    "check",									#make sure you add that ',' if you want more than one emoji // order of appearance is descending	
	"cross"									#obvioulsy change custom_emoji to whatever the name of your emoji is on your server
]

async def react(message):								#however we do need to call those emojis from the server... i mean guild
    for emoji in message.guild.emojis:
        if emoji.name in custom_emojis:
            await message.add_reaction(emoji)

@bot.event												
async def on_message(message):
    if message.channel.id == 583379986811977746 or message.channel.id == 583380237493207073:			#change this as well my dude
        await react(message)
		
		
bot.run("NTgzNTc3MzkzNzcyNjI1OTQz.XO-Y_g.Nl7lRPq_UCli2CKAc9MX22wxwwc")									#hope you kept this somwhere safe >>