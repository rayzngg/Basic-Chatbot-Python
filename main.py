from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

systemPrompt = "You are a helpful assistant. Your role is to answer the user's queries in a concise and efficient manner."
message = [{"role": "system", "content": systemPrompt}]

print("This is the start of your conversation. Enter 'exit', 'quit' or 'end' to end the conversation.\n")

while True:
    userQuery = input("You: ")

    if userQuery.lower() in {"exit", "quit", "end"}:
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




