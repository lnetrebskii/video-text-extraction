import csv
from openai import OpenAI

# Extract words suitable for B1 and higher level
def extract_b1_words(text, api_key):
    
    client = OpenAI(api_key = api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Extract B1 and higher level words from the following text:\n\n{text}"}
        ],
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5
    )
    
    words = response.choices[0].message.content.split()
    unique_words = list(set(words))
    return unique_words

def save_words_to_csv(words, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Word']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for word in words:
            writer.writerow({'Word': word})
