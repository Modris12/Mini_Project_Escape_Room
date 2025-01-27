#Initiate_game_state
INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "timer_running": False,
    "target_room": outside
}


#start game
game_state = INIT_GAME_STATE.copy()

start_game()