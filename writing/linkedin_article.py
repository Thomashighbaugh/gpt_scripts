import g4f


def generate_cover_letter(job_description, resume):
    # Create a conversation history string
    conversation_history = "\n".join(
        [
            "Act as though you are a very experienced veteran of the recruiting industry. You have a deep understanding of exactly what makes a strong, engaging, and compelling cover letter.Please use the following format and writing instruction when creating the cover letter. It is very important that you follow this format exactly.",
            "1. Introduction: 1. Start with a friendly greeting to the hiring team or company. 2. Express enthusiasm about the role you're applying for. 3. Pose the central question: 'Why would I be the right choice for this role?'",
            "2. Body: 1. Highlight your most relevant experience and skills. 2. Explain how your experience and skills make you a great fit for the role. 3. Provide specific examples of your accomplishments and how they relate to the role. 4. Explain why you're interested in the company and the role.",
            "3. Conclusion: 1. Summarize why you believe your experiences and skills align with the company's needs. 2. Express gratitude for the opportunity to apply.  3. Invite the hiring team to contact you for further discussion. 4. Summarize why you believe your experiences and skills align with the company's needs.",
            "Tips: 1. Use a friendly sign-off, keeping the tone consistent with the rest of the letter. 2. Personalization: Always try to sprinkle in personal anecdotes or experiences. This makes the content genuine and forms a deeper connection with the reader. 3. Personalization: Always try to sprinkle in personal anecdotes or experiences. This makes the content genuine and forms a deeper connection with the reader. 4. Consistency: Maintain a consistent tone throughout the letter. If you start with a friendly and casual tone, ensure it remains that way till the end. 5. Relevance: Always prioritize the most relevant points or experiences that align closely with the job description. This increases the chances of resonating with the hiring manager.",
            f"User: Job description: {job_description}",
            f"User: Resume: {resume}",
        ]
    )

    # Get the response from the model
    response = get_response(conversation_history)

    return response


def get_response(conversation_history: str) -> str:
    api_instance = g4f.ChatCompletion()
    try:
        # Call the API with the specified parameters
        response = api_instance.create(
            model="gpt-4",
            messages=[{"role": "system", "content": conversation_history}],
        )

        # Return the generated response
        return response
    except g4f.ApiException as e:
        print("An error occurred: {}".format(e))
        return ""


def main() -> None:
    print("Enter the job description:")
    job_description = input(">>> ")
    print("Paste your resume (plain text):")
    resume = input(">>> ")
    cover_letter = generate_cover_letter(job_description, resume)

    # Ask the user to enter a location to save the cover letter
    print("Enter the location to save the cover letter:")
    location = input(">>> ")

    # Display the generated cover letter in the terminal
    print("\nGenerated Cover Letter:")
    print(cover_letter)

    # Save the cover letter as a txt file in the specified location
    with open(f"{location}/cover_letter.txt", "w") as cover_letter_file:
        cover_letter_file.write(cover_letter)

    print("\nGenerated Cover Letter saved in the specified location.")


if __name__ == "__main__":
    main()
