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
            for k in options['tea'][j]:
                if k == i:
                    options_allergies.append(j)
        for j in options['flavor']:
            for k in options['flavor'][j]:
                if k == i:
                    options_allergies.append(j)
        for j in options['topping']:
            for k in options['topping'][j]:
                if k == i:
                    options_allergies.append(j)

    if pref[0] != 'none' and len(options_allergies) > 0:
        for i in options['tea']:
            for j in pref:
                for k in options_allergies:
                    if i == j and i != k:
                        pref_temp.append(i)
        choice[0] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['flavor']:
            for j in pref:
                for k in options_allergies:
                    if i == j and i != k:
                        pref_temp.append(i)
        choice[1] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['topping']:
            for j in pref:
                for k in options_allergies:
                    if i == j and i != k:
                        pref_temp.append(i)
        choice[2] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

    elif pref[0] == 'none' and len(options_allergies) > 0:
        for i in options['tea']:
            for j in options_allergies:
                if i != j:
                    pref_temp.append(i)
        choice[0] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['flavor']:
            for j in options_allergies:
                if i != j:
                    pref_temp.append(i)
        choice[1] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['topping']:
            for j in options_allergies:
                if i != j:
                    pref_temp.append(i)
        choice[2] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

    elif pref[0] != 'none' and len(options_allergies) == 0:
        for i in options['tea']:
            for j in pref:
                if i == j:
                    pref_temp.append(i)
        choice[0] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['flavor']:
            for j in pref:
                if i == j:
                    pref_temp.append(i)
        choice[1] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['topping']:
            for j in pref:
                if i == j:
                    pref_temp.append(i)
        choice[2] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

    elif pref[0] == 'none' and len(options_allergies) == 0:
        for i in options['tea']:
            pref_temp.append(i)
        choice[0] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

        for i in options['flavor']:
            pref_temp.append(i)
        choice[1] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []
        for j in options['topping']:
            pref_temp.append(i)
        choice[2] = pref_temp[randint(0, len(pref_temp) - 1)]
        pref_temp = []

    print(choice[0] + '\n' + choice[1] + '\n' + choice[2] + '\n')
    return choice
