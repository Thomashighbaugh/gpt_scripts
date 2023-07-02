#!/bin/sh

echo "Quick Start Environment Bootstrap"

# First Provision the Virtual Environment
python -m venv .venv
# Then Activate It
source .venv/bin/activate
# Finally Install the Needed Packages
pip install -r requirements.txt
