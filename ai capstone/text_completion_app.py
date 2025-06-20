import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_completion(prompt, temperature=0.7, max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the AI Text Completion App. Type 'exit' to quit.")
    while True:
        user_input = input("\nEnter your prompt: ").strip()
        if user_input.lower() == "exit":
            break
        if not user_input:
            print("Prompt cannot be empty. Try again.")
            continue

        temperature = input("Temperature (0.0 to 1.0, default 0.7): ").strip()
        max_tokens = input("Max tokens (default 150): ").strip()

        temperature = float(temperature) if temperature else 0.7
        max_tokens = int(max_tokens) if max_tokens else 150

        output = get_completion(user_input, temperature, max_tokens)
        print("\nAI Response:")
        print(output)

if __name__ == "__main__":
    main()
