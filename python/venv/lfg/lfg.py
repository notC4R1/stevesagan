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
    emoji = "😩"
    channel = message.channel
    if (message.author.display_name != "LFG_BOT"):
        text = message.content
        text = text.split(" ")
        try:
            text[1] = int(text[1])
        except:
            await channel.send("Please use integers to specify number of players")
            return
        if (len(text) < 3 or len(text) > 3):
            test = "fail"
            await channel.send("Please initiate bot with 'LFG [1-4] [Game Name]")
            
        else:
            if (str(text[0]) == "!LFG"):
                bot_message = str(message.author) + " wants to play " + text[2] + " with " + str(text[1]) + " people. Please use :weary: to join."
                await channel.send(bot_message)
    else:
        await message.add_reaction(emoji)



client.run(CLIENT_TOKEN)
