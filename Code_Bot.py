# writing the code bot #
# importing modules #
import discord 
import os 
import random 
from dotenv import load_dotenv 

# Initializing variables #
load_dotenv() 
 
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  
client = discord.Client(intents=intents)
token = str(os.getenv('TOKEN')) #Creating client to send a requesto to disord API #

# Initializing the Bot #
@client.event 
async def on_ready(): 
    print("Logged in as a bot {0.user}".format(client)) 

jokes_responses = {
    "why you can't write with a broken pencil": "because it is pointless"
}

# Setting appropiate response to user meassage #    
@client.event 
async def on_message(message): 
    username = str(message.author).split("#")[0] 
    channel = str(message.channel.name) 
    user_message = str(message.content) 
  
    print(f'Message {user_message} by {username} on {channel}') 
  
    if message.author == client.user: 
        return
  
    if channel == "general": 
        if user_message.lower() == "hello" or user_message.lower() == "hi": 
            await message.channel.send(f'Hello {username}') 
            return
        elif user_message.lower() == "bye": 
            await message.channel.send(f'Bye {username}') 
        elif user_message.lower() == "tell me a joke": 
            joke = random.choice(list(jokes_responses.keys()))
            response = jokes_responses[joke]
            await message.channel.send(f'{joke}\n\n{response}')

# Argument to run the bot by calling an event #         
client.run(token)  