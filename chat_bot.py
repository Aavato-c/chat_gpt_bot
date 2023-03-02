import os
import openai
import logging
import json
import time

# Store your api key in .env dile in the same directory as this file
openai.api_key = os.environ.get('API_OPENAI')

# Logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)   
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Basic logger
logger = setup_logger('default_logger', 'log_of_bot.log')

# Chat logger
chat_logger = setup_logger('second_logger', 'second_logfile.log')

# Consts
CHAT_LOG_FILE = "Chat_log.json"

# Openai tunings for the bot
CHAT_GPT_MODEL_ROLE = "You are a helpful assistant."

# Initiate the chat log
messages = [{"role": "system", "content": CHAT_GPT_MODEL_ROLE}]

def chatgpt_bot(user_name):
    input_text = input(f"{user_name}: ")
    messages.append({"role": "user", "content": input_text})
    chat_logger.info(f"{user_name}: {input_text}")
    
    logger.info("Making request to OpenAI")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    
    messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print(f"ChatGPT: {response['choices'][0]['message']['content']})")
    
    chat_logger.info(f"ChatGPT: {response['choices'][0]['message']['content']})")


def initiate_dialogue():
    print("This is a python program that uses OpenAI's ChatGPT API to chat with you.\n\n")
    user_name = input("What is your name? ")
    print("Thanks. Let's chat!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    logger.info("Chat log initiated")
    while True:
        chatgpt_bot(user_name)


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    initiate_dialogue()

if __name__ == "__main__":
    main()