import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    client = genai.Client(api_key=api_key)
    print(client.models.generate_content(model="gemini-2.0-flash-001",
                                         contents="What's makes python a great language for llms? Limit your answer to roughly a paragraph in length.").text)

if __name__ == "__main__":
    main()
