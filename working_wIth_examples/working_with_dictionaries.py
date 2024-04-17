#  Examples of how to use a dictionary in Python
#  Dictionaries are defined with key:value pairs (note comma)
#  Keys can be integers or strings
test_dict = {
    1: "one",
    2: "two",
    3: "three"

}
# We retrieve items from a dictionary using the dictionary
# name and specifying a key
print("*** Return the value with the key of 2")
print(test_dict[2])
# iterating through a dict with a loop
print("Iterate through a list with a loop")
for i in range(1, 3):  # start at 1 stop before 3
    print(test_dict[i])
# Methods used with Dictionaries
# Return a list of all values in the dictionary
test_dict[1] = "REPLACED"
print("*** Return a List of all the values in a dictionary")
print(test_dict.values())
# Find the length of the dictionary (number of key:item pairs)
dict_length = len(test_dict.values())
print(f"*** The length of the dictionary is {dict_length} items")
print("*** Use the get method for another way to return a value with a key")
print(test_dict.get(2))
# How would you make a dictionary of class members with
# email address(as the key), last name  first name and email address?
ITN1_class = {
    "fgluck@sanford.org": "Gluck, Fredric",
}

item_value = {  # Key is player number, value is list of items in the backpack
    "FBG": ["ax", "knife"],
    "TJG": ["knife", "water"]
}

points = {
    "ax": 23,
    "knife": 44

}

print(ITN1_class["fgluck@sanford.org"])

# From Python QOD
game_pieces = {
    "Chess": 32,
    "Checkers": 24,
    "Othello": 64,
    "Deck of Cards": 52,
    "Mancala": 48
}

# What is the correct way to retrieve the number of pieces for the game Mancala?

print (f"The number of pieces for Mancala is: {game_pieces['Mancala']}")
