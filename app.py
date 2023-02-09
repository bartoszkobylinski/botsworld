import os
from flask import Flask, request, jsonify, url_for, render_template
from flask_restful import Resource, Api
from discord import SyncWebhook
import logging
from dotenv import load_dotenv

load_dotenv()

level = logging.DEBUG
level_name = logging.getLevelName(level)
logging.basicConfig(filename="logs.txt", filemode='w', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', force=True)
app = Flask(__name__)
api = Api(app)


try:
    DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")
except None as error:
    logging.CRITICAL("Discord Webhook got None value", + error)

disc_web = 'https://discord.com/api/webhooks/1072191615491375225/HexMlgMPhY_KqD4DSCyn5z3qvEIhg2VfFCpZYBW8m72FIojvQSvwoUUyO4bclf72X9Xb'
@app.route("/")
def index():
    return render_template("index.html")


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
            webhook = SyncWebhook.from_url(disc_web)
            webhook.send(content=message)
            return {"message": message}, 200
        except Exception as error:
            logging.error("Exeption occured", exc_info=True)
            return {"message": error}, 404


api.add_resource(BotEndpoint, '/api/v1/send_json')

if __name__ == "__main__":
    app.run()

