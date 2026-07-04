import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

def summarize_article(title):

    prompt = f"""
You are a music industry analyst.

Summarize this music headline into exactly three concise bullet points.

Headline:
{title}
"""

    response = client.chat.completions.create(
        model="z-ai/glm-5.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=150
    )

    return response.choices[0].message.content