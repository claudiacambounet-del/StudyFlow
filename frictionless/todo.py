import json
from  colorama import Fore, Style

PASTEL = {
    "done": Fore.LIGHTGREEN_EX + Style.BRIGHT,
    "todo": Fore.LIGHTRED_EX + Style.BRIGHT,
    "category": Fore.LIGHTBLUE_EX,
    "title": Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
    "reset": Style.RESET_ALL
}

def load_tasks():
    with open("data/tasks.json", "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open("data/tasks.json", "w") as f:
        json.dump(tasks, f , indent=4)


def add_task(name, priority, time_minutes, category = 'general'):
    tasks = load_tasks()
    tasks.append({
        "name": name,
        "priority": priority,
        "time": time_minutes,
        "category": category,
        "done": False  
    })
    save_tasks(tasks)
    print(f"'{name}' task was added in the '{category}' category.")

def list_tasks():
    tasks = load_tasks()
    print(PASTEL["title"] + "\n Your Tasks \n" + PASTEL["reset"])
    for t in tasks:
        status = PASTEL["done"] + "[Done]" if t["done"] else PASTEL["todo"] + "[Todo]"
        print(
            f"{status}{PASTEL['reset']}"
            f"{t['name']} - {t['time']} min - priority {t['priority']} - "
            f"{PASTEL['category']}{t.get('category', 'general')}{PASTEL['reset']}"
           
        )

def plan_session(minutes):
    tasks = load_tasks()
    tasks_sorted = sorted(tasks, key=lambda x:(-x["priority"], x["time"]))
    plan = []
    total = 0
    for t in tasks_sorted:
        if total + t["time"] <= minutes:
            plan.append(t)
            total += t["time"]

    print(f"Your {minutes}-minute study plan:")
    for t in plan:
        print(f"- {t['name']} ({t['time']} min)")

    return plan

def mark_done(name):
    tasks = load_tasks()
    found = False

    for t in tasks:
        if t["name"].lower() == name.lower():
            t['done'] = True
            found = True
            break
    if found:
        save_tasks(tasks)
        print(f"Task '{name}' is done!")
    else:
        print(f"Task '{name}' not found.")    


def delete_task(name):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["name"].lower() != name.lower()] 
    save_tasks(new_tasks)
    print(f"Deleted task '{name}'.")       

def clear_all():
    save_tasks([])
    print("All tasks are gone!")

def clear_done():
    tasks = load_tasks()
    tasks = [t for t in tasks if not t["done"]]
    save_tasks(tasks)
    print("All completed tasks are gone!")      
