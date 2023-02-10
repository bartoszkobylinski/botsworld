import os
from flask import Flask, request, jsonify, url_for, render_template
from flask_restful import Resource, Api
from discord import SyncWebhook
import logging
from dotenv import load_dotenv
'''
load_dotenv()

level = logging.DEBUG
level_name = logging.getLevelName(level)
logging.basicConfig(filename="logs.txt", filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', force=True)
'''
app = Flask(__name__)
api = Api(app)


try:
    DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
except None as error:
    logging.CRITICAL("Discord Webhook got None value", + error)


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

'''
class BotEndpoint(Resource):
    def get(self):
        message = request.args.get("message")
        response = {"message": " " + (message if message else "default message")}
        return jsonify(response)

    def run(self):
        app.run()

    def post(self):
        message = request.get_json()
        if not message:
            logging.error("Error: There is no request message ")
            return 404, {"message": "There is no request message"}
        try:
            webhook = SyncWebhook.from_url(DISCORD_WEBHOOK)
            webhook.send(content=message)
            return {"message": message}, 200
        except Exception as error:
            logging.error("Exeption occured", exc_info=True)
            return {"message": error}, 404


api.add_resource(BotEndpoint, '/api/v1/send_json')
'''


if __name__ == "__main__":
    app.run()

