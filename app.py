import os
from flask import Flask, request, jsonify, url_for, render_template
from flask_restful import Resource, Api
import requests
from discord import SyncWebhook

app = Flask(__name__)
api = Api(app)

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")


@app.route("/")
def index():
    return render_template("index.html")

class BotEndpoint(Resource):
    def get(self):
        message = request.args.get("message")
        response = {"message": " " + (message if message else "default message")}
        return jsonify(response)

    def run(self):
        app.run(host='localhost', port=6000)

    def post(self):
        message = request.get_json()
        print(f"I've got message: {message}")
        webhook = SyncWebhook.from_url(DISCORD_WEBHOOK)
        webhook.send(content=message)
        return {"message": message}, 200


api.add_resource(BotEndpoint, '/api/v1/send_json')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

