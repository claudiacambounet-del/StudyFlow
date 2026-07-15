import time
from progress import progress_bar_with_countdown


def pomodoro():
    print("Starting Pomodoro timer...")
    work_time = 25 * 60 
    break_time = 5 * 60
    
    print("Focus time! 25 minutes.")
    progress_bar_with_countdown(work_time)



    print("Break time! You get 5 minutes to relax!")
    progress_bar_with_countdown(break_time)
        

