// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('./config.json');
const { MessageReactionAdd } = require('discord.js/src/util/Events');

// Create a new client instance with the required permissions
const client = new Client({
     intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMessageReactions
    ],
});

// When the client is ready, run this code (only once)
// We use 'c' for the event parameter to keep it separate from the already defined 'client'
//This client.once block is borrowed from discord.js documentation
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
    console.log(client.guilds);
}
);

// Log in to Discord with your client's token
client.login(token)

const sentMessages = new Map();

// Check new messages. Confirms they do not come from LFG_BOT to prevent spam
client.on('messageCreate', async message => {
    if (message.author.username != "LFG_BOT"){
        message_string = message.content.split(" ");
        message_string[1] = Number(message_string[1])
        author = message.author.username;
//Only initiate bot with !LFG command
        if (message_string[0] == "!LFG"){


//Input validation to confirm standard of !LFG [int for players] [game name]
            if (isNaN(message_string[1])){
                message.channel.send("Please use an integer after !LFG to set number of players");
            }else if
                (typeof message_string[2] == 'undefined'){
                message.channel.send("Please enter the name of the game you wish to play");
            }else {
                const sentMessage = await message.channel.send(author + " wants to play " + message_string[2] + 
                " with " + message_string[1] + " people");
                sentMessage.react("😩");
//Reaction filter to only collect reaction posted in the recruitment message by bot
                const reactionFilter = (reaction, user) => {
                    return reaction.emoji.name === '😩' && user.id !== sentMessage.author.id;
                };

//Create map of sentMessages to store all messages to be called on later. Message ID and Game Name is stored.
                sentMessages.set(sentMessage.id, message_string[2]);


//Await reactions and user filter above as the collector, max will be the number designated by the original !LFG request       
                sentMessage.awaitReactions({filter: reactionFilter, max:message_string[1]})
                    .then(()=>{
                        gameName = sentMessages.get(sentMessage.id)
                        message.channel.send("The party is ready to play " + gameName);
                    });
            }
        }
    }
});

// Testing - Check for string "dota"
client.on('messageCreate', async message =>{
    const collectorFilter = message => message.content.includes('dota', 'Dota');
    const collector = message.channel.createMessageCollector({filter: collectorFilter});

    collector.on('collect', m =>{
        console.log(m.content+ " " + collector.collected);
    });

});



