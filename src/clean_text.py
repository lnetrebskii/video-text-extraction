from openai import OpenAI


def clean_text_with_chatgpt(text, api_key):
    
    client = OpenAI(api_key = api_key)
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Clean the following text by removing duplicates and noise:\n\n{text}"}
        ],
        max_tokens=20480,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    return response.choices[0].message.content
