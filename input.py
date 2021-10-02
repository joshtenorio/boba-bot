import discord
import os

async def parseCommand(message):
    commandMessage = message.content.split(" ")
    if (commandMessage[0] == "$help"):
        await help(message)
#    if nextCommand

async def help(message):
    helpMessage = "list of commands:/n"
    helpMessage += "$help: list of commands."
    helpMessage += "$preference: change your preferences for tea"
    helpMessage += "$allergy: change your allergies"
    helpMessage += "$make: makes a boba for you!"
    helpMessage += "$list: lists the choices."
    await message.channel.send(helpMessage)
    


