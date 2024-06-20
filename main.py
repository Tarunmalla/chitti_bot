import os
import discord
from discord import message
from discord import client
from discord.ext import commands
from discord.flags import Intents
from codeforces.ratings import get_handle_info
from leetcode.prob_count  import user_info
from dotenv import load_dotenv

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
    await msg.send(f'Yes {msg.author} , Chitti is here to server you. use !help to know more about me..')


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
async def ratings(msg,handle_name):
    """
    to get user ratings in the codeforces
    """
    await msg.send(get_handle_info(handle_name))

@bot.command()
async def leetcode(msg,handle):
    """
    to get leetcode stats 
    """
    await msg.send(user_info(handle))

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
