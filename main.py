import discord
import os
from discord.ext import commands

# On demande au système d'aller chercher le token dans les variables secrètes
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot de test prêt : {bot.user.name}')

@bot.command()
async def test(ctx):
    await ctx.send("Le laboratoire de Luluhoo est opérationnel ! 🧪")

# Si on trouve le token, on lance le bot
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Erreur : Le token est introuvable dans les secrets.")
