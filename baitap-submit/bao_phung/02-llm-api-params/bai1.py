from openai import OpenAI
from openai_client import OpenAIClient

client = OpenAIClient().get_client()

user_input = input("\nEnter your question: ")
messages = [{"role": "system", "content": "You are a helpful assistant."}]
messages.append({"role": "user", "content": user_input})

stream = client.chat.completions.create(
    messages=messages,
    model="gpt-4o-mini",
    stream=True,
    max_tokens=400,
    temperature=0.7,
    top_p=1.0,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end="")
