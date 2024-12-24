# utils/menu_utils.py
# llm_tui/utils/menu_utils.py

def display_menu(options):
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    while True:
        try:
            choice = input("Enter your choice: ")
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(options):
                return choice_index
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_user_input(prompt):
    while True:
        user_input = input(f"{prompt}: ")
        if user_input.strip():
            return user_input
        else:
            print("Input cannot be empty. Please try again.")
