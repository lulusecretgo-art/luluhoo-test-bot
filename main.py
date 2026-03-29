import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# On charge le token depuis le fichier .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Le bot de test est en ligne : {bot.user.name}')

@bot.command()
async def coucou(ctx):
    await ctx.send("Coucou ! Ton bot tourne en local sur ton PC ! 💻🚀")

bot.run(TOKEN)
