import concurrent.futures
import discord
import keyboard
import pydirectinput
import pyautogui
import os
from dotenv import load_dotenv
from DiscordPlaysKeyCodes import *

# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Declare intents to be able to see messages
intents = discord.Intents.default()
intents.messages = True  # Enable message-related intents
intents.guild_messages = True  # Enable message-related intents
intents.message_content = True  # Enable message-reading

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.event
async def on_message(message):
    if message.author == bot.user:  # To prevent the bot from responding to itself
        return
    if message.content == "ping":
        HoldAndReleaseKey(A, 0.5)
        await message.channel.send("pong")


# Run the bot with your Discord bot token
bot.run(DISCORD_TOKEN)
