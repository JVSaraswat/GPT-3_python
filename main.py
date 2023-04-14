import openai

# Set up the OpenAI API client
openai.api_key = "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"
# Use the openai.Completion method to generate text:
def ask_question(question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=(f"Q: {question}\nA:"),
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

question = "Could you tell me some time management techniques?"
answer = ask_question(question)
print(answer)