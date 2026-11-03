# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def mem(ctx):
    with open('memes/meme1.webp', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    img_name = random.choice(os.listdir('memes'))
    with open(f'memes/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.command('fox')
async def fox(ctx):
    '''fox komutunu çağırdığımızda, program tilki_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

categories = {
    "animals": ["https://random.dog/woof.json", "https://randomfox.ca/floof/"],
    "gaming": ["https://images.unsplash.com/photo-1550745165-9bc0b252726f",
                "https://images.unsplash.com/photo-1612287233202-b51b36619dfc"],
    "anime": ["https://images.unsplash.com/photo-1578632767115-351597cf2477", 
              "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f"],
}

@bot.command()
async def animals(ctx):
  await ctx.send(random.choice(categories["animals"]))


@bot.command()
async def gaming(ctx):
  await ctx.send(random.choice(categories["gaming"]))


@bot.command()
async def anime(ctx):
  await ctx.send(random.choice(categories["anime"]))


ideas = ["araba lastiğinden saksı yapımı",
          " eski saksıları çiçek sulayıcı olarak kullanmak",
         "plastik şişelerden kedilere oyuncak yapmak",
         "plastık kutudan kalemlik yapmak",
         "plastik kutudan takı kutusu yapmak",
         " plastik şişeden diş fırçalık yapmak",
         "eski deterjan kutularından kitap tutacağı yapmak",
         "plastik şişeden telefon tutacağı yapmak",
         "plastik kutudan kuş yemliği yapmak",]

@bot.command()
async def idea(ctx):
    await ctx.send(random.choice(ideas))

bot.run('TOKEN')
