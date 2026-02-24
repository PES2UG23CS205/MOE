import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# MODEL_NAME = "mixtral-8x7b-32768"
MODEL_NAME = "llama-3.3-70b-versatile"


def route_prompt(user_input: str) -> str:
    routing_prompt = f"""
Classify this query into ONE category:
technical
billing
general
crypto_tool

Return ONLY the category word.

Query:
{user_input}
"""

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,  # deterministic routing
        messages=[{"role": "user", "content": routing_prompt}],
    )

    return completion.choices[0].message.content.strip().lower()