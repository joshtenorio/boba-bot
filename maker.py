import discord
import filemanager as fm
import json
from random import randint


def makeBoba(message):
    with open('options.json', 'r') as f:
        options = json.load(f)

    u = fm.getAuthor(message.author.name + "#" + str(message.author.id))
    if u == -1:
        fm.addAuthor(message.author.name + "#" + str(message.author.id))
        u = fm.getAuthor(message.author.name + "#" + str(message.author.id))

    pref = fm.getPreferences(message.author.name + "#" + str(message.author.id))
    allergies = fm.getAllergies(message.author.name + "#" + str(message.author.id))

    options_allergies = []
    pref_temp = []
    choice = ['', '', '']

    for i in allergies:
        for j in options['tea']:
            if j == i:
                options_allergies.append(i)
        for j in options['flavor']:
            if j == i:
                options_allergies.append(i)
        for j in options['topping']:
            if j == i:
                options_allergies.append(i)

    for i in options['tea']:
        print(i)
        for j in pref:
            print(j)
            for k in options_allergies:
                if i == j and i != k:
                    pref_temp.append(j)
    if len(pref_temp) == 0:
        for i in options['tea']:
            for j in options_allergies:
                if i != j:
                    pref_temp.append(j)
    print(len(pref_temp))
    choice[0] = pref_temp[randint(0, len(pref_temp) - 1)]
    pref_temp = []

    for i in options['flavor']:
        for j in pref:
            for k in options_allergies:
                if i == j and i != k:
                    pref_temp.append(j)
    if len(pref_temp) == 0:
        for i in options['flavor']:
            for j in options_allergies:
                if i != j:
                    pref_temp.append(j)
    choice[1] = pref_temp[randint(0, len(pref_temp) - 1)]
    pref_temp = []

    for i in options['topping']:
        for j in pref:
            for k in options_allergies:
                if i == j and i != k:
                    pref_temp.append(j)
    if len(pref_temp) == 0:
        for i in options['topping']:
            for j in options_allergies:
                if i != j:
                    pref_temp.append(j)
    choice[2] = pref_temp[randint(0, len(pref_temp) - 1)]

    print(choice[0] + '\n' + choice[1] + '\n' + choice[2] + '\n')
    return choice
