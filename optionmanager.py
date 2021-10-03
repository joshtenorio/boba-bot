import json

def getTea():
    with open("options.json", "r") as f:
        data = json.load(f)
        tea = data["tea"]
        return list(tea.keys())

def getToppings():
    with open("options.json", "r") as f:
        data = json.load(f)
        toppings = data["topping"]
        return list(toppings.keys())

def getFlavors():
    with open("options.json", "r") as f:
        data = json.load(f)
        flavor = data["flavor"]
        return list(flavor.keys())