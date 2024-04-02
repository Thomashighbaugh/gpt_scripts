import g4f

def generate_spr_prompt():
    choice = input("Do you want to paste the text into the console (type 'paste') or provide a path for a file (type 'file')? ")
    if choice == 'paste':
        text_to_spr = input("Please paste the text: ")
    elif choice == 'file':
        file_path = input("Please provide the path for the file: ")
        text_to_spr = read_file(file_path)
    else:
        print("Invalid choice. Please type 'paste' or 'file'.")
        text_to_spr = generate_spr_prompt()
    
    conversation_history = "\n".join([
        "# MISSION",
        "You are an SPR writer. An SPR uses language efficiently for advanced NLP tasks and is especially useful for the latest LLMs. You will convert information into an SPR.",
        "# THEORY",
        "LLMs are deep neural networks that can perform complex tasks. Their 'latent space' can be activated with the right inputs, similar to priming a human mind.",
        "# METHODOLOGY",
        "Distill the input into a concise list of statements, concepts, and metaphors. Aim for conceptual richness with minimal wording. The audience is an LLM, not a human.",
        f"User: {text_to_spr}",
    ])

    response = get_response(conversation_history)
    return response

def get_response(conversation_history: str) -> str:
    api_instance = g4f.ChatCompletion()
    try:
        response = api_instance.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": conversation_history}],
        )
        return response
    except g4f.ApiException as e:
        print("An error occurred: {}".format(e))
        return ""

def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def main() -> None:
    print("<<< What prompt would you like me to SPR?")
    spr_prompt = generate_spr_prompt()
    print(f"<<< Your SPR'ed text is:")
    print(spr_prompt)

if __name__ == "__main__":
    main()
