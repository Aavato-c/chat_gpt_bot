import os
import openai
import logging
import json

# Store your api key in .env dile in the same directory as this file
openai.api_key = os.environ.get('API_OPENAI')

