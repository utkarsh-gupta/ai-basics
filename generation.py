from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "You are a helpful assistant that answers questions "
                        "in the style of a redneck cowboy from southeast texas."
                    )
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is the best way to use a lasso?"
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)
