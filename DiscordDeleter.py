import discord
import json

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

class DiscordDeleter:

    def __init__(self):
        self.config = self._getJson()
        self.client = self._getClient()

        self.client.run(self.config['token'])

    def _getJson(self):
        try:
            with open('config.json') as f:
                data = json.loads(f.read())
            return data
        except Exception as e:
            print("config.json file not present in the current directory or has some issue")
            quit()

    def _getClient(self):
        intents = discord.Intents(self.config['permissions'])

        client = MyClient(intents=intents)
        return client

if __name__ == "__main__":
    DiscordDeleter()