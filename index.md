# Implementation Scripts

<!-- toc -->

## Introduction

Here are scripts that implement some GPT related functionality or interaction, generally a result of a tutorial or some extrapolation there upon.

Included is a bootstrapping script, so that with a basic installation of Python on a Unix-like OS, you can quickly spin up the environment necessary to run the scripts. I have opted not to torture potentially interested parties with my functional package manager (Nix) and its way of doing business and feel that, for the time being at least, using a Python Notebook would be overkill. Thus I have opted to use `venv` for this bootstrapping process, an easy and baked in solution to isolated development environments for Python scripts.

In order to run these scripts, assuming you have cloned the repository (or downloaded the zip file) and are using a Unix-like OS with BASH or ZSH as you terminal emulator's shell, navigate to this directory and run:

```bash

bash start.sh

python [name_of_the_script_you_want_to_run].py

# You will then be prompted for input depending on the script chosen

```

> Note
>
> You will need to provide the `OPENAI_API_KEY` environmental variable to your shell to run these scripts. This can be done by running `export OPENAI_API_KEY=[your key]` and keys can be sourced from [here](https://platform.openai.com/account/api-keys).

| Script Name                   | Functionality                                                                             |
| ----------------------------- | ----------------------------------------------------------------------------------------- |
| gpt3chatbot.py                | Creates a chatbot out of GPT-3, memory via of prior input via loops                       |
| gpt3therapist.py              | Chatbot acts as a therapist, beginning by asking how the user feels and going from there. |
| gpt3prompgenerator.py         | Generates and improves prompts                                                            |
| gpt3bloginformativearticle.py | Generates informative blog posts when given a topic                                       |
| gpt3tutorialwriter.py         | Writes technical tutorials when provided an objective                                     |
| start.sh                      | Bootstraps the Python Environment and Installs the Needed Packages                        |
| requirements.txt              | List of dependencies that will be installed by `pip`                                      |
