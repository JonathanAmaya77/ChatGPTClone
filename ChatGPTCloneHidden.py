import os
import requests
import openai
import requests

api_key = "Enter your API key here"
url = "https://api.openai.com/v1/chat/completions"

# Header with Authorization token
headers = {"Authorization": f"Bearer {api_key}"}

# Initialize conversation context
messages = []


def send_message(user_message):
    # Add the user message to the conversation history
    messages.append({"role": "user", "content": user_message})

    # Create request payload
    body = {
        "model": "gpt-3.5-turbo",  # Change to "gpt-4" if you have access
        "messages": messages
    }

    # Send request to OpenAI API
    response = requests.post(url, headers=headers, json=body)

    # Check for errors
    if response.status_code == 200:
        response_data = response.json()
        if "choices" in response_data and response_data["choices"]:
            assistant_message = response_data["choices"][0]["message"]["content"]
            # Add the assistant's response to the conversation history
            messages.append({"role": "assistant", "content": assistant_message})
            return assistant_message
        else:
            return "No response received from OpenAI."
    else:
        return f"Error: {response.status_code}, {response.text}"


print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program.")
print("Type 'new' to start a new conversation thread.\n")

while True:
    user_message = input("You: ").strip()
    if user_message.lower() == "exit":
        break
    elif user_message.lower() == "new":
        # Clear context for a new conversation thread
        messages = []
        print("New conversation thread started.\n")
        continue
    response_text = send_message(user_message)
    print(f"GPT: {response_text}")

