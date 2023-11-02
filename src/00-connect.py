import os
import openai
import requests
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a two sentence poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)

# Create an OpenAI request using the python requests library.
response = requests.post("https://api.openai.com/v1/engines/davinci/completions",
                        headers={"Authorization": "Bearer " + os.getenv("OPENAI_API_KEY")},
                        json={"prompt": "How are you doing today?",
                              "max_tokens": 100,
                              "temperature": 0.9,
                              "top_p": 1,
                              "frequency_penalty": 0,
                              "presence_penalty": 0,
                              "stop": ["\n"]})

print("\n\n")
print(response.json()["choices"][0]["text"])
