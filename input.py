import discord
import os
import filemanager as fm

async def parseCommand(message):    # Takes input from user and selects with command to run
    commandMessage = message.content.split(" ")
    if (commandMessage[0] == "$help"):
        await help(message)
    if (commandMessage[0] == "$preference"):
        await preferences(message)
    if (commandMessage[0] == "$allergy"):
        await allergy(message)
    if (commandMessage[0] == "$make"):
        await make(message)
    if (commandMessage[0] == "$list"):
        await list(message)
    if (commandMessage[0] == "$json"):
        await listJson(message)

async def help(message):
    helpMessage = "**List of Commands:**\n"
    helpMessage += "$help: lists the commands.\n"
    helpMessage += "$preference: change your preferences for tea, each sepperated by a space.\n"
    helpMessage += "$allergy: change your allergies, each sepperated by a space.\n"
    helpMessage += "$make: makes a boba for you!\n"
    helpMessage += "$list: lists the choices.\n"
    await message.channel.send(helpMessage)

async def preferences(message):     # Change the preferences of the author
    preferenceArray = message.content.split(" ")    # Take the input and parse it into an array
    fm.setPreferences(message.author, preferenceArray)
    newPreferences = "Changed the preferences for "
    newPreferences += message.author
    newPreferences += "to:\n\t"
    newPreferences += preferenceArray
    await message.channel.send(newPreferences)

async def allergy(message):     # Change the allergies of the author
    allergyArray = message.content.split(" ")   # Take the input and parse it into an array
    fm.setAllergies(message.author, allergyArray)
    newAllergy = "Changed the preferences for "
    newAllergy += message.author
    newAllergy += "to:\n\t"
    newAllergy += preferenceArray
    await message.channel.send(newPreferences)

async def make(message):    
    pass
#   get the preferences of the message.author
#   get the allergies of the message.author
#   calculate the best drink to get (we should add a slight random factor
#   so you don't get the same drink every time)

async def list(message):
    listArray = message.content.split(" ")
    if(len(listArray) == 1):    # If the input is only $list
        listPrompt = "You can specify what your looking for using **$list <category>**\n"
        listPrompt += "Categories are:\n"
        listPrompt += "\t1) tea\n"
        listPrompt += "\t2) flavor\n"
        listPrompt += "\t3) toppings\n"
        listPrompt += message.author
        await message.channel.send(listPrompt)
    
    if(listArray[1].lower() == "tea" or listArray[1].lower() == "teas" or listArray[1] == "1"):
        listPrompt = "For teas, you have the following options:\n\n"
        listPrompt += "**Tea**: Green, Black, Oolong"
        await message.channel.send(listPrompt)
    
    if(listArray[1].lower() == "flavor" or listArray[1].lower() == "flavors" or listArray[1] == "2"):
        listPrompt = "For flavors, you have the following options:\n\n"
        listPrompt += "**Fruit Tea**: Honey, Lychee, Lychee Rose, Mango, Mango Passion Fruit, Mango Peach, Peach, Peach Pomegranate, Rose, Strawberry, Strawberry Lychee, Strawberry Mango, Strawberry Peach, Strawberry Pineapple\n"
        listPrompt += "**Milk Tea**: Almond, Banana, Chocolate, Coconut, Coffee, Earl Grey, Hokkaido, Nagasaki Green Honey, Honeydew, Jasmine, Lavender, Lavender Vanilla, Lychee Rose, Mango, Matcha, Okinawa, Pistachio, Rose, Royal, Taro, Taro Lavender, Thai, Tiger, Urban, Vanilla\n"
        await message.channel.send(listPrompt)
    
    if(listArray[1].lower() == "topping" or listArray[1].lower() == "toppings" or listArray[1] == "3"):
        listPrompt = "For toppings, you have the following options:\n\n"
        listPrompt += "**Toppings**: Brown Sugar, Crystal Boba, Coffee Jelly, Custard Pudding, Honey Boba, Lychee Jelly, Lychee Popping Pearls, Mango Popping Pearls, Pomegranate Popping Pearls, Rainbow Jelly, Rainbow Popping Pearls, Strawberry Popping Pearls, Tamarindo Straw"
        await message.channel.send(listPrompt)

    async def listJson(message):
        output = "Authors: "
        output += fm.getAuthor(getAuthors())
