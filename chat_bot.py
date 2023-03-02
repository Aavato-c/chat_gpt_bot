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

# Openai tunings for the bot
CHAT_GPT_MODEL_ROLE = "You are a helpful assistant."

# Initiate the chat log
messages = [{"role": "system", "content": CHAT_GPT_MODEL_ROLE}]

def chatgpt_bot(input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )
    return response


def initiate_dialogue():
    print("This is a python program that uses OpenAI's ChatGPT API to chat with you.\n\n")
    user_name = input("What is your name? ")
    print("Thanks. Let's chat!")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    initiate_dialogue()