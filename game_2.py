class location:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.neighbors = []

# Build entry
entry = location()
entry.name = "entry"
entry.neighbors = ["gallery"]
entry.description = "Here we are in the entry. From here you can see the " + entry.neighbors[0]

# Build gallery

gallery = location()
gallery.name = "gallery"
gallery.neighbors = ["kitchen", "entry"]
gallery.description = "Here we are in the gallery. From here you can see the " + gallery.neighbors[0]

# Build kitchen

kitchen = location()
kitchen.name = "kitchen"
kitchen.neighbors = ["gallery", "hall"]
kitchen.description = "Here we are in the kitchen. From here you can see the " + kitchen.neighbors[0]

# Build hall
hall = location()
hall.name = "hall"
hall.neighbors = ["kitchen", "gallery"]
hall.description = "Here we are in the hall. From here you can see the " + hall.neighbors[0]


class pc:
    name = "Nathan"
    location = entry
    hp = 10
    inventory = []

action_verbs = ["move", "take"]

input_string = "move to the gallery"
parsed_string = input_string.split()
action = [i for i in parsed_string if any(v in i for v in action_verbs)]

def move(parsed_string):
    dest = [i for i in parsed_string if any(v in i for v in pc.location.neighbors)]
    pc.location = eval(dest[0])
    print(pc.location.description)