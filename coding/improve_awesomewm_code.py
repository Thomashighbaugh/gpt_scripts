import sys
import re
from pathlib import Path

# Ensure the g4f module is in the path
sys.path.append(str(Path(__file__).parent.parent.parent))
import g4f


# Function to extract code from the AI's response
def read_code(text: str) -> str:
    if match := re.search(r"```(lua)\n(?P<code>[\S\s]+?)\n```", text):
        return match.group("code")


# Prompt the user for the path to their Lua code
path = input("Enter the path to your AwesomeWM Lua code: ")

# Read the Lua code from the file
with open(path, "r") as file:
    lua_code = file.read()

# Request improvements from the AI
print("Requesting code improvements...")
response = []
for chunk in g4f.ChatCompletion.create(
    model=g4f.models.gpt_4_32k,
    messages=[
        {
            "role": "user",
            "content": f"Refactor for performance and modularity, comprehensively document using ldoc format and generally improve the AwesomeWM Lua code in this file:\n```lua\n{lua_code}\n```",
        }
    ],
    timeout=300,
    stream=True,
):
    response.append(chunk)
    print(chunk, end="", flush=True)
print()
response = "".join(response)

# Save the improved Lua code back to the file
if improved_lua_code := read_code(response):
    with open(path, "w") as file:
        file.write(improved_lua_code)
