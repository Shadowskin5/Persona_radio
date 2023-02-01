'''
 Author: Blake Lupien
 Date: 2023-18-01
 Description: This is a test file for the discord.py library and the discord API
 Advised by Jaden Daniels, the goat'''

import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefixP='!', intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'Logging into {client.user}...')

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1-10')
#async and await are hand and hand. async enables await, which is a response to async. They communciate with each other. Cool stuff :)
#ctx is the context of the message. It is the message itself.
    answer = random.randint(1, 10)

    input = await client.wait_for('message')

    if int(input.content) == answer:
        await ctx.send('Yippee! Thats it!')
    else:
        await ctx.send(f'No, it is fr {answer}')

    

client.run('MTA1MzMzMjI3NDkwMjQ3OTAyOQ.GG9wqR.72DIqqkPBLlRBpFldLjBJGTo3y7lX54aoLquzI')