from openai import OpenAI
from openai_client import OpenAIClient

client = OpenAIClient().get_client()

messages = [{"role": "system", "content": "You are a helpful assistant."}]
while True:
    user_input = input("\nEnter your question: ")
    if (
        user_input.lower() == "exit"
        or user_input.lower() == "quit"
        or user_input.lower() == "quit"
        or user_input.lower() == "q"
    ):
        break
    messages.append({"role": "user", "content": user_input})

    stream = client.chat.completions.create(
        messages=messages,
        model="gpt-4o-mini",
        stream=True,
        max_tokens=500,
        temperature=0.7,
        top_p=1.0,
    )

    bot_reply = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            print(content, end="")
            bot_reply += content

    print()
    messages.append({"role": "assistant", "content": bot_reply})
