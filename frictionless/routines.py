import webbrowser
import subprocess
import json
import os

def load_routines():
    with open("data/routines.json", "r") as f:
        return json.load(f)

def run_routine(name):
    routines = load_routines()
    routine = routines.get(name)

    if not routine:
        print(f"Routine '{name}' not found.")
        return

    for url in routine["urls"]:
        webbrowser.open(url)

    for app in routine["apps"]:
        subprocess.Popen(app)

    for file in routine["files"]:
        os.startfile(file)

    print(f"Routine '{name}' launched successfully!")
