import json

# NOTE:
# when referencing authors, use message.author.name + "#" + str(message.author.id)
# get a list of authors and their preferences
def getAuthors():
    with open('authors.json') as file:
        data = json.load(file)
        userList = data['authors']
    return userList

# parameter author is the discord tag
def addAuthor(author):
    # check if author already exists
    u = getAuthor(author)
    if u != -1:
        print(author + " already exists in .json")
        return

    authordict = {"author": author, "preferences": [], "allergies": ["none"] }
    users = getAuthors()
    users.append(authordict)
    dictionary = {"authors": users}
    with open('authors.json', 'w') as file:
        json.dump(dictionary, file)

def setPreferences(author, preferences):
    user = getAuthor(author)
    if user == -1:
        addAuthor(author)

    users = getAuthors()
    for u in users:
        if u['author'] == author:
            u["preferences"] = preferences
    dictionary = {"authors": users}
    with open('authors.json', "w") as file:
        json.dump(dictionary, file)

def setAllergies(author, allergies):
    user = getAuthor(author)
    if user == -1:
        addAuthor(author)

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
    if u == -1:
        addAuthor(tag)
        u = getAuthor(tag)
    return u["preferences"]

def getAllergies(tag):
    u = getAuthor(tag)
    if u == -1:
        addAuthor(tag)
        u = getAuthor(tag)
    return u["allergies"]

setPreferences("jardjard", ["asdf"])

# given a string, gets the relevant path to picture
def getPathPicture(input):
    photoDir = "photos/"
    extension = ".png"
    input.lower().replace()
    print(photoDir + input + extension)
    return photoDir + input + extension