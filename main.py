import os
from aiohttp import client 
import discord
from dotenv import load_dotenv

load_dotenv()
'''
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(message):
        if message.author == client.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
            
intents = discord.Intents.default()
intents.message_content = True


server_id = os.getenv("SERVER_ID")

client = MyClient(intents=intents)

client.run(os.getenv("DISCORD_TOKEN"))

'''
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot has logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello")

client.run(os.getenv("DISCORD_TOKEN"))

