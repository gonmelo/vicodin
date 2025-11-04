from openai import OpenAI


def diagnose(prompt: str) -> str:
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5",
        tools=[{"type": "web_search"}],
        input=prompt,
    )
    return response.output_text
