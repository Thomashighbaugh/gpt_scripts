# utils/display_utils.py
import os

def display_output(output, save_path=None):
    print("\n--- Output ---\n")
    print(output)
    print("\n--- End Output ---\n")

    if save_path:
      while True:
        save_choice = input("Do you want to save the output to a file? (yes/no): ").lower()
        if save_choice == "yes":
            while True:
                file_path = input(f"Enter the full path to save the file (or press Enter to use default {save_path}): ").strip()
                if not file_path:
                    file_path = save_path
                try:
                  with open(file_path, 'w') as f:
                      f.write(output)
                  print(f"Output saved to {file_path}")
                  return
                except Exception as e:
                    print(f"Error saving file: {e}. Please try again.")

        elif save_choice == "no":
           return
        else:
          print("Invalid input. Please enter 'yes' or 'no'.")
