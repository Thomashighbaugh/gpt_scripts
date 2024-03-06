# Bootstrap Process

To get these scripts to work locally, you will need to have the gpt4free up and running, as well as a local virtual environment within the directory you have the scripts in. To do so follow the below commands in this order.

```bash
# Get GPT4Free
git clone https://github.com/xtekky/gpt4free

# Change directories into the gpt4free project
cd gpt4free

# pull the selenium container you'll want
docker pull selenium/node-chrome

# Build then start the container with docker compose
docker-compose up  --build

# ─────────────────────────────────────────────────────────────────
# Now in a new terminal emulator window

# Download these scripts
git clone https://github.com/Thomashighbaugh/GPT_Scripts

# Provision the Virtual Environment
python -m venv .venv

# Activate The Virtual Environment
source .venv/bin/activate

# Install the Needed Packages
pip install -r requirements.txt

```

Once this is done, to run the scripts is as easy as `python [script].py` using the same terminal emulator window you entered the `source .venv/bin/activate` command in.  
