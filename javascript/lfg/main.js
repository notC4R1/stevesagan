// Require the necessary discord.js classes
const { Client, Events, GatewayIntentBits } = require('discord.js');
const { token } = require('./config.json');

// Create a new client instance
const client = new Client({
     intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ],
});

// When the client is ready, run this code (only once)
// We use 'c' for the event parameter to keep it separate from the already defined 'client'
client.once(Events.ClientReady, c => {
	console.log(`Ready! Logged in as ${c.user.tag}`);
    console.log(client.guilds);
}
);

// Log in to Discord with your client's token
client.login(token)

client.on('messageCreate', (message)=>{
    message_string = message.content.split(" ")
    if (message_string[0] === "!LFG"){
        message.channel.send(message.author.username + " " + "Wants to play " +
        message_string[2] + " " + "with " + message_string[1] + " people.");
    }

});

