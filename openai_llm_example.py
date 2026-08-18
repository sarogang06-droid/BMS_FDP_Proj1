import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_openai(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
    )
    return response.output_text


if __name__ == "__main__":
    user_input = input("Ask the OpenAI model: ")
    answer = ask_openai(user_input)
    print("\nAI Response:\n")
    print(answer)
