# import os
# from dotenv import load_dotenv
# from huggingface_hub import InferenceClient

# load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")

# client = InferenceClient(api_key=HF_TOKEN)

# MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


# def call_llm(prompt: str) -> str:
#     try:
#         response = client.chat.completions.create(
#             model=MODEL_NAME,
#             messages=[
#                 {"role": "system", "content": "You are a helpful DSA tutor."},
#                 {"role": "user", "content": prompt},
#             ],
#             max_tokens=300,
#             temperature=0.3,
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         return f"❌ Error: {e}"

import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found! Set it in environment variables.")

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


def call_llm(prompt: str) -> str:
    try:
        payload = {
            "model": "hf:HuggingFaceH4/zephyr-7b-beta",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 300
        }

        response = requests.post(API_URL, headers=headers, json=payload)

        data = response.json()

        if "choices" in data:
            return data["choices"][0]["message"]["content"]

        return f"❌ Unexpected response: {data}"

    except Exception as e:
        return f"❌ Error: {e}"