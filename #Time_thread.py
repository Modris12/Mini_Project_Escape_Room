
        # Time thread

import threading
import time

stop_event = threading.Event()
        
def start_timer(seconds, stop_event):        
    print(f"Timer started: {seconds} seconds remaining.")
    while seconds > 0 and not stop_event.is_set():
        minutes, secs = divmod(seconds, 60)
        timer = f"{minutes:02d}:{secs:02d}"
        print(timer, end="\r", flush=True)
        time.sleep(1)
        seconds -= 1

    if not stop_event.is_set():  # Timer expired
        print("\nTime's up! The room is now flooded. Life over.")
        exit()
        game_state["game_over"] = True  # Mark game as over
        stop_event.set()  # Trigger stop event to stop the game completely