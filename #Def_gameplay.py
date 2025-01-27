#Def_gameplay
def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state ["current_room"])

import threading

    
def play_room(room):
    """
    Play a room. Check if it's the target room or if the game is over.
    """
    global stop_event
    if game_state.get("game_over", False):  # Check if the game is over
        print("Game over! You can't continue.")
        return  # Exit the function to prevent further gameplay

    game_state["current_room"] = room
    if game_state["current_room"] == game_state["target_room"]:
        print("Congrats! You escaped the room!")
        stop_event.set()  # Stop the timer
        game_state["game_over"] = True  # End the game
        return  # Exit the function to prevent further gameplay

    while not game_state.get("game_over", False):  # Loop only if the game is not over
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if game_state.get("game_over", False):  # Check after every input
            print("Game over! You can't continue.")
            return
        

        if intended_action == "explore":
            explore_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
        linebreak()

    
def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if room != current_room:
            return room
    return None
            

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None