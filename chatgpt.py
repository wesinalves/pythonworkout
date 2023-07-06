import requests
import json

# Define the API endpoint URL 
api_url = "https://api.openai.com/v1/chat/completions"

# set your OpenAi API key
api_key = "YOUR_API_KEY"

# define the headers with your API key
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# define the payload with the message you want and the model
data = {
    "model": "gpt-3.5-turbo",
    "messages":[
        {"role": "user", "content": "Who won the world series in 2020"}
    ]
}

# send a post request to the endpoint
response = requests.post(api_url, headers=headers, json=data)

# get the response as JSON
response_json = response.json()

# extract the generated reply
reply = response_json["choices"][0]["message"]["content"]

print(reply) 

# Curte, comenta e compatilha!!!!