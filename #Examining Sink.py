#Examining Sink
for item in object_relations[current_room["name"]]:
        if item["name"] == item_name:
            # Handle accidents like sink flooding only for the sink
            if item["type"] == "accident" and item_name == "sink":
                if not game_state.get("timer_running", False):
                    print("You broke the sink and the room is starting to flood rapidly. You have only 2 minutes until the room is full of water and you won't be able to get out.  RUN!!!")
                    specific_time = 120
                    game_state["timer_running"] = True
                    threading.Thread(target=start_timer, args=(specific_time, stop_event)).start()
                return play_room(current_room)