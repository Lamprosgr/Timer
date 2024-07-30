import time
import sys

def countdown_timer(minutes):
    total_seconds = minutes * 60
    
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer = f'{mins:02}:{secs:02}'
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    
    print("Time's up! Task completed.")

# Example usage:
timer = int(input("How many minutes"))
countdown_timer(timer)  
