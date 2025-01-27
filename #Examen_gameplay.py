#Examen.gameplay

for item in object_relations[current_room["name"]]:        
        if item["name"] == item_name:
            output = "You examine " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if have_key:
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    if item["type"] == "furniture":
                        output += "There isn't anything interesting about it."
            print(output)
            break    

    if output is None:
        print("The item you requested is not found in the current room.")
    
    if next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes':
        play_room(next_room)
    else:
        play_room(current_room)