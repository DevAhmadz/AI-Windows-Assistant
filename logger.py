import logging
from datetime import datetime

# Configure logger
logging.basicConfig(
    filename="action.log",
    level=logging.INFO,
    format="%(asctime)s — %(message)s",
)

def log_action(user_input, intent, result):
    log_msg = f"User input: '{user_input}' | Detected intent: '{intent}' | Action: {result}"
    logging.info(log_msg)
