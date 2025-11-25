import time
import os
from datetime import datetime

def clear():
    os.system("cls" if os.name == "nt" else "clear")

start = datetime.now()

try:
    while True:
        now = datetime.now()
        diff = now - start

        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60

        clear()
        print("========================================")
        print("        🕒 CLI TIMER DASHBOARD")
        print("========================================")
        print(f"Start Time : {start.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Current Time : {now.strftime('%Y-%m-%d %H:%M:%S')}")
        print("----------------------------------------")
        print(f"Elapsed : {hours} hour {minutes} min {seconds} sec")
        print("========================================")
        print("Press CTRL + C to stop the timer")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nTimer stopped. Bye 👋")
