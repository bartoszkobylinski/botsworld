import os
from aiohttp import client 
import discord
from pyairtable import Table
#  from dotenv import load_dotenv
import json

#  load_dotenv()
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
        users.append(row.get('fields', 'field not founded').get("User", 'user not founded'))
        sentence.append(row.get('fields', 'field not founded').get("Sentences", 'user not founded'))
    return dict(zip(users, sentence))




def send_message_to_discord_channel(message):
    return message


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
    if message.content.startswith("$users_sentences"):
        users_sentences = json.dumps(get_users_list_with_sentences())
        print(type(users_sentences))
        await message.channel.send(users_sentences)
    if send_message_to_discord_channel(message):
        await message.channel.send(message)


@client.event
async def some():
    pass

client.run(BOT_TOKEN)

