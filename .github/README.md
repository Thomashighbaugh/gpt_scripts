# GPT Scripts

This repository contains GPT-3-Turbo scripts that utilize various prompts to provide specific interaction patterns with GPT-3 from your local terminal (command line).

## Rebased Using GPT4Free

My trial for OpenAI's API ran out, I am poor and yet using the ChatGPT interface, or any alternative I have explored, to do a lot of these tasks is painful (but shout out to FlowGPT where I have many of my prompts located for ease of demonstration).

Luckily, GPT4Free exists (still) and it enables one to query the API of various implementations of GPT-3-turbo and GPT-4 for free.

With GPT4Free, I am able to return to working with AI using Python scripts instead of waiting for FlowGPT to load and generate most of what I have AI do for me. This has meant reworking the API call of these scripts (or using the < 1.0.0 version of the pip `openai` package and setting an extra variable in the script with some other annoyances that I opted not to do), which now has been completed for all of the scripts in this repository and they have been tested to ibsure they at least work (optimally, no. Adjustments needed for longer content generation, mostly swapping the model to GPT-3-turbo which has more than just Bing as a potential generator) and I will begin pulling my prompts from FlowGPT to populate this repository for some more mature and substantial scripts in the near future.

Yes I know that Gemini is free for certain number of messages a day, but I am not going to use it for these scripts as it enables you to turn off the content blocking so I am using it where I find that useful and use GPT4Free here instead.

## Scripts Available

```
 .
├──  coding - files for writing or improving code 
│  ├──  annotate_python_code.py - quickly provide annotations for Python code
│  ├──  awesomewm_code_generator.py - generate code for AwesomeWM
│  ├──  bash_oneliner.py - write a bash one-liner quickly to do a specific task
│  ├──  improve_awesomewm_code.py - improve AwesomeWM code
│  └──  improve_python_code.py - improve Python code (and add comments + docstrings to it)
├──  job_seeking - files for finding a job
│  └──  coverletter.py - writes cover letters after taking your resume and the job description
├──  misc - miscellaneous files
│  └──  therapist.py - a chatbot therapist that basically asks how it made you feel
├──  prompting - files for interacting with AI 
│  ├──  chatbot.py - a regular chatbot in your terminal
│  ├──  g4f_check.py - checks what providers and models are available 
│  ├──  image_prompt_generator.py - creates image prompts for stablediffusion models
│  ├──  prompt_generator.py - generates prompts based on your input 
│  ├──  prompt_optimizer.py - optimizes a prompt
│  └──  spr_generator.py - generates a condensed version of input text primed for AI 
└──  writing - files for writing content
   ├──  blog_article.py - writes an article for a blog
   ├──  linkedin_article.py - Writes an article for LinkedIn
   └──  tutorial_writer.py - writes a tutorial

```
