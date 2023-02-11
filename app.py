import os
from flask import Flask, request, jsonify, render_template
from discord import SyncWebhook
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def transform_message_to_string(json_data):
    data = json.loads(json_data)
    message = data.get("message", "")
    return message

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/send_message")
def send_message():
    if request.method == "POST":
        message = request.data()
        discord_webhook = request.data['webhook']
        print(type)
        webhook = SyncWebhook.from_url(discord_webhook)
        webhook.send(content=message["message"])
        return render_template("send_message.html")
    else:
        return render_template("send_message.html")

@app.route("/api/v1/send_json", methods=["GET"])
def query_data():
    data = request.args.get("message")
    return jsonify({"data":data})


@app.route("/api/v1/send_json", methods=["POST"])
def send_json_to_discord_bot():
    message = request.get_json()
    print(f"this is the type{type(message)} and message: {message}")
    webhook = SyncWebhook.from_url(DISCORD_WEBHOOK)
    #message = transform_message_to_string(message)
    webhook.send(content=message['message'])
    return jsonify({"message": message})


if __name__ == "__main__":
    app.run()

