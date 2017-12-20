#Verbs
### Define pc class

import locations.py

class pc:
	def __init__(self):
		self.name = ""
		self.location = library
		self.hp = 10
		self.inventory = []
	
player1 = pc()

action_verbs = ["move", "take"]

#how to move 

input_string = "move to the gallery"
parsed_string = input_string.split()
action = [i for i in parsed_string if any(v in i for v in action_verbs)]

def move(parsed_string):
    dest = [i for i in parsed_string if any(v in i for v in player1.location.neighbors)]
    player1.location = eval(dest[0])
    print(player1.location.description)
	