from dotenv import load_dotenv

# Load API keys and MARBLE_* settings from the nearest .env for every entry
# point (main.py, werewolf scripts, tests) before any module reads them.
load_dotenv()
