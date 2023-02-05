import discord
import json

class MyClient(discord.Client):

    command = "$remove"

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # setup
        splitMessage = message.content.split()
        user = message.author
        channel = message.channel

        # guards
        if not splitMessage[0] == "$remove":
            return
        del splitMessage[0]
        if not len(splitMessage) > 0:
            return

        # success
        await channel.send("Deleting your message...")
        await message.delete()
        await channel.send("Deleted message.")
        await channel.send("Deleting messages containing the given words for user {}...".format(user))
        try:
            async for message in channel.history(limit=None):
                print("running...")
                for word in splitMessage:
                    if word in message.content:
                        await message.delete()
        except Exception as e:
            print(e)
        else:
            await channel.send("Finished deleting messages.")

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
        except:
            print("config.json file not present in the current directory or has some issue")
            quit()

    def _getClient(self):
        intents = discord.Intents(value = self.config['permissions'])
        intents.messages = True
        intents.message_content = True

        client = MyClient(intents=intents)
        return client


if __name__ == "__main__":
    DiscordDeleter()