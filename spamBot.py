import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

intent = discord.Intents.default()
intent.message_content = True
bot = commands.Bot(command_prefix='/', intents=intent)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def spam(ctx, *args):
    arguments = ' '.join(args)
    for role in ctx.author.roles:
        if role.name == 'Spammer':
            for i in range(100):
                await ctx.send(arguments)

bot.run(os.getenv('TOKEN'))
