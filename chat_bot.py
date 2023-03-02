import os
import openai
import logging
import json

# Store your api key in .env dile in the same directory as this file
openai.api_key = os.environ.get('API_OPENAI')

logging.basicConfig(filename='./log_of_bot.txt',format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Consts
CHAT_LOG_FILE = "Chat_log.json"

