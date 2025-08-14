from openai import OpenAI
from openai_client import OpenAIClient
import tiktoken

client = OpenAIClient().get_client()

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def split_text_by_tokens(text, max_tokens=1500):
    enc = tiktoken.encoding_for_model("gpt-4o-mini")
    tokens = enc.encode(text)
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunks.append(enc.decode(chunk_tokens))
    return chunks

def translate_text(text, target_language):
    prompt = (
        f"""You are a senior professional translator, fluent in both the source and target languages at a native level, with the ability to edit content so that it is both accurate and engaging.
            Your task:
            1. Carefully read the source text and translate it into [TARGET LANGUAGE] with high accuracy, preserving meaning, facts, proper nouns, and numerical data.
            2. Maintain a natural, fluent tone that fits the cultural context and writing style of the target language.
            3. Choose smooth, appealing wording that creates an engaging reading experience, matching or surpassing the quality of the original text.
            4. Adjust sentence structure and flow to ensure clarity and coherence, avoiding literal or mechanical translations.
            5. If the source contains errors or ambiguities, refine the translation to keep it clear and logical.
            6. Preserve important formatting (headings, paragraphs, bullet points, etc.).
            7. For technical or domain-specific terms, use the most accurate and widely accepted terminology suited for the target audience.

            Output:
            - A complete, professional, and captivating translation with high editorial quality.
            - Do not include explanations or notes unless explicitly requested.
            
            Text:{text}
            """
    ).replace("[TARGET LANGUAGE]", target_language)

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional translator."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return resp.choices[0].message.content.strip()

text = read_file("baitap-submit/bao_phung/02-llm-api-params/bai4.txt")
chunks = split_text_by_tokens(text)
print(f"📄 File có {len(chunks)} phần cần dịch.")
translated_parts = []
for idx, chunk in enumerate(chunks, start=1):
    print(f"🔄 Đang dịch phần {idx}/{len(chunks)}...")
    translated_text = translate_text(chunk, "English")
    translated_parts.append(translated_text)

# Ghép lại
final_translation = "\n".join(translated_parts)

# Lưu file
output_file = "baitap-submit/bao_phung/02-llm-api-params/bai4_output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(final_translation)

print(f"✅ Hoàn tất! Bản dịch đã lưu vào {output_file}")
