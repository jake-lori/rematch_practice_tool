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
directions_all_medium_relative = directions_pass_medium_relative + directions_shooting_medium
directions_all_medium_cardinal = directions_pass_medium_cardinal + directions_shooting_medium

# called whenever the program needs to speak
def speak_blocking(text):
    engine.say(text)
    engine.runAndWait()

# called whenever the program starts a new mode
def gamemode_start_message(mode):
    speak_blocking("Mode Selected: " + mode)

# setup the passing direction version. cardinal or relative. used for passing and all actions.
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

# runs the mode with the initial statement and the directions.
# if needs_passing_setup is true, it will run the passing setup function to determine which directions to use.
def run_mode_with_setup(statement, cardinal_directions_path, relative_directions_path, needs_passing_setup, min_time, max_time):
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

    direction_loop(directions, min_time, max_time)

# main loop for all the modes. it will randomly select a direction from the list and speak it after a delay.
def direction_loop(directions, min_time, max_time):
    try:
        while True:
            sleep_amount = random.uniform(min_time, max_time)
            time.sleep(sleep_amount)

            direction = random.choice(directions)
            speak_blocking(direction)

    except KeyboardInterrupt:
        speak_blocking("Returning to main menu")
        print("Returning to main menu")
        return


# functions for each mode. they will call the run_mode_with_setup function with if it needs a direction check and the minimum and maximum time intervals.
# min_time = minimum_time from main()
# max_time = maximum_time from main
def pass_directions_easy(min_time, max_time):
    run_mode_with_setup("Passing. Easy.", directions_pass_easy_cardinal, directions_pass_easy_relative, True, min_time, max_time)

def pass_directions_medium(min_time, max_time):
    run_mode_with_setup("Passing. Medium.", directions_pass_medium_cardinal, directions_pass_medium_relative, True, min_time, max_time)

def shoot_directions_easy(min_time, max_time):
    run_mode_with_setup("Shooting. Easy.", directions_shooting_easy, directions_shooting_easy, False, min_time, max_time)

def shoot_directions_medium(min_time, max_time):
    run_mode_with_setup("Shooting. Medium.", directions_shooting_medium, directions_shooting_medium, False, min_time, max_time)

def all_actions_easy(min_time, max_time):
    run_mode_with_setup("All Actions. Easy.", directions_all_easy_cardinal, directions_all_easy_relative, True, min_time, max_time)

# Get time range from user (or skip if not needed)
def get_time_range(needs_timing):
    if not needs_timing:
        return None, None

    try:
        minimum_time = input("What is the minimum time between directions? (e.g. 0.5) ").strip()
        minimum_time = float(minimum_time)
        if minimum_time < 0.1:
            print("Minimum time must be at least 0.1 seconds.")
            return get_time_range(True)
        else:
            print("Minimum time set to", minimum_time, "seconds.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_time_range(True)

    try:
        maximum_time = input("What is the maximum time between directions? (e.g. 1.2) ").strip()
        maximum_time = float(maximum_time)
        if maximum_time < 0.1:
            print("Maximum time must be at least 0.1 seconds.")
            return get_time_range(True)
        elif maximum_time < minimum_time:
            print("Maximum time must be greater than minimum time.")
            return get_time_range(True)
        else:
            print("Maximum time set to", maximum_time, "seconds.")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_time_range(True)

    return minimum_time, maximum_time

# main function to run the program. it will ask the user for input and run the requested mode.
def main():
    print("======= REMATCH PRACTICE TOOL =======")
    program_running = True

    while program_running:
        try:
            user_mode = input(
                "Type 'pass easy', 'pass medium', 'shoot easy', 'shoot medium', 'all easy', or 'exit' to choose a mode: "
            ).strip().lower()

            # calls function to get the timing intervals for the TTS only if a mode requires it
            if user_mode in ["pass easy", "pass medium", "shoot easy", "shoot medium", "all easy"]:
                minimum_time, maximum_time = get_time_range(needs_timing=True)
            else:
                minimum_time = maximum_time = None

            match user_mode:
                case "pass easy":
                    pass_directions_easy(minimum_time, maximum_time)
                case "pass medium":
                    pass_directions_medium(minimum_time, maximum_time)
                case "shoot easy":
                    shoot_directions_easy(minimum_time, maximum_time)
                case "shoot medium":
                    shoot_directions_medium(minimum_time, maximum_time)
                case "all easy":
                    all_actions_easy(minimum_time, maximum_time)
                case "exit":
                    speak_blocking("Exiting program")
                    program_running = False
                case _:
                    print("Invalid input. Please enter pass easy, pass medium, shoot easy, shoot medium, all easy, or exit.")

        except KeyboardInterrupt:
            speak_blocking("Exiting program")
            break


if __name__ == "__main__":
    main()