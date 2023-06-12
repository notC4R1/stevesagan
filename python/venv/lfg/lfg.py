from operator import length_hint
import discord
import secrets
import asyncio

API_ENDPOINT = "https://discord.com/api/v10"
CLIENT_SECRET = secrets.CLIENT_SECRET
CLIENT_ID = secrets.CLIENT_ID
CLIENT_TOKEN = secrets.CLIENT_TOKEN
REDIRECT_URI = ""

client = discord.Client()
guild_text_channels = []
guild_members = []


@client.event
async def on_ready():
    print("Signed in as LFG_BOT$1531".format(client))
##Testing Purpose to ID channels
    for guild in client.guilds:
        print(guild)
        for channel in guild.channels:
            if type(channel) == discord.TextChannel:
                guild_text_channels.append(channel)
        for member in guild.members:
            guild_members.append(member)
    for i in range(len(guild_text_channels)):
        print(guild_text_channels[i])


@client.event
async def on_message(message):
    emoji = "😩"
    channel = message.channel

###Check if anyone but the bot is triggering the call.
    if (message.author.display_name != "LFG_BOT"):
        message_id = message.id
        text = message.content
        text = text.split(" ")
        if (text[0] == "!LFG"):
            try:
                text[1] = int(text[1])
            except:
                await channel.send("Please use integers to specify number of players")
                return
            if (len(text) < 3 or len(text) > 3):
                await channel.send("Please initiate bot with 'LFG [1-4] [Game Name]")
                
            else:
                if (str(text[0]) == "!LFG"):
                    bot_message = str(message.author) + " wants to play " + text[2] + " with " + str(text[1]) + " people. Please use :weary: to join."
                    await channel.send(bot_message)
                    await channel.send(str(message_id) + " " + str(message.author.display_name))


###Check for bots own response to add first reaction so users can easily click it
    if "wants to play" in message.content.lower():
        await message.add_reaction(emoji)


###Monitor all reactions
@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    reaction_total = 0
    split_message = message.content.split()
    reaction_goal = int(split_message[6])
    if (message.author.display_name == "LFG_BOT"):
        for reaction in message.reactions:
            reaction_total = reaction.count
            await channel.send(reaction.users())
        await channel.send(str(reaction_total)+ " reactions")
        if int(reaction_total -1 ) == reaction_goal:
            #await channel.send(payload.member.display_name + " used this emoji" + message.reactions[0].emoji)
            await channel.send("Team is ready!!")

    

 
client.run(CLIENT_TOKEN)
