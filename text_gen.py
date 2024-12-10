from openai import OpenAI
client = OpenAI()\

completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "Write a little bit on how to make coffee"
            }
        ]
    )

print(completion.choices[0].message.content)