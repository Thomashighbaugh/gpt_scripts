#!/usr/bin/env bash

# A NixOS/portable implementation of the start script using Z-Shell like I do locally to insure that things are all  
# set up in my current zsh session envuiroment the first time.

echo " !!! Quick Start Environment Bootstrap !!!"

echo ">>> Provision the Virtual Environment <<<"
python -m venv .venv

echo ">>> Activate The Virtual Environment <<<"
source .venv/bin/activate

echo ">>> Install the Needed Packages <<<"
pip install -r requirements.txt

echo "!!! Environment Bootstrapped !!!"

