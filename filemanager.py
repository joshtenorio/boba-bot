import json

# get a list of authors and their preferences
def getAuthors():
    with open('authors.json') as file:
        data = json.load(file)
        userList = data['authors']
    return userList

def addAuthor(author):
    pass

def setPreferences(author, preferences):
    pass

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

def getPreferences(tag):
    u = getAuthor(tag)
    return u["preferences"]

def getAllergies(tag):
    u = getAuthor(tag)
    return u["allergies"]

setAllergies("tenmo#6399", ["boop"])
print(getAllergies("tenmo#6399"))
