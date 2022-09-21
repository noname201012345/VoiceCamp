import discord
import os
from discord.ext import commands
from rerun import rerun

client=commands.Bot(command_prefix=':', self_bot=True, help_command=None)

GUILD_ID = 755793441287438469
CHANNEL_ID = 994552773637062656

@client.event
async def on_ready():
    os.system('clear')
    print(f'Logged in as {client.user} ({client.user.id})')
    vc = discord.utils.get(client.get_guild(GUILD_ID).channels, id = CHANNEL_ID)
    await vc.connect()
    print(f"Successfully joined {vc.name} ({vc.id})")

client.run(os.getenv("TOKEN"))
rerun()
