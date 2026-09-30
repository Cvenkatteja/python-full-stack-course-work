#load libarires
import os
import time
from datetime import datetime
from huggingface_hub import InferenceClient
from dotenv import load_dotenv



#step-->1 Loading hugginface Token from .env file
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    print("Error : HF_TOKEN is not found")
    print("Create a .env file and copy paste the token in it")
print("HF_TOKEN = Your Token is",HF_TOKEN[:3])

client = InferenceClient(provider = "auto",token = HF_TOKEN)
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


