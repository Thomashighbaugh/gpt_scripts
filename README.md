# GPT Scripts

A terminal-based user interface for interacting with local Ollama language models. Evolved from my original python scripts for interacting with OpenAI, then G4F & now Ollama. 

## Overview

This project provides a text-based menu-driven interface to access various functionalities powered by large language models (LLMs) through Ollama. It allows users to easily generate code, optimize prompts, create job hunting materials, and produce different types of written content, all from the comfort of their terminal.

You will have to have your own models downloaded with a functional Ollama setup first,of course. 

## Features

-   **Dynamic Model Loading**: Automatically detects and loads available Ollama models.
-   **Categorized Functionality**: Features are grouped into logical categories: Coding, Prompting, Job Hunting, and Writing.
-   **Individual Scripts**: Each LLM-powered function is contained in its own script file within its category, promoting modularity and maintainability.
-   **Common Utility Functions**: Commonly used functions are placed in the `utils` directory for easy access by different parts of the project.
-   **User Input Prompts**: Uses clear prompts to guide users through each function.
-   **Output Display & Saving**: Displays LLM outputs to the terminal, with options to save responses to files.

## Categories and Functionalities

### Coding
-   **Code Generation**: Generate code snippets based on user-defined descriptions.
-   **Code Explanation**: Get explanations for provided code snippets.
-   **Code Optimization**: Optimize existing code snippets for better performance or readability.
-   **Bash One-Liner Generation**: Generate bash one-liner commands based on a description.

### Prompting
-   **Prompt Generation**: Generate prompts based on user input.
-   **Prompt Optimization**: Optimize existing prompts to achieve better results.
-   **Image Prompt Generation**: Create prompts for image generation models based on user descriptions.
-   **Image Prompt Optimization**: Optimize image generation prompts.

### Job Hunting
-   **Cover Letter Generation**: Generate cover letters based on user inputs such as job descriptions and experience.
-   **Resume Optimization**: Optimize existing resume text.
-   **Interview Question Generation**: Generate relevant interview questions based on the role and company.

### Writing
-   **Twitter Post About Article**: Create a tweet about a given article.
-   **LinkedIn Post About Article**: Create a LinkedIn post about a given article.
-   **Technical Blog Post Outline & Writing**: Generate a blog post outline, and then expand it into a full blog post on a technical topic.
-   **Technical Tutorial Outline & Writing**: Generate a tutorial outline, and then expand it into a full tutorial on a technical topic.

## Installation

1.  **Install Ollama**: Ensure that you have Ollama installed and running on your system. Follow the instructions on the [Ollama website](https://ollama.com/).
2.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Thomashighbaugh/gpt-scripts
    cd gpt-scripts
    ```
3.  **Create a Virtual Environment (Recommended)**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
    ```
4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Application**:
    ```bash
    python main.py
    ```
2.  **Follow the Prompts**: The application will display a series of menus. Use the number keys to make your selection.
3.  **Enter Input**: When prompted, enter the required input, such as code snippets, descriptions, or text for writing tasks.
4.  **View Output**: The output will be displayed in the terminal, with an option to save the results to a file.

## File Structure

```
llm_tui/
├── main.py               # Main entry point for the application
├── utils/
│   ├── __init__.py
│   ├── ollama_utils.py   # Functions for interacting with Ollama
│   ├── menu_utils.py     # Functions for displaying menus and getting input
│   └── display_utils.py  # Functions for displaying and saving output
├── coding/
│   ├── __init__.py
│   ├── code_generation.py     # Generate code snippets
│   ├── code_explanation.py    # Explain code snippets
│   ├── code_optimization.py   # Optimize code snippets
│   └── bash_one_liner_generation.py # Generates bash one-liners
├── prompting/
│   ├── __init__.py
│   ├── prompt_generation.py    # Generate prompts
│   ├── prompt_optimization.py  # Optimize prompts
│   ├── image_prompt_generation.py # Generate image prompts
│   └── image_prompt_optimization.py # Optimize image prompts
├── job_hunting/
│   ├── __init__.py
│   ├── cover_letter_generation.py # Generate cover letters
│   ├── resume_optimization.py    # Optimize resume text
│   └── interview_question_generation.py # Generate interview questions
├── writing/
│   ├── __init__.py
│   ├── twitter_post_about_article.py # Generate twitter posts about articles
│   ├── linkedin_post_about_article.py # Generate linkedin posts about articles
│   ├── technical_blog_post_outline_writing.py # Generate technical blog posts
│   └── technical_tutorial_outline_writing.py # Generate technical tutorials
```

## Contributing

Feel free to contribute by submitting issues or pull requests. If you have ideas for new features or improvements, please share them with me!
