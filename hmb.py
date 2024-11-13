import discord
from discord.ext import commands
from discord import app_commands

token = "MTI5OTMxOTg4ODQzMDQ5NzkwMw.GMbwUT."
token2 ="en1NUq0RtUpkTaMfy7Ca1zbg6SX0NLHacV_8fs"

tokenn = token + token2

intents = discord.Intents.default()
intents.members = True  
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées: {len(synced)}")
    except Exception as e:
        print(f"Erreur de synchronisation des commandes slash: {e}")






bot.run(tokenn)






















