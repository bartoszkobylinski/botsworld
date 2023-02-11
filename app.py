import os
from flask import Flask, request, jsonify, render_template
from discord import SyncWebhook
from dotenv import load_dotenv
import json

load_dotenv()
app = Flask(__name__)
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/send_message")
def send_message():
    if request.method == "POST":
        try:
            message = request.get_json()
            discord_webhook = message['discord_webhook']
            webhook = SyncWebhook.from_url(discord_webhook)
            webhook.send(content=message["message"])
            return jsonify({"message": "Message sent successfully!"}), 200
        except KeyError:
            return jsonify({"error": "Missing 'message' or 'discord_webhook' in JSON payload"}), 400
        except ValueError:
            return jsonify({"error": "Invalid Discord webhook URL."}), 400
    else:
        return render_template("send_message.html")


if __name__ == "__main__":
    app.run()

