# GPT Scripts

This repository contains GPT-3 scripts that utilize various prompts to provide specific interaction patterns with GPT-3 from your local terminal (command line).

## OpenAI API Key

These scripts look for an environmental variable called `OPENAI_API_KEY` thus on Linux one would need to run something like `export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxx` replacing the portion to the right of the equal sign with your API key of course.

## Scripts Available

| Script                    | Functionality Provided                                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| chatbot.py                | a basic chatbot provided with the conversation's history for additional context                                                  |
| gpt_prompt_generator.py   | Provided a topic, it generates a better prompt for GPT based models with additional questions to help further improve the prompt |
| image_prompt_generator.py | Provided a topic, it generates a Stable Diffusion prompt                                                                         |
| therapist.py              | Using conversation history for context, this provides therapist like interaction from GPT-3                                      |
| tutorial_writer.py        | Writes a tutorial on a given technical topic                                                                                     |

## Bootstrapping Your Environment

To ease the usage of the correct dependencies and streamline the creation of an isolated virtual environment, a bash script is included that will (on Linux at the very least) automatically do everything necessary except the exporting of your API key.

To run the script, enter the following command in your terminal after navigating to the location you've downloaded this repository to:

```bash
bash start.sh
```

This will take care of the following prerequisite steps:

- setting up virtual environment with `python -m venv`
- sourcing the virtual environment
- installing the dependencies listed in `requirements.txt`
