import threading
from cProfile import run

import discord
from flask import Flask, request
from flask_restful import Resource, Api
from threading import Thread
from bot import client as discord_client
import requests


app = Flask(__name__)
api = Api(app)





class BotEndpoint(Resource):
    def get(self):
        return {"message": "welcome"}
    
    def post (self):
        message = request.get_json()
        send_message(message)
        return {"message": message}, 200
    
    def run():
        app.run(host='localhost', port=6000)


api.add_resource(BotEndpoint, '/api/v1/send_message')




def send_message(message):
    discord_bot_url = f"https://discordapp.com/api/v6/bots/{BOT_TOKEN}/channels/{CHANEL_ID}/messages"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bot {bot_token}"
    }
    payload = {
        "content": message
    }
    response = requests.post(discord_bot_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message")


if __name__ == "__main__":

    app.run(debug=True, port=6000)
