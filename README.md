# Send Message to Discord Webhook

This is an endpoint at www.bartoszkobylinski.com/api/v1/send_message where you can send a message to your Discord webhook.
## Obtaining a Discord Webhook

To obtain a Discord webhook, you need to create a webhook for a specific channel in your Discord server. You can find detailed information on how to do this on the official Discord site.
https://discord.com/developers/docs/intro
### Usage
To use the send_message endpoint, you'll need to provide the message you want to send and the Discord webhook URL in a JSON payload. The message content should be in the format {"message": "Your message here"} and the Discord webhook should be in the format {"discord_webhook": "https://discordapp.com/api/webhooks/your-webhook-url"}.

Please note that this endpoint should not be overused, as it can impact the performance of the server and the Discord API.

### Cloning the Project
To clone the project, you can use the following command:

git clone https://github.com/your-username/your-project.git

### Installing Dependencies

The project dependencies are listed in the `requirements.txt` file. To install them, you can use the following command:

pip install -r requirements.txt

This will install all the packages listed in the `requirements.txt` file, which are necessary for the project to run properly.

Thank you!