import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
# MODEL_NAME = "mixtral-8x7b-32768"
MODEL_NAME = "llama-3.3-70b-versatile"


def call_expert(system_prompt, user_input):
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.7,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
    )

    return completion.choices[0].message.content