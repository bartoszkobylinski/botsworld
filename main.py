import os
from aiohttp import client 
import discord
from pyairtable import Table
from dotenv import load_dotenv
import json

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
# Airtable integration

def get_users_list_with_sentences():
    users = []
    sentence = []
    table = Table(os.getenv("AIRTABLE_API_KEY"), os.getenv("AIRTABLE_BASE_ID"), os.getenv('AIRTABLE_TABLE_NAME'))
    data = table.all()
    for row in data:
        users.append(row.get('fields','do not find fields').get("User",'do not find user'))
        sentence.append(row.get('fields','do not find fields').get("Sentences", 'do not find user'))
    return dict(zip(users,sentence))

users_sentence_list = get_users_list_with_sentences()
print(users_sentence_list)


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
'''
