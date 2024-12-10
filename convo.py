from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "knock knock."}]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Who's there?"}]
        },
        {
            "role": "assistant",
            "content": [{"type": "text", "text": "Europe."}]
        },
        {
            "role": "user",
            "content": [{"type": "text", "text": "Europe Who?"}]
        }
    ]
)

print(response.choices[0].message.content)