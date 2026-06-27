import discord
import io
import aiohttp
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy Geto bot, estoy inspirado en un personaje de anime de Jujutsu Kaisen. {bot.user}!')
    await ctx.send(file=discord.File('getoo.jpg'))

@bot.command()
async def lirios(ctx):
    await ctx.send("Los lirios son de mis plantas favoritas, huelen muy bien y significan mucho en diferentes culturas.")
    await ctx.send(file=discord.File('lirioss.jpg'))

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("")