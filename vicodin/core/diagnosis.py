from openai import OpenAI


def diagnose(prompt: str) -> str:
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5",
        tools=[{"type": "web_search"}],
        text={
            "verbosity": "low"
        },
        instructions="Talk like Dr. House from House MD."
        input=prompt,
    )
    return response.output_text
