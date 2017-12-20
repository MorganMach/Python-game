 #Objects for game2

# how to take 
	
input_string = "take the book"
parsed_string = input_string.split()
action = [i for i in parsed_string if any(v in i for v in action_verbs)]

def take(parsed_string):
	obj = [i for i in parsed_string if any(v in i for v in player1.location.inventory)]
	player1.inventory = player1.inventory + obj
	
	
class takables:
	def __init__(self):
		self.name = ""
		self.description = "" 
	
	def look(self):
		print(self.description)
	