import os
import discord
from discord import message
from discord import client
from discord.ext import commands
from discord.flags import Intents
from codeforces.ratings import handle_ratings
from leetcode.prob_count  import user_info
from dotenv import load_dotenv
from ext.handles import add_cf_handle,add_leetcode_handle


# Intents are required for receiving certain events
intents = discord.Intents.default()
intents.message_content = True

# Create a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def chitti(msg):
    await msg.send(f'Yes {msg.author} , Chitti is here to server you. use !help to know more about me.. ')


@bot.command()
async def math(msg,arg):
    """
    for doing basic math operations
    """
    await msg.send(f'result: {eval(arg)}')

@bot.command()
async def activate(msg):
    """
    for announcements
    """
    await msg.send("@everyone important notice!!")
# Run the bot

@bot.command()
async def ratings(msg):
    """
    to get user ratings in the codeforces
    """
    if msg.channel.name == 'contest-ratings':
        await msg.send(handle_ratings())
    else:
        await msg.send("Please follow the ruless... Don't disturb me!")


@bot.command()
async def leetcode(msg):
    """
    to get leetcode stats 
    """
    if msg.channel.name == 'contest-ratings':
        embedVar = discord.Embed(title="Leetcode stats", description=user_info(), color=0x00ff00)
        await msg.send(embed=embedVar)
    else:
        await msg.send("Please follow the ruless... Don't disturb me!")


@bot.command()
async def sethandle(msg,handle):
    """
    to add handle to the database
    """
    if msg.channel.name == "set-handle":
        req = add_cf_handle(msg.author.name,handle)
        await msg.send(req)
    else:
        await msg.send("Please follow the ruless... Don't disturb me!")

@bot.command()
async def setleetcode(msg,handle):
    """
    to add handle to the database
    """
    if msg.channel.name == "set-handle":
        req = add_leetcode_handle(msg.author.name,handle)
        await msg.send(req)
    else:
        await msg.send("Please follow the ruless... Don't disturb me!")


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
