import sys
import re
from pathlib import Path
from os import path

# Add the grandparent of the current file's directory to sys.path to allow importing from there
sys.path.append(str(Path(__file__).parent.parent.parent))

import g4f  # Importing a custom module, assumed to be in the grandparent directory

def read_code(text: str) -> str:
    """
    Extracts and returns the Python code block from the provided text.

    Args:
    text (str): The text containing the code block.

    Returns:
    str: The extracted code block, if found; otherwise, None.
    """
    # Use regular expression to find a code block wrapped in triple backticks
    if match := re.search(r"```(python|py|)\n(?P<code>[\S\s]+?)\n```", text):
        return match.group("code")  # Return the matched code block

# Prompt the user for the path to the file containing the code to be improved
path = input("Path: ")

# Open the file at the given path and read its contents
with open(path, "r") as file:
    code = file.read()

# Construct the prompt message with rules for improving the code
prompt = f"""
Annotate the code in this file:
```py
{code}
```
Rules to Strictly Apply In Formulating Your Completion:
- Comment the file as completely as possible to aid in human readability.
- Never trunicate or otherwise remove any aspect of any code for brevity or any other purpose. 
- Add docstrings to all functions and classes.
"""

print("Create code...")
response = []

# Generate a response from the g4f model by streaming chunks of the completion
for chunk in g4f.ChatCompletion.create(
    model=g4f.models.gpt_4_turbo,
    messages=[{"role": "user", "content": prompt}],
    timeout=300,
    stream=True,
):
    response.append(chunk)  # Append each chunk to the response list
    print(chunk, end="", flush=True)  # Print each chunk as it is received

print()
response = "".join(response)  # Join all chunks into a single string

# If the response contains a code block, write it to the file at the given path
if code := read_code(response):
    with open(path, "w") as file:
        file.write(code)
