import random
import pyttsx3
import time

# init the tts engine
engine = pyttsx3.init()

# set properties before adding anything to speak
directions_easy = ["North", "South", "East", "West"]
directions_medium = directions_easy + ["North East", "North West", "South East ", "South West"]
directions_shooting = ["Top Left", "Top Right", "Bottom Left", "Bottom Right", "Middle Left", "Middle Right", "Middle", "Middle Top", "Middle Bottom"]
directions_all = directions_easy + directions_medium + directions_shooting + ["Flick"]

def speak_blocking(text):
    engine.say(text)
    engine.runAndWait()

def gamemode_start_message(mode):
    speak_blocking("Mode Selected: " + mode)
    speak_blocking("Cardinals Directions = Pass Location.")
    speak_blocking("Relative Directions = Shot Location.")


def pass_directions_easy():
    gamemode_start_message("Passing. Easy.")
    try:
        while True:
            sleep_amount = random.uniform(0.4, 1.0)
            time.sleep(sleep_amount)

            direction = random.choice(directions_easy)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting easy mode")
        return

def pass_directions_medium():
    gamemode_start_message("Passing. Medium.")
    try:
        while True:
            sleep_amount = random.uniform(0.3, 0.6)
            time.sleep(sleep_amount)

            direction = random.choice(directions_medium)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting medium mode")
        return

def shooting():
    gamemode_start_message("Shooting. Medium.")
    try:
        while True:
            sleep_amount = random.uniform(0.6, 0.8)
            time.sleep(sleep_amount)

            direction = random.choice(directions_shooting)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting shooting mode")
        return

def all_actions():
    gamemode_start_message("All Actions.")
    try:
        while True:
            sleep_amount = random.uniform(0.5, 0.7)
            time.sleep(sleep_amount)

            direction = random.choice(directions_all)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting shooting mode")
        return

def main():
    statement = ("Type 'easy', 'medium', 'shoot' or 'all' to choose a mode: ")
    speak_blocking(statement)

    while True:
        user_mode = input(statement).strip().lower()
        match user_mode:
            case "easy":
                pass_directions_easy()
                break
            case "medium":
                pass_directions_medium()
                break
            case "shoot":
                shooting()
                break
            case "all":
                all_actions()
                break
            case _:
                speak_blocking("Invalid input. Please enter easy, medium, shoot, or all.")

main()