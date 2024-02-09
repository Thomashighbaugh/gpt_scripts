import g4f

def generate_cover_letter(job_description, resume):
    # Create a conversation history string
    conversation_history = "\n".join(['I want you to act as a cover letter writer. I will provide you with information about the job that I am applying for and my relevant skills and experience, and you will use this information to create a professional and effective cover letter while considering the following rules: - You should use appropriate formatting and layout to make the cover letter visually appealing and easy to read. - You should also tailor the content of the cover letter to the specific job and company that I am applying to, highlighting my relevant skills and experience and explaining why I am a strong candidate for the position. - Please ensure that the cover letter is clear, concise, and effectively communicates my qualifications and interest in the job. - The cover letter should also open strong and and convey enthusiasm. - Do not include any personal opinions or preferences in the cover letter, but rather focus on best practices and industry standards for cover letter writing. - Please start the cover letter with a question that calls the attention of the hiring manager. - You must take the following into consider and must apply it to your completion When it comes to writing content, two factors are crucial, “perplexity” and “burstiness.” Perplexity measures the complexity of text. Separately, burstiness compares the variations of sentences. Humans tend to write with greater burstiness, for example, with some longer or complex sentences alongside shorter ones. AI sentences tend to be more uniform. Therefore, when writing the following content I am going to ask you to create, I need it to have a good amount of perplexity and burstiness. Generate a tailored cover letter based on the given job description and resume.',
                                       f'User: Job description: {job_description}',
                                       f'User: Resume: {resume}'])

    # Get the response from the model
    response = get_response(conversation_history)

    return response

def get_response(conversation_history: str) -> str:
    api_instance = g4f.ChatCompletion()
    try:
        # Call the API with the specified parameters
        response = api_instance.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": conversation_history}
            ])
        
        # Return the generated response
        return response.choices[0]['message']['content'].strip()
    except g4f.ApiException as e:
        print("An error occurred: {}".format(e))
        return ''

def main() -> None:
    print("Enter the job description:")
    job_description = input(">>> ")
    print("Paste your resume (plain text):")
    resume = input(">>> ")
    cover_letter = generate_cover_letter(job_description, resume)

    # Save the cover letter as a txt file
    with open("cover_letter.txt", "w") as cover_letter_file:
        cover_letter_file.write(cover_letter)

    print("\nGenerated Cover Letter saved in 'cover_letter.txt'")

if __name__ == "__main__":
    main()
