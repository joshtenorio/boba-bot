import discord
import os
import bs4
import filemanager as fm
from maker import makeBoba
import optionmanager as om
from googlesearch import search 

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
    if (commandMessage[0] == "$user"):
        await user(message)

async def help(message):
    helpMessage = "**List of Commands:**\n"
    helpMessage += "$help: lists the commands.\n"
    helpMessage += "$preference: change your preferences for tea, each separated by a space.\n"
    helpMessage += "$allergy: change your allergies, each separated by a space.\n"
    helpMessage += "$make: makes a boba for you!\n"
    helpMessage += "$list: lists the choices.\n"
    helpMessage += "$user: displays the users current Preferences and Allergies.\n"
    await message.channel.send(helpMessage)

async def preferences(message):     # Change the preferences of the author
    preferenceArray = message.content.split(" ")    # Take the input and parse it into an array
    preferenceArray.pop(0)      # Removes the "$preference" part of the string
    for p in range(len(preferenceArray)):   # Changes the input to be all lowercase
        preferenceArray[p] = preferenceArray[p].lower()
    fm.setPreferences((message.author.name + "#" + str(message.author.id)), preferenceArray)    # Changes the preferences in teh json file
    if(len(preferenceArray) == 0):    # If the input is only $allergy
        preferencePrompt = "You can specify what your preferences are using **$preference <preference1> <preference 2>**\n"
        await message.channel.send(preferencePrompt)
    else:   # If any preferences were listed
        newPreference = "Changed the preferences for **"
        newPreference += message.author.name
        newPreference += "** to:\n\t"
        for p in preferenceArray:
            newPreference += p
            newPreference += " "
        await message.channel.send(newPreference)

async def allergy(message):     # Change the allergies of the author
    allergyArray = message.content.split(" ")   # Take the input and parse it into an array
    allergyArray.pop(0)     # Removes the "$allergy" part of the string
    for a in range(len(allergyArray)):      # Changes the input to be all lowercase
           allergyArray[a] = allergyArray[a].lower()
    fm.setAllergies((message.author.name + "#" + str(message.author.id)), allergyArray)     # Changes the allergies in teh json file
    if(len(allergyArray) == 0):    # If the input is only $allergy
        allergyPrompt = "You can specify what your allergies are using **$allergy <allergy1> <allergy2>**\n"
        await message.channel.send(allergyPrompt)
    else: 
        newAllergy = "Changed the allergy for **"
        newAllergy += message.author.name
        newAllergy += "** to:\n\t"
        for a in allergyArray:
            newAllergy += a
            newAllergy += " "
        await message.channel.send(newAllergy)

async def make(message):
    choice = makeBoba(message)
    tea = om.getTea()
    flavor = om.getFlavors()
    toppings = om.getToppings()
    paths = ["", "", ""]
    name = message.author.name
    output = name + ", your boba order is:\n"
    for c in choice:
        output += c + "\n"
    await message.channel.send(output)
    print(len(choice))
    for t in tea:
        for c in choice:
            if c == t:
                paths[0] = fm.getPathPicture(c)

    for f in flavor:
        for c in choice:
            if c == f:
                paths[1] = fm.getPathPicture(c)

    for t in toppings:
        for c in choice:
            if c == t:
                paths[2] = fm.getPathPicture(c)

    print(paths)
    for p in paths:
        await message.channel.send(file=discord.File(p))

async def list(message):    # Lists the possible choices from the boba bot
    listArray = message.content.split(" ")
    if(len(listArray) == 1):    # If the input is only $list
        listPrompt = "You can specify what your looking for using **$list <category>**\n"
        listPrompt += "Categories are:\n"
        listPrompt += "\t1) tea\n"
        listPrompt += "\t2) flavor\n"
        listPrompt += "\t3) toppings\n"
        await message.channel.send(listPrompt)
    else: 
        if(listArray[1].lower() == "tea" or listArray[1].lower() == "teas" or listArray[1] == "1"):
            listPrompt = "For teas, you have the following options:\n\n"
            for i in range(len(om.getTea()) - 1):
                listPrompt += om.getTea()[i] + ", "
            listPrompt += om.getTea()[len(om.getTea()) - 1]

            await message.channel.send(listPrompt)
        
        if(listArray[1].lower() == "flavor" or listArray[1].lower() == "flavors" or listArray[1] == "2"):
            listPrompt = "For flavors, you have the following options:\n\n"
            for i in range(len(om.getFlavors()) - 1):
                listPrompt += om.getFlavors()[i] + ", "
            listPrompt += om.getFlavors()[len(om.getFlavors()) - 1]
            
            await message.channel.send(listPrompt)
        
        if(listArray[1].lower() == "topping" or listArray[1].lower() == "toppings" or listArray[1] == "3"):
            listPrompt = "For toppings, you have the following options:\n\n"
            for i in range(len(om.getToppings()) - 1):
                listPrompt += om.getToppings()[i] + ", "
            listPrompt += om.getToppings()[len(om.getToppings()) - 1]

            await message.channel.send(listPrompt)

async def user(message):    # Used to view the preferences and allergies of the current user
    userPrint = "Let's take a look at "
    userPrint += message.author.name
    userPrint += "'s personal information:\n\t"
    userPrint += "**Preferences**: "
    preferenceArray = fm.getPreferences(message.author.name + "#" + str(message.author.id))
    for p in preferenceArray:
            userPrint += p
            userPrint += " "
    userPrint += "\n\t**Allergies**: "
    allergyArray = fm.getAllergies(message.author.name + "#" + str(message.author.id))
    for a in allergyArray:
            userPrint += a
            userPrint += " "
    await message.channel.send(userPrint)
