import random
import pyttsx3
import time
import keyboard

# init the tts engine
engine = pyttsx3.init()

# set properties before adding anything to speak

# passing directions init

directions_pass_easy_relative = ["Front", "Back", "Left", "Right"]
directions_pass_easy_cardinal = ["North", "South", "East", "West"]

directions_pass_medium_relative = directions_pass_easy_relative + ["Front Left", "Front Right", "Back Left ", "Back Right"]
directions_pass_medium_cardinal = directions_pass_easy_cardinal + ["North East", "North West", "South East", "South West"]

# shooting directions init

directions_shooting_easy = ["Top Left", "Top Right", "Bottom Left", "Bottom Right", "Middle"]
directions_shooting_medium = directions_shooting_easy + ["Volley", "Crossbar"]
directions_shooting_hard = directions_shooting_medium + ["Middle Top", "Middle Bottom", "Middle Left", "Middle Right"]

# all actions init

directions_all_easy_relative = directions_pass_easy_relative + directions_shooting_easy
directions_all_easy_cardinal = directions_pass_easy_cardinal + directions_shooting_easy

def speak_blocking(text):
    engine.say(text)
    engine.runAndWait()

def gamemode_start_message(mode):
    speak_blocking("Mode Selected: " + mode)

# setup the passing direction version cardinal or relative

def passing_setup():
    statement = ("Should passing direction be cardinal (e.g. north) or relative (e.g. front)? ")
    #speak_blocking(statement)
    while True:
        user_input = input(statement).strip().lower()
        if user_input in ["cardinal", "relative"]:
            break
        else:
            print("Invalid input. Please enter cardinal or relative.")

    match user_input:
        case "cardinal":
            speak_blocking("Cardinal Directions Selected.")
            print("Cardinal Directions Selected.")
            return(0)
        case "relative":
            speak_blocking("Relative Directions Selected.")
            print("Relative Directions Selected.")
            return(1)

# run_mode_with_setup
def run_mode_with_setup(statement, cardinal_directions_path, relative_directions_path, needs_passing_setup):
    if needs_passing_setup:
        passing_setup_mode = passing_setup()
        if passing_setup_mode == 0:
            directions =  cardinal_directions_path
        elif passing_setup_mode == 1:
            directions = relative_directions_path
        else:
            speak_blocking("Invalid mode selected.")
            return
    else:
        directions = relative_directions_path
    gamemode_start_message(statement)
    print(statement)


    direction_loop(directions)

# main loop for all the modes

def direction_loop(directions):
    try:
        while True:
            sleep_amount = random.uniform(0.5, 1.0)
            time.sleep(sleep_amount)

            direction = random.choice(directions)
            speak_blocking(direction)

    except KeyboardInterrupt:
        speak_blocking("Returning to main menu")
        print("Returning to main menu")
        return

def pass_directions_easy():
    run_mode_with_setup("Passing. Easy.", directions_pass_easy_cardinal, directions_pass_easy_relative, True)

def pass_directions_medium():
    run_mode_with_setup("Passing. Medium.", directions_pass_medium_cardinal, directions_pass_medium_relative, True)

def shoot_directions_easy():
    run_mode_with_setup("Shooting. Easy.", directions_shooting_easy, directions_shooting_easy, False)

def shoot_directions_medium():
    run_mode_with_setup("Shooting. Medium.", directions_shooting_medium, directions_shooting_medium, False)

def all_actions_easy():
    run_mode_with_setup("All Actions. Easy.", directions_all_easy_cardinal, directions_all_easy_relative, True)

def main():
    print("======= REMATCH PRACTICE TOOL =======")
    program_running = True

    while program_running:
        try:
            statement = ("Type 'pass easy', 'pass medium', 'shoot easy', 'shoot medium', 'all easy', or 'exit' to choose a mode: ")
            user_mode = input(statement).strip().lower()

            match user_mode:
                case "pass easy":
                    pass_directions_easy()
                case "pass medium":
                    pass_directions_medium()
                case "shoot easy":
                    shoot_directions_easy()
                case "shoot medium":
                    shoot_directions_medium()
                case "all easy":
                    all_actions_easy()
                case "exit":
                    speak_blocking("Exiting program")
                    program_running = False
                case _:
                    statement = ("Invalid input. Please enter pass easy, pass medium, shoot easy, shoot medium, all easy, or exit.")
                    print(statement)

        except KeyboardInterrupt:
            speak_blocking("Exiting program")
            break

if __name__ == "__main__":
    main()