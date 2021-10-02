import json

# get a list of authors and their preferences
def getAuthors():
    with open('authors.json') as file:
        data = json.load(file)
        print(type(data['authors'])) # this is list
        userList = data['authors']
        print(data['authors'][0]['author'])
    return userList

def addAuthor(author):
    pass

def setPreferences(author, preferences):
    pass

def setAllergies(author, allergies):
    pass

def getAuthor(tag):
    users = getAuthors()
    for u in users:
        if u['author'] == tag:
            print("found u")
            return u

def getPreferences(tag):
    u = getAuthor(tag)
    return u["preferences"]

def getAllergies(tag):
    u = getAuthor(tag)
    return u["allergies"]


