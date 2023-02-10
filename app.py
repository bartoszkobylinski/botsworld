import os
from flask import Flask, request, jsonify, render_template
from discord import SyncWebhook
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/v1/send_json", methods=["GET"])
def query_data():
    data = request.args.get("message")
    return jsonify({"data":data})


@app.route("/api/v1/send_json", methods=["POST"])
def send_json_to_discord_bot():
    message = request.get_json()
    webhook = SyncWebhook.from_url(DISCORD_WEBHOOK)
    webhook.send(content=message)
    return jsonify({"message": message})


if __name__ == "__main__":
    app.run()

