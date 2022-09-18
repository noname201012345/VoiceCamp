from discord.ext import commands
import discord
import os
import json

bot = commands.Bot("!", self_bot=True) # Defining bot.

guild=755793441287438469
channel=994552773637062656

@bot.event # Turning the bot online.
async def on_ready():
    print("This program has logged in to the account " + f"{bot.user}.\n")
    voice_channel = discord.utils.get(bot.get_guild(guild).channels, id = channel)
    await voice_channel.connect()
        
bot.run(os.getenv["TOKEN"], bot=False)
