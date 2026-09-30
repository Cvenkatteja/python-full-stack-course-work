'''
#You -->Swiggy App --> Restaurants --> Food

#Python Program --> API --> LLMs --> Response

import requests
#Send a request to the test endpoint that echoes information
url = "https://httpbin.org/json"
#url = "https://codegnan.com/"
response = requests.get(url)
print(response) #it returns status code
print(f'Status Code is : {response.status_code}')
#data = response.content
#print("Response data:",data)
data = response.json()
print(data) #returns in dict format
print(data.keys())

import os
from dotenv import load_dotenv
#read the .env file and load its values into the environment
load_dotenv()
#retrieve the token by its name
token = os.getenv("HF_TOKEN")
#confirm if the given token is loaded without printing
#the whole secret key
if token:
    print("Token Loaded Successfully:",token[:3])
else:
    print("No Token found,check your .envfile exists")

'''

#First API call

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
load_dotenv()
client = InferenceClient(provider="auto",
                         token = os.getenv("HF_TOKEN")
                         )
response = client.chat.completions.create(
    model = "Qwen/Qwen2.5-7B-Instruct",
    messages = [
        {
            "role": "user",
            "content":"What is Artificial Intelligence?"}],
    max_tokens = 100)
print(response)
print(response.choices[0].message.content)

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.3",
    token=os.getenv("HF_TOKEN")
)
#Create a Function to give multiple questions
#day 5

#here we  create a function

def chat(prompt):
    """Function to accept input responses"""
    response = client.chat.completions.create(
        model = "Qwen/Qwen2.5-7B-instruct",
        messages = [
            {
                "role" : "user",
                "content" : prompt}],
        max_tokens = 200)
    return response.choices[0].message.content
#prompt = input("enter the desired prompt:")
#print(chat(prompt))

#in the case  if we need to multiple question

question = [
    "Explain  about Genereative ai ,like you are teaching to a kid",
    "Explain about quantaum computing in the simplest way",
    "What is the purposse of the Rag?Explain in a simple way."]
for question in question:
    print('==' * 50)
    print("question:")
    print(question)
    print()
    answer = chat(question)
    print(answer)
    print()
    
#we want to  build  an interactive chat


while True:
    question  = input(" Enter Your question or type = 'exit' to stop:")
    if question.lower() == "exit":
        print("Good Bye... Have a good day")
        break
    answer = chat(question)
    print('\n AI Response')
    print(answer)
    



































