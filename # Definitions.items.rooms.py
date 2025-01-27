# Definitions Items.Rooms
game_room = {
    "name": "game room",
    "type": "room",
}
piano = {
    "name": "piano",
    "type": "furniture",
}
couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}
key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

#BedRoom1
bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}
queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}
door_b = {
    "name": "door b",
    "type": "door",
}
key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,   
} 
door_c = {
    "name": "door c",
    "type": "door",
}
#BedRoom 2
bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}
double_bed = {
    "name": "double bed",
    "type": "furniture",
}
key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}    
dresser = {
    "name": "dresser",
    "type": "furniture",
}


#Living Room

living_room = {
    "name": "living room",
    "type": "room",
}
dining_table = {
    "name": "dining table",
    "type": "furniture",
}
sink = {
    "name": "sink",
    "type": "accident",
}
door_d = {
    "name": "door d",
    "type": "door",
}
key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}
#Outside
outside = {
  "name": "outside"
}
all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

all_furniture = [piano, queen_bed, double_bed, dresser, dining_table]

all_keys = [key_a, key_b, key_c, key_d]

all_accidents = [sink]

# define which items/rooms are related
# possibly this is not done. Will see when we run code

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "outside": [door_d],
    "living room": [dining_table, sink, door_d, door_c],
    "door a": [game_room, bedroom_1], #probably should be keys as well assigned
    "door b": [bedroom_1, bedroom_2], #probably should be keys as well assigned
    "door c": [bedroom_1, living_room], #probably should be keys as well assigned
    "door d": [living_room, outside], #probably should be keys as well assigned
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "dining table": [],
    "couch": [],
    "sink": [],
}