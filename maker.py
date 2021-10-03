import discord
import filemanager as fm

def makeBoba(message):
    userTag = message.author
    authObject = fm.getAuthor(userTag)
    if authObject == -1:
        fm.addAuthor(userTag)

        # alternatively just use getPreferences/getAllergies
        authObject = fm.getAuthor(userTag)



