#Stop Event
def play_room(room):
    """
    Play a room. Check if it's the target room or if the game is over.
    """
    global stop_event
    if game_state.get("game_over", False):  # Check if the game is over
        print("Game over! You can't continue.")
        return  # Exit the function to prevent further gameplay