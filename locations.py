### Build location class and locations



#   Build another fn (probably look, takes item desc, make more rooms

class location:
    def __init__(self):
        self.name = ""
        self.description = ""
		self.inventory = []
        self.neighbors = []

# Build library

library = location() # make empty location object called "library"
library.name = "library" # define "name" attribute
library.neighbors = ["hall"] # define "neighbors attribute"
library.inventory = ["book"]
library.description = "Here we are in the library. From here you can see the " + library.neighbors[0] + "a" library.inventory

# Build gallery

gallery = location()
gallery.name = "gallery"
gallery.neighbors = ["kitchen", "art_room"]
gallery.description = "Here we are in the gallery. From here you can see the " + gallery.neighbors[0]

# Build kitchen

kitchen = location()
kitchen.name = "kitchen"
kitchen.neighbors = ["gallery", "hall"]
kitchen.description = "Here we are in the kitchen. From here you can see the " + kitchen.neighbors[0]

# Build hall
hall = location()
hall.name = "hall"
hall.neighbors = ["kitchen", "gallery", "library"]
hall.description = "Here we are in the hall. From here you can see the " + hall.neighbors[0]

# Build art room
art_room = location()
art_room.name = "art room"
art_room.neighbors = ["gallery", "hall"]
art_room.description = "Messy, as usual. You can see the " + art_room.neighbors[0]

# Build main room
main_room = location()
main_room.name = "main room"
main_room.neighbors = ["gallery"]
main_room.description = "There is an odd scent in the air. Behind you is the " +main_room.neighbors[0]

	
#How to commit to git, check status, add with "git add", git commit, write message, git push (origin master)
