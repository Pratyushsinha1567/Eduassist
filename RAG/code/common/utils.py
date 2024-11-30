import openai
import os
from dotenv import load_dotenv, find_dotenv

import numpy as np
import nest_asyncio
import os



load_dotenv(r"C:\Users\praty\OneDrive\Desktop\RAG\code\common\openAI.env")
def getapi():
    api_key=os.environ.get('OPENAI_API_KEY')
    print(api_key)
    return api_key
getapi()