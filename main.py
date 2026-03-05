import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API key not found")

client = genai.Client(api_key=api_key)

def main():
    ai_return = client.models.generate_content(
        model = "gemini-2.5-flash", 
        contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    if ai_return.usage_metadata is None:
        raise RuntimeError("Usage Metadata is None")
    print(f"Prompt tokens: {ai_return.usage_metadata.prompt_token_count}\nResponse tokens: {ai_return.usage_metadata.candidates_token_count}")
    print(ai_return.text)
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
