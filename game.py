
def library():
	print()
	print("A door leads to the hallway") 
	response = "empty"
	while response not in ("hall"):
		response = input("Please leave the room") 
		
	if response == "hall":
			hall()
			
def hall():
	print()
	print("you can move to the kitchen or art room") 
	response = poke
	while response not in ("kitchen", "art room"):
		response = input("staying still is probably a bad idea") 
		
	if response == "art room":
		art_room()
	elif response == "kitchen":
		kitchen()