# GPT Scripts

This repository contains GPT-3-Turbo scripts that utilize various prompts to provide specific interaction patterns with GPT-3 from your local terminal (command line).

## Rebased Using GPT4Free

My trial for OpenAI's API ran out, I am poor and yet using the ChatGPT interface, or any alternative I have explored, to do a lot of these tasks is painful (but shout out to FlowGPT where I have many of my prompts located for ease of demonstration).

Luckily, GPT4Free exists (still) and it enables one to query the API of various implementations of GPT-3-turbo and GPT-4 for free. After all if the implementation as it is is free, you aren't exactly stealing anything and Bing by Microsoft can probably more than easily afford a small group of people's token costs as it mines metadata to sell out of it anyway.

With GPT4Free, I am not able to return to working with AI using Python scripts instead of waiting for FlowGPT to load and generate most of what I have AI do for me. This has meant reworking the API call of these scripts (or using the < 1.0.0 version of the pip `openai` package and setting an extra variable in the script with some other annoyances that I opted not to do), which now has been completed for all of the scripts in this repository and they have been tested to ibsure they at least work (optimally, no. Adjustments needed for longer content generation, mostly swapping the model to GPT-3-turbo which has more than just Bing as a potential generator) and I will begin pulling my prompts from FlowGPT to populate this repository for some more mature and substantial scripts in the near future.

## Scripts Available

| Script                    | Functionality Provided                                                                                                           |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| bash_oneliner             | outputs a bash one-liner to achieve a specific task, great for git and ffmpeg commands                                           |
| blog_article              | writes an informative blog article on a provided topic                                                                           |
| chatbot.py                | a basic chatbot provided with the conversation's history for additional context                                                  |
| coverletter.py            | takes a job description and your resume then outputs a coverletter                                                               |
| g4f_check                 | outputs gpt4free models and provider status                                                                                      |
| gpt_prompt_generator.py   | Provided a topic, it generates a better prompt for GPT based models with additional questions to help further improve the prompt |
| image_prompt_generator.py | Provided a topic, it generates a Stable Diffusion prompt                                                                         |
| improve_code.py           | provided a path, it will optimize python code and save it(warning: destructive)                                                  |
| therapist.py              | Using conversation history for context, this provides therapist like interaction from GPT-3                                      |
| tutorial_writer.py        | Writes a tutorial on a given technical topic                                                                                     |

## Bootstrapping Your Environment

[Bootstrapping Documentation](/docs/bootstrap.md)
