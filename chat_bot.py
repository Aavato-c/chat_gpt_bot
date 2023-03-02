import os
import openai
import logging
import json
import time

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

def chatgpt_bot(user_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    input_text = input(f"{user_name}: ")
    messages.append({"role": "user", "content": input_text})
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    print(response)
    print(response['choices'][0]['message']['content'])
    return response


def initiate_dialogue():
    print("This is a python program that uses OpenAI's ChatGPT API to chat with you.\n\n")
    user_name = input("What is your name? ")
    print("Thanks. Let's chat!")
    time.sleep(1)
    return chatgpt_bot(user_name)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    initiate_dialogue()

if __name__ == "__main__":
    main()