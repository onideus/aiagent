import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")


def main():
    user_input = sys.argv
    if len(user_input) < 2 and user_input[1] is None:
        print("not prompt provided, exiting")
        sys.exit(1)
    user_prompt = user_input[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.0-flash-001",
                                              contents=messages)
    print(response.text)

    if len(user_input) > 2 and user_input[2] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
