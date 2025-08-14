from openai import OpenAI
from openai_client import OpenAIClient
import requests
from bs4 import BeautifulSoup


def get_website_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        main_content = soup.find("div", id="main-detail")
        if main_content:
            return main_content.get_text(strip=True)
        else:
            return "Không tìm thấy nội dung trang web."
    else:
        raise Exception(f"Không thể truy cập trang web: {response.status_code}")


def get_website_text_bỵ_jina(url):
    jina_url = "https://r.jina.ai/" + url
    resp = requests.get(jina_url)
    if resp.status_code != 200:
        raise Exception(f"Lỗi lấy dữ liệu: {resp.status_code}")
    return resp.text


def build_summary_prompt(content):
    """
    Tạo prompt chuẩn để gửi cho AI tóm tắt nội dung.
    """
    prompt = f"""
    Bạn là một chuyên gia tóm tắt tin tức. 
    Nhiệm vụ của bạn là đọc nội dung sau và tóm tắt thật ngắn gọn, đầy đủ ý chính, bỏ qua thông tin thừa, giữ nguyên thông tin quan trọng.

    Nội dung:
    {content}

    Yêu cầu:
    - Viết bằng tiếng Việt.
    - Giữ đúng các số liệu, tên riêng.
    - Độ dài tóm tắt khoảng 3-5 câu.
    - Không sử dụng từ ngữ khó hiểu, viết dễ hiểu cho người đọc.
    """
    return prompt.strip()


client = OpenAIClient().get_client()
url = input("Vui lòng nhập link url để tóm tắt tin tức: ")

# main_content = get_website_text(url)
main_content = get_website_text_bỵ_jina(url)
prompt = build_summary_prompt(main_content)

print("Đang gửi yêu cầu tóm tắt...")

stream = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="gpt-4o-mini",
    stream=True,
    max_tokens=500,
    temperature=0.7,
    top_p=1.0,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content is not None:
        print(content, end="")
