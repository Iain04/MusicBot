import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

# Import cogs
from help_cog import help_cog
from music_cog import music_cog

# Load environment variables from .env file
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Define the intents your bot will use
intents = discord.Intents.default()
intents.voice_states = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Remove the default help command so that we can write our own
bot.remove_command('help')

# Define an asynchronous function to register the cogs with the bot
async def register_cogs():
    await bot.wait_until_ready() # Wait until the bot is ready
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

# Feedback on ready
# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    asyncio.ensure_future(register_cogs()) # Schedule register_cogs() as a future

# Start the bot with our token
bot.run(DISCORD_BOT_TOKEN)
