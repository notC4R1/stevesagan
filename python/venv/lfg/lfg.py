import discord
import secrets
import asyncio

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
###Check if anyone but the bot is triggering the call.
    if (message.author.display_name != "LFG_BOT"):
        text = message.content
        text = text.split(" ")
        if (text[0] == "!LFG"):
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
###Check for bots own response to add first reaction so users can easily click it
    if "wants to play" in message.content.lower():
        await message.add_reaction(emoji)
###Check for the reaction from users. Else statement to ignore the bots initial reaction
    def check(reaction, user):
        return user == message.author and str(reaction.emoji) == "😩"
    try:
        reaction, user = await client.wait_for('reaction_add', timeout = 10.0, check=check)
    except :
        pass
    else:
        if user.display_name != "LFG_BOT" and reaction.emoji == "😩":
            await channel.send('Good')
            await channel.send(user.display_name + reaction.emoji)

 




client.run(CLIENT_TOKEN)
