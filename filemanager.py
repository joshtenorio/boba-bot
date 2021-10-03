import json

# get a list of authors and their preferences
def getAuthors():
    with open('authors.json') as file:
        data = json.load(file)
        userList = data['authors']
    return userList

# parameter author is the discord tag
def addAuthor(author):
    authordict = {"author": author, "preferences": [], "allergies": [] }
    users = getAuthors()
    users.append(authordict)
    dictionary = {"authors": users}
    with open('authors.json', 'w') as file:
        json.dump(dictionary, file)

def setPreferences(author, preferences):
    users = getAuthors()
    for u in users:
        if u['author'] == author:
            u["preferences"] = preferences
    dictionary = {"authors": users}
    with open('authors.json', "w") as file:
        json.dump(dictionary, file)

def setAllergies(author, allergies):
    users = getAuthors()
    for u in users:
        if u['author'] == author:
            u["allergies"] = allergies
    dictionary = {"authors": users}
    with open('authors.json', "w") as file:
        json.dump(dictionary, file)

def getAuthor(tag):
    users = getAuthors()
    for u in users:
        if u['author'] == tag:
            return u
    return -1

def getPreferences(tag):
    u = getAuthor(tag)
    return u["preferences"]

def getAllergies(tag):
    u = getAuthor(tag)
    return u["allergies"]

