from openai import OpenAI
from groqai_client import GroqAIClient

def write_script_code(question):
    prompt = f"""You are a senior software engineer highly proficient in Python.
        Please read the problem statement below and write a complete Python solution.
        - Only output valid Python code and code comments.
        - Do not include explanations, analysis, pseudocode, sample inputs/outputs, or anything except Python code and comments.
        - The code should be clean, readable, and follow best practices.
        - Ensure the code is well-commented to explain each step.
        - Have sample input/output examples to verify the code works.
        Problem statement: {question}
        """
    bot_reply = ""
    resp = client.chat.completions.create(
        model="gemma2-9b-it",
        messages=[
            {
                "role": "system",
                "content": "You are a senior software engineer highly proficient in Python.",
            },
            {"role": "user", "content": prompt},
        ],
        stream=True,
        max_tokens=1500,
    )

    print("🔄 Processing your request...")
    for chunk in resp:
        content = chunk.choices[0].delta.content
        if content is not None:
            bot_reply += content

    return bot_reply.strip()


client = GroqAIClient().get_client()

user_input = input("\nEnter your question: ")
result = write_script_code(user_input)
clean_result = "\n".join(
    line for line in result.splitlines() if line.strip() not in ("```python", "```")
)

# Save result to final.py
with open(
    "baitap-submit/bao_phung/02-llm-api-params/final.py", "w", encoding="utf-8"
) as f:
    f.write(clean_result)
print("✅ Output saved to final.py")
