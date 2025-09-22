from openai import OpenAI
from dotenv import load_dotenv
import json

with open("config.json", "r") as f:
    config = json.load(f)
systemPrompt = config.get("systemPrompt", "")

load_dotenv()
client = OpenAI()

def editConfig(newPrompt):
    with open ("config.json", "r") as f:
        config = json.load(f)
    
    config["systemPrompt"] = newPrompt

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    
    return

message = [{"role": "system", "content": systemPrompt}]

print("\nThis is the start of your conversation.\n\nType [end] to end the conversation.\n\nType [config] to adjust system prompt. (warning: this will restart the chat)\n")

while True:
    userQuery = input("You: ")

    if userQuery.lower() in {"end"}:
        break

    if userQuery.lower() in {"config"}:
        print(f'\nSystem prompt: {systemPrompt}\n\nWould you like to change the system prompt?\n')
        configConfirm = input("<y/n>: ")
        if configConfirm == "y":
            newPrompt = input("\nEnter new system prompt: ")   
            editConfig(newPrompt)
            break
        if configConfirm == "n":
            break
       
    if not userQuery:
        continue 

    message.append({"role": "user", "content": userQuery}) 

    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = message
    )
    botMsg = response.choices[0].message.content
    print(f'\nGPT: {botMsg}\n')
    message.append({"role": "assistant", "content": botMsg}) 







