import json
import time
from datetime import datetime

def load_reminders():
    with open("data/reminders.json") as f:
        return json.load(f)
    
def add_reminder(time_str, message):
    reminders = load_reminders()
    reminders.append({"time": time_str, "message": message})
    with open("data/reminders.json", "w") as f:
        json.dump(reminders, f, indent = 4)
    print("Added!")

def start_reminders():
    reminders = load_reminders()
    print("Reminder system running...")

    while True:
        now = datetime.now().strftime("%H:%M")
        for r in reminders:
            if r["time"] == now:
                print(f"Reminders : {r['message']}") 
            time.sleep(60)               