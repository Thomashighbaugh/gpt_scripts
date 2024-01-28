# GPT Scripts

This repository contains GPT-3 scripts that utilize various prompts to provide specific interaction patterns with GPT-3 from your local terminal (command line).

## Rebased Using GPT4Free

My trial for OpenAI's API ran out, I am poor and yet using the ChatGPT interface, or any alternative I have explored, to do a lot of these tasks is painful (but shout out to FlowGPT where I have many of my prompts located for ease of demonstration).

Luckily, GPT4Free exists (still) and it enables one to query the API of various implementations of GPT-3-turbo and GPT-4 for free. After all if the implementation as it is is free, you aren't exactly stealing anything and Bing by Microsoft can probably more than easily afford a small group of people's token costs as it mines metadata to sell out of it anyway.

With GPT4Free, I am not able to return to working with AI using Python scripts instead of waiting for FlowGPT to load and generate most of what I have AI do for me. This has meant reworking the API call of these scripts (or using the < 1.0.0 version of the pip `openai` package and setting an extra variable in the script with some other annoyances that I opted not to do), which now has been completed for all of the scripts in this repository and they have been tested to ibsure they at least work (optimally, no. Adjustments needed for longer content generation, mostly swapping the model to GPT-3-turbo which has more than just Bing as a potential generator) and I will begin pulling my prompts from FlowGPT to populate this repository for some more mature and substantial scripts in the near future.

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
./bin/start.sh
# or
bash bin/start.bash
# or
zsh bin/start.zsh
```

This will take care of the following prerequisite steps:

- setting up virtual environment with `python -m venv`
- sourcing the virtual environment
- installing the dependencies listed in `requirements.txt`
