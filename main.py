import discord
from discord.ext import commands

# Configuration des permissions (ce qu'on a coché sur le portail)
intents = discord.Intents.default()
intents.message_content = True  # Pour lire les messages
intents.members = True          # Pour voir les membres

# On crée le bot avec un préfixe (ex: !test)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Le bot de test est en ligne : {bot.user.name}')
    print('------')

@bot.command()
async def coucou(ctx):
    await ctx.send(f"Salut {ctx.author.mention} ! Ton bot de test fonctionne parfaitement. 🚀")

@bot.command()
async def ping(ctx):
    latence = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong ! ({latence}ms)")

# REMPLACE 'TON_TOKEN_ICI' par le jeton que tu as copié
bot.run('TOKEN_SECRET_ICI')
