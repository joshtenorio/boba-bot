import discord
import os
import input
import auth
client = discord.Client()

@client.event
async def on_ready():
        print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
        print(message.content)
        print(message.author)
        if message.author == client.user:
                return

        if message.content.startswith('$hello'):
                await message.channel.send('Hello!')
        if message.content.startswith('$joke'):
                await message.channel.send("don't spell part backwards, its a trap!")
                
        await input.parseCommand(message) 
        

client.run(auth.botToken)
