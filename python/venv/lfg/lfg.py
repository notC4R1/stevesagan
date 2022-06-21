import discord
import secrets

API_ENDPOINT = "https://discord.com/api/v10"
CLIENT_SECRET = secrets.CLIENT_SECRET
CLIENT_ID = secrets.CLIENT_ID
CLIENT_TOKEN = secrets.CLIENT_TOKEN
REDIRECT_URI = ""

client = discord.Client()

@client.event
async def on_ready():
    print("Signed in as LFG_BOT$1531".format(client))
##Testing Purpose to ID channels
    for guild in client.guilds:
        print(guild)
        for channel in guild.channels:
            print(channel)

@client.event
async def on_message(message):
    if (message.author.display_name != "LFG_BOT"):
        channel = message.channel
        text = message.content
        text = text.split()
        if (len(text) > 3):
            await channel.send("Please initiate bot with 'LFG [1-4] [Game Name")
        else:
            if (str(text[0]) == "!LFG"):
                await channel.send("prints")

client.run(CLIENT_TOKEN)
