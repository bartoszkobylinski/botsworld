import os 
import discord
from dotenv import load_dotenv

load_dotenv()

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

client = MyClient(intents=intents)

client.run(os.getenv("DISCORD_TOKEN"))

