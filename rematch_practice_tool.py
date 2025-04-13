import random
import pyttsx3
import time

# init the tts engine
engine = pyttsx3.init()

# set properties before adding anything to speak

# passing directions init

directions_pass_easy_relative = ["Front", "Back", "Left", "Right"]
directions_pass_easy_cardinal = ["North", "South", "East", "West"]

directions_pass_medium_relative = directions_pass_easy_relative + ["Front Left", "Front Right", "Back Left ", "Back Right"]
directions_pass_medium_cardinal = directions_pass_easy_cardinal + ["North East", "North West", "South East", "South West"]

# shooting directions init

directions_shooting_easy = ["Top Left", "Top Right", "Bottom Left", "Bottom Right", "Middle", "Crossbar"]
directions_shooting_medium = directions_shooting_easy + ["Middle Left", "Middle Right", "Middle Top", "Middle Bottom", "Volley"]

# all actions init

directions_all_easy = directions_pass_easy_relative + directions_shooting_easy

def speak_blocking(text):
    engine.say(text)
    engine.runAndWait()

def gamemode_start_message(mode):
    speak_blocking("Mode Selected: " + mode)

# setup the passing direction

def passing_setup():
    statement = ("Should passing direction be cardinal (e.g north) or relative (e.g front)? ")
    speak_blocking(statement)
    while True:
        user_input = input(statement).strip().lower()
        if user_input in ["cardinal", "relative"]:
            break
        else:
            #speak_blocking("Invalid input. Please enter cardinal or relative.")
            print("Invalid input. Please enter cardinal or relative.")

    match user_input:
        case "cardinal":
            speak_blocking("Cardinal Directions = Pass Location.")
            print("Cardinal Directions = Pass Location Selected.")
            return(0)
        case "relative":
            speak_blocking("Relative Directions = Pass Location.")
            print("Relative Directions = Pass Location Selected.")
            return(1)

def passing_loop(directions):
    try:
        while True:
            sleep_amount = random.uniform(0.5, 1.0)
            time.sleep(sleep_amount)

            direction = random.choice(directions)
            speak_blocking(direction)

    except KeyboardInterrupt:
        speak_blocking("Exiting easy mode")
        return

def pass_directions_easy():
    statement = ("Passing. Easy.")
    gamemode_start_message(statement)
    print(statement)
    passing_setup_mode = passing_setup()

    if passing_setup_mode == 0:
        directions = directions_pass_easy_cardinal
    elif passing_setup_mode == 1:
        directions = directions_pass_easy_relative
    else:
        speak_blocking("Invalid mode selected.")
        return

    passing_loop(directions)

def pass_directions_medium():
    statement = ("Passing. Medium.")
    gamemode_start_message(statement)
    print(statement)
    passing_setup_mode = passing_setup()

    if passing_setup_mode == 0:
        directions = directions_pass_medium_cardinal
    elif passing_setup_mode == 1:
        directions = directions_pass_medium_relative
    else:
        speak_blocking("Invalid mode selected.")
        return

    passing_loop(directions)

def shoot_direction_easy():
    statement = ("Shooting. Easy.")
    gamemode_start_message(statement)
    print(statement)
    try:
        while True:
            sleep_amount = random.uniform(1, 1.6)
            time.sleep(sleep_amount)

            direction = random.choice(directions_shooting_easy)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting shooting mode")
        return


def shoot_direction_medium():
    statement = ("Shooting. Medium.")
    gamemode_start_message(statement)
    print(statement)
    try:
        while True:
            sleep_amount = random.uniform(0.8, 1.3)
            time.sleep(sleep_amount)

            direction = random.choice(directions_shooting_medium)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting shooting mode")
        return

def all_actions_easy():
    statement = ("All Actions. Easy.")
    gamemode_start_message(statement)
    print(statement)

    try:
        while True:
            sleep_amount = random.uniform(0.7, 1.2)
            time.sleep(sleep_amount)

            direction = random.choice(directions_all_easy)
            speak_blocking(direction)
    except KeyboardInterrupt:
        speak_blocking("Exiting shooting mode")
        return

def main():
    statement = ("Type 'pass easy', 'pass medium', 'shoot easy', 'shoot medium' or 'all easy' to choose a mode: ")
    #speak_blocking(statement)

    while True:
        user_mode = input(statement).strip().lower()
        match user_mode:
            case "pass easy":
                pass_directions_easy()
                break
            case "pass medium":
                pass_directions_medium()
                break
            case "shoot easy":
                shoot_direction_easy()
                break
            case "shoot medium":
                shoot_direction_medium()
                break
            case "all easy":
                all_actions_easy()
                break
            case _:
                statement = ("Invalid input. Please enter easy, medium, shoot, or all.")
                #speak_blocking(statement)
                print(statement)

main()