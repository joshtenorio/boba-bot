import discord
import filemanager as fm

def makeBoba(message):
    u = fm.getAuthor(message.author)
    if u == -1:
        fm.addAuthor(message.author)
        u = fm.getAuthor(message.author)

    pref = fm.getPreferences(message.author)
    allergies = fm.getAllergies(message.author)
