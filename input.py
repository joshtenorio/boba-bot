import discord
import os

async def parseCommand(message):
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
#   set the preferences to the message.author 

async def allergy(message):     # Change the allergies of the author
    allergyArray = message.content.split(" ")   # Take the input and parse it into an array
#   set the allergies to the message.author

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
        await message.channel.send(listPrompt)
    
    if(listArray[1].lower == "tea" or listArray[1].lower == "teas" or listArray[1] == "1"):
        listPrompt = "For **teas**, you have the following options:\n\n"
        listPrompt += "Tea: Green\t\nBlack\t\nOolong"
        await message.channel.send(listPrompt)
    
    if(listArray[1].lower() == "flavor" or listArray[1].lower() == "flavors" or listArray[1] == "2"):
        listPrompt = "For **flavors**, you have the following options:\n\n"
        listPrompt += "Fruit Tea: Honey\nLychee\nLychee Rose\t\nMango\t\nMango Passion Fruit\t\nMango Peach\t\nPeach\t\nPeach Pomegranate\t\nRose\t\nStrawberry\t\nStrawberry Lychee\t\nStrawberry Mango\t\nStrawberry Peach\t\nStrawberry Pineapple\n"
        listPrompt += "Milk Tea: Almond\t\nBanana\t\nChocolate\t\nCoconut\t\nCoffee\t\nEarl Grey\t\nHokkaido\t\nNagasaki Green Honey\t\nHoneydew\t\nJasmine\t\nLavender\t\nLavender Vanilla\t\nLychee Rose\t\nMango\t\nMatcha\t\nOkinawa\t\nPistachio\t\nRose\t\nRoyal\t\nTaro\t\nTaro Lavender\t\nThai\t\nTiger\t\nUrban\t\nVanilla\n"
        await message.channel.send(listPrompt)
    
    if(listArray[1].lower() == "topping" or listArray[1].lower() == "toppings" or listArray[1] == "3"):
        listPrompt = "For **toppings**, you have the following options:\n\n"
        listPrompt += "Toppings: Brown Sugar\t\nCrystal Boba\t\nCoffee Jelly\t\nCustard Pudding\t\nHoney Boba\t\nLychee Jelly\t\nLychee Popping Pearls\t\nMango Popping Pearls\t\nPomegranate Popping Pearls\t\nRainbow Jelly\t\nRainbow Popping Pearls\t\nStrawberry Popping Pearls\t\nTamarindo Straw"

#   list out the drink options
