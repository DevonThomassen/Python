import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import asyncio
import datetime

# token from bot
import key

d_client = discord.Client()
client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(datetime.datetime.now())
    print('------')
    # Status what the bot is playing
    await client.change_presence(game=discord.Game(name='Getting better'))

@client.event
async def on_message(message):
    # fix @client.command
    await client.process_commands(message)
    # admin person
    if message.author.id == '198898599545798656':
        if message.content.lower().startswith('!ping'):
            print('hello admin')
    # role admin
        if message.content.lower().startswith('!admin?'):
            if '472433848366661635' in (role.id for role in message.author.roles):
                await client.send_message(message.channel, 'admin!')
            else:
                await client.send_message(message.channel, 'no...')
    # global
    if message.content.lower().startswith('!ping'):
        await client.send_message(message.channel, 'pong!')
    if message.content.lower().startswith('!say'):
        args = message.content.split(' ')
        await client.send_message(message.channel, (' '.join(args[1:])))
    # chat filter
    filter = ['badword1', 'badword2']
    bypass = ['1988985995457986562',    # Me
              '199100448957792256']     # Jason
    contents = message.content.split(' ')
    for word in contents:
        if word.lower() in filter:
            if not message.author.id in bypass:
                # bot needs access to delete the msg otherwise bot crashes
                # await client.delete_message(message)
                await client.send_message(message.channel, 'He noob')

@client.command()
async def cd():
    print('works')
    i = 5
    while i >= 0:
        await client.say(i)
        # important to not forget to put await in front of the sleep
        await asyncio.sleep(1)
        # important to not forget '-=' instead of only the '-'
        i -= 1

""""
Doesnt work ):
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted')
"""


client.run(key.token)
