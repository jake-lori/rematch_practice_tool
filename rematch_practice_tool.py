import random
import pyttsx3
import time
import keyboard

# init the tts engine
engine = pyttsx3.init()

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

# custom mode init

directions_custom = []

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
    if not needs_passing_setup:
        # passed with shooting modes.
        directions = relative_directions_path

    else:
        # passes with passing and all actions modes.
        passing_setup_mode = passing_setup()
        if passing_setup_mode == 0:
            directions =  cardinal_directions_path
        elif passing_setup_mode == 1:
            directions = relative_directions_path
        else:
            speak_blocking("Invalid mode selected.")
            return
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
# max_time = maximum_time from main()

# run_mode_with_setup(
#     mode_name: str,                      # Description of the mode and difficulty
#     cardinal_directions: list[str] | None,  # List of cardinal directions (or None if not used)
#     relative_directions: list[str] | None,  # List of relative directions (or default directions if needed)
#     needs_setup: bool,                   # Whether setup instructions should be spoken before starting
#     min_time: float,                     # Minimum time between directions (in decimal seconds)
#     max_time: float                      # Maximum time between directions (in decimal seconds)
# )

def pass_directions_easy():
    run_mode_with_setup("Passing. Easy.", directions_pass_easy_cardinal, directions_pass_easy_relative, True, 0.5, 1.2)

def pass_directions_medium():
    run_mode_with_setup("Passing. Medium.", directions_pass_medium_cardinal, directions_pass_medium_relative, True, 0.3, 0.6)

def shoot_directions_easy():
    run_mode_with_setup("Shooting. Easy.", None, directions_shooting_easy, False, 0.9, 1.2)

def shoot_directions_medium():
    run_mode_with_setup("Shooting. Medium.", None, directions_shooting_medium, False, 0.5, 0.5)

def all_actions_easy():
    run_mode_with_setup("All Actions. Easy.", directions_all_easy_cardinal, directions_all_easy_relative, True, 1, 1.5)

def custom_mode(min_time, max_time):
    run_mode_with_setup("Custom Mode.", None, directions_custom, False, min_time, max_time)

# Get time range from user (or skip if not needed)
def get_time_range():

    try:
        minimum_time = input("What is the minimum time between directions? (e.g. 0.5) ").strip()
        minimum_time = float(minimum_time)

        if minimum_time < 0.1:
            print("Minimum time must be at least 0.1 seconds.")

        else:
            print("Minimum time set to", minimum_time, "seconds.")

    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_time_range()

    try:
        maximum_time = input("What is the maximum time between directions? (e.g. 1.2) ").strip()
        maximum_time = float(maximum_time)

        if maximum_time < 0.1:
            print("Maximum time must be at least 0.1 seconds.")

        elif maximum_time < minimum_time:
            print("Maximum time must be greater than minimum time.")

        else:
            print("Maximum time set to", maximum_time, "seconds.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    return minimum_time, maximum_time

# gets the directions wanted for custom mode from the user.
def get_custom_directions():
    global directions_custom
    directions_custom = []
    print("Enter the directions you want to practice. Type 'done' when you are finished.")
    while True:
        direction = input("Enter direction: ").strip()
        if direction.lower() == "done":
            break
        elif direction:
            directions_custom.append(direction)  # Append to a single list
        else:
            print("Invalid input. Please enter a direction or 'done'.")

    if not directions_custom:
        print("No directions entered. Exiting custom mode.")
        return

    print("Custom directions added:", directions_custom)

# main function to run the program. it will ask the user for input and run the requested mode.
def main_menu():
    print("======= REMATCH PRACTICE TOOL =======")
    program_running = True

    # sets the function name for the gamemmodes
    mode_functions = {
        "pass easy": pass_directions_easy,
        "pass medium": pass_directions_medium,
        "shoot easy": shoot_directions_easy,
        "shoot medium": shoot_directions_medium,
        "all easy": all_actions_easy,
        "custom": custom_mode
    }

    # only these modes need user timing setting
    modes_need_timing = [
        custom_mode
    ]

    while program_running:
        try:
            user_selected_mode = input(
                "Type 'pass easy', 'pass medium', 'shoot easy', 'shoot medium', 'all easy', 'custom', or 'exit' to choose a mode: "
            ).strip().lower()

            if user_selected_mode == "exit":
                program_running = False
                break

            elif user_selected_mode == "custom":
                get_custom_directions()
                minimum_time, maximum_time = get_time_range()
                mode_functions[user_selected_mode](minimum_time, maximum_time)

            elif user_selected_mode in mode_functions:
                if user_selected_mode not in modes_need_timing:
                    mode_functions[user_selected_mode]()
                else:
                    # calls function to get the timing intervals only if a mode requires it
                    minimum_time, maximum_time = get_time_range()
                    mode_functions[user_selected_mode](minimum_time, maximum_time)

            else:
                print("Invalid input. Please enter pass easy, pass medium, shoot easy, shoot medium, all easy, or exit.")


        except KeyboardInterrupt:
            speak_blocking("Exiting program")
            break

def main():
    main_menu()

if __name__ == "__main__":
    main()