# GPT Scripts

This repository contains GPT-3-Turbo scripts that utilize various prompts to provide specific interaction patterns with GPT-3 from your local terminal (command line).

## Rebased Using GPT4Free

My trial for OpenAI's API ran out, I am poor and yet using the ChatGPT interface, or any alternative I have explored, to do a lot of these tasks is painful (but shout out to FlowGPT where I have many of my prompts located for ease of demonstration).

Luckily, GPT4Free exists (still) and it enables one to query the API of various implementations of GPT-3-turbo and GPT-4 for free. After all if the implementation as it is is free, you aren't exactly stealing anything and Bing by Microsoft can probably more than easily afford a small group of people's token costs as it mines metadata to sell out of it anyway.

With GPT4Free, I am not able to return to working with AI using Python scripts instead of waiting for FlowGPT to load and generate most of what I have AI do for me. This has meant reworking the API call of these scripts (or using the < 1.0.0 version of the pip `openai` package and setting an extra variable in the script with some other annoyances that I opted not to do), which now has been completed for all of the scripts in this repository and they have been tested to ibsure they at least work (optimally, no. Adjustments needed for longer content generation, mostly swapping the model to GPT-3-turbo which has more than just Bing as a potential generator) and I will begin pulling my prompts from FlowGPT to populate this repository for some more mature and substantial scripts in the near future.

## Scripts Available

### Categories

Scripts are broken up into functional categories, based on what the script is used to ease the process of. Those cateogories are:

| Category    | Description                                               |
| ----------- | --------------------------------------------------------- |
| coding      | Scripts that write or rewrite or otherwise deal with code |
| job_seeking | Scripts that help with finding work                       |
| misc        | Scripts that don't fit into any other category            |
| prompting   | scripts to generate or otherwise manipulate prompts       |
| writing     | Scripts that help with content creation                   |

### Scripts List

| Scripts                | Category                 | Description                                               |
| ---------------------- | ------------------------ | --------------------------------------------------------- |
| bash_oneliner          | coding                   | get a bash oneliner for specific complex BASH syntax life |
| improve_awesomewm_code | coding                   | for documenting awesome code with ldoc and improving it   |
| improve_python_code    | coding                   | for improving python code, especially these scripts       |
| -----------            | ----------------------   |
| coverletter            | job_seeking              | generate a cover letter for a job application             |
| -------------          | ---------------          |
| therapist              | misc                     | talk to a therapist                                       |
| ------------           | ------------------------ |
| chatbot                | prompting                | chat with a chatbot                                       |
| g4f_check              | prompting                | determine models and providers available                  |
| image_prompt_generator | prompting                | generate an image prompt for stable diffusion             |
| prompt_generator       | prompting                | generate a prompt for any model                           |
| ---------------        | -------------            |
| blog_article           | writing                  | generate a blog article                                   |
| linkedin_post          | writing                  | generate a linkedin post                                  |
| tutorial_writer        | writing                  | generate a tutorial                                       |

## Bootstrapping Your Environment

[Bootstrapping Documentation](/docs/bootstrap.md)
