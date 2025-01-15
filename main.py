# halted omnia...

import discord
from discord.ext import commands
from discord.utils import get

from config import get_config

config = get_config()

SERVER_ID = config['botInfo']['serverId']
TOKEN = config['botInfo']['botToken']
CHANNEL_ID = config['botInfo']['channelId']
ROLE_TO_GIVE_ID = config['botInfo']['roleToGiveId']
ROLE_TO_REMOVE_ID = config['botInfo']['roleToRemoveId']

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    guild = bot.get_guild(SERVER_ID)
    print("passing guild")
    if str(message.channel.id) == str(CHANNEL_ID):
        role_to_give = guild.get_role(ROLE_TO_GIVE_ID)
        role_to_remove = guild.get_role(ROLE_TO_REMOVE_ID)
        if role_to_give not in message.author.roles:
            if role_to_remove in message.author.roles:
                await message.author.remove_roles(role_to_remove)
            await message.author.add_roles(role_to_give)
            await message.channel.send(f'{message.author.mention}, you have been given the role {role_to_give.name}!')
        else:
            await message.channel.send(f'{message.author.mention}, you already have the role {role_to_give.name}!')

bot.run(TOKEN)
