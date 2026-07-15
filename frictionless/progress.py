import time
import sys
from colorama import Fore, Style

PASTEL = {
    "bar": Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
    "fill": Fore.LIGHTMAGENTA_EX + Style.BRIGHT,
    "text": Fore.LIGHTBLUE_EX + Style.BRIGHT,
    "reset": Style.RESET_ALL
}

def progress_bar_with_countdown(duration_seconds):
    total = duration_seconds
    bar_length = 30

    for remaining in range(total, -1, -1):
        minutes = remaining // 60
        seconds = remaining % 60
        countdown = f"{minutes:02d}:{seconds:02d}"

        percent = int(((total - remaining) / total) * 100)
        filled_length = int(bar_length * percent / 100)

        bar = (
            PASTEL["fill"] + "█" * filled_length +
            PASTEL["bar"] + " " * (bar_length - filled_length)
        )

        sys.stdout.write(
            f"\r{PASTEL['text']} {countdown}| Progress: {percent}% {PASTEL['reset']} {bar}"
        )
        sys.stdout.flush()
        time.sleep(1)

    print("\n" + PASTEL["fill"] + " Done ! " + PASTEL["reset"])    