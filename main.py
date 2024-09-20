import discord
from discord.ext import commands

# Replace with your bot token
TOKEN = 'bot token here'

USER_ID_TO_MONITOR = 'user id here'

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot has logged in as {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    if member.id == USER_ID_TO_MONITOR:
        if not before.self_stream and after.self_stream:
            await member.move_to(None)
            print(f'User {member.name} has been kicked for starting to stream.')

bot.run(TOKEN)
