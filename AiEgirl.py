import discord
from discord.ext import commands
import os
import logging

logging.basicConfig(level=logging.DEBUG)

TOKEN = 'MTI4MjM3MTM1MDQ5Mjc0MTc0Mw.GsUKWX.1SR3ehJ1Sa-FzvCA_proQn9ZkeRJi6Op7rv5Gw'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.debug(f'Bot logged in as {bot.user}!')

@bot.command()
async def picture(ctx, number: int = 1):
    image_file = f"{number}p.png"
    
    if os.path.isfile(image_file):
        logging.debug(f"Image file found: {image_file}")
        await ctx.send(file=discord.File(image_file))
        logging.debug(f"Image sent: {image_file}")
    else:
        await ctx.send("Image file not found!")
        logging.debug(f"Image file not found: {image_file}")

@bot.command(name='picture1')
async def picture_1(ctx):
    await picture(ctx, number=1)

@bot.command(name='picture2')
async def picture_2(ctx):
    await picture(ctx, number=2)

@bot.command(name='picture3')
async def picture_3(ctx):
    await picture(ctx, number=3)

@bot.command(name='picture4')
async def picture_4(ctx):
    await picture(ctx, number=4)

@bot.command(name='picture5')
async def picture_5(ctx):
    await picture(ctx, number=5)

@bot.command(name='picture6')
async def picture_6(ctx):
    await picture(ctx, number=6)

@bot.command(name='picture7')
async def picture_7(ctx):
    await picture(ctx, number=7)

@bot.command(name='picture8')
async def picture_8(ctx):
    await picture(ctx, number=8)

@bot.command(name='picture9')
async def picture_9(ctx):
    await picture(ctx, number=9)

@bot.command(name='picture10')
async def picture_10(ctx):
    await picture(ctx, number=10)

bot.run(TOKEN)
