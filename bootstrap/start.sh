#!/bin/sh

# POSIX shell environment bootstrap script to get the ball rolling

echo " !!! Quick Start Environment Bootstrap !!!"

echo ">>> Provision the Virtual Environment <<<"
python -m venv .venv

echo ">>> Activate The Virtual Environment <<<"
./.venv/bin/activate

echo ">>> Install the Needed Packages <<<"
pip install -r requirements.txt

echo "!!! Environment Bootstrapped !!!"


