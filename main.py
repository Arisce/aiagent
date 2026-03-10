import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.call_function import available_functions
from functions.call_function import call_function

verbose = False

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API key not found")

client = genai.Client(api_key=api_key)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(20):

        response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt, 
            temperature=0)
        )

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.usage_metadata is None:
            raise RuntimeError("Usage Metadata is None")
        
        if args.verbose:
            print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage_metadata.prompt_token_count}\nResponse tokens: {response.usage_metadata.candidates_token_count}")
        
        if response.function_calls:

            function_results = []

            for function_call in response.function_calls:

                function_call_result = call_function(function_call, verbose=verbose)

                if not function_call_result.parts:
                    raise Exception("Function call returned no parts")

                function_response = function_call_result.parts[0].function_response

                if function_response is None:
                    raise Exception("Function response was None")

                if function_response.response is None:
                    raise Exception("Function response payload was None")

                function_results.append(function_call_result.parts[0])

                print(function_response.response)        

                if verbose:
                    print(f"-> {function_response.response}")

        else:
            print(response.text)
            break
        
        messages.append(types.Content(role="user", parts=function_results))

    else:
        print("Error: Maximum number of iterations reached without a final response.")
        sys.exit(1)
        


if __name__ == "__main__":
    main()
