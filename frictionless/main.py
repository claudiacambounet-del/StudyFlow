import sys
from routines import run_routine
from todo import add_task, list_tasks, plan_session, mark_done, clear_done, delete_task, clear_all
from reminders import start_reminders, add_reminder
from pomodoro import pomodoro
from colorama import Fore, Style
import datetime
from progress import progress_bar_with_countdown

def show_greeting():
    hour = datetime.datetime.now().hour

    if hour < 12:
        greeting = "Good morning, welcome to StudyFlow!"
    elif hour < 19:
        greeting = "Good afternoon, welcome to StudyFlow!"
    else:
        greeting = "Good evening, welcome to StudyFlow!"

    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + greeting + Style.RESET_ALL)
  
def show_help():
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + " Commands " + Style.RESET_ALL)
    print("routine <name>           - Run a predefined study routine")
    print("add-task <name> <priority> <time_minutes> [category]")
    print("                        - Add a new task")
    print("list-tasks              - Show all tasks")
    print("done <name>             - Mark a task as done")
    print("delete-task <name>      - Delete a task")
    print("clear-done              - Remove all completed tasks")
    print("clear-all               - Remove all tasks")
    print("plan <minutes>          - Plan a study session")
    print("pomodoro                - Start a Pomodoro timer")
    print("add-reminder <HH:MM> <message>")
    print("                        - Add a reminder")
    print("reminders               - Start checking reminders")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_greeting()
        show_help()
        sys.exit(0)

    command = sys.argv[1]

    if command == 'routine':
        run_routine(sys.argv[2])

    elif command == 'add-task':
        name = sys.argv[2]
        priority = int(sys.argv[3])
        time_minutes = int(sys.argv[4])
        category = sys.argv[5] if len(sys.argv) > 5 else 'general'
        add_task(name, priority, time_minutes, category)

    elif command == 'plan':
        minutes = int(sys.argv[2])
        plan_session(minutes)

    elif command == "add-reminder":
        time_str = sys.argv[2]
        message = ' '.join(sys.argv[3:])
        add_reminder(time_str, message)

    elif command == "reminders":
        start_reminders()

    elif command == "done":
        task_name = ' '.join(sys.argv[2:])
        mark_done(task_name)

    elif command == "clear-done":
        clear_done()

    elif command == "list-tasks":
        list_tasks()

    elif command == 'delete-task':
        task_name = " ".join(sys.argv[2:])
        delete_task(task_name)

    elif command == "clear-all":
        clear_all()

    elif command == "pomodoro":
        pomodoro()

    else:
        show_help()
             
