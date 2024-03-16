import sys, re
from pathlib import Path

# Ensure the g4f module is in the path
sys.path.append(str(Path(__file__).parent.parent.parent))
import g4f

# Function to extract code from the AI's response
def read_code(text):
    if match := re.search(r"```(lua)\n(?P<code>[\S\s]+?)\n```", text):
        return match.group("code")

# Prompt the user for the path to their Lua code
path = input("Enter the path to your AwesomeWM Lua code: ")

# Read the Lua code from the file
with open(path, "r") as file:
    lua_code = file.read()


# Set up the prompt 

prompt="""
You are a world class software engineer. \n 

Improve the AwesomeWM Lua code in this file:\n```lua\n{lua_code}\n```

# Rules to Strictly Apply In Formulating Your Completion: \n

-   Don't remove anything, comment it out instead. \n
-   Please add comprehensive documentation for [file or module name], including clear and concise explanations of its purpose, design, and implementation. Consider including examples of how to use the module, as well as any relevant diagrams or flow charts to help illustrate its workings. Ensure that the documentation is easily accessible to other developers and is updated as the module evolves. Consider using documentation tools such as inline comments, markdown files, or a documentation generator to simplify the process. \n
-   Refactor the code to make it more readable, perform more effciently and be more easily maintainable. This might splitting functions into smaller pieces, or simplifying complex expressions. Ensure that the code is well-organized and follows the conventions of the language or framework being used. Please only rename locally scoped variables and nothing that is returned or the result of the function within the file. \n
-   Add your explanations for changes at the top of the file in a comment. \n 
-   Add type annotations if possible. \n
-   Don't remove license comments. \n

"""



# Request improvements from the AI
print("Requesting code improvements...")
response = []
for chunk in g4f.ChatCompletion.create(
    model=g4f.models.gpt_35_long,
    messages=[{"role": "user", "content": f"Improve the AwesomeWM Lua code in this file:\n```lua\n{lua_code}\n```"}],
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
