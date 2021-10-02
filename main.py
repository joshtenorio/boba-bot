import discord
import os
import input

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
        await input.parseCommand(message) 
        

client.run('ODkzOTY0NTE3OTc1OTQ1MjU2.YVjHVg.OHTxuCtXYcIkWLupRMWRavs5pAU')