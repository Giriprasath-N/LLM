import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_client():
    """Initialize and return the Gemini API client."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("[!] Warning: GEMINI_API_KEY environment variable is missing.")
        print("    Please add GEMINI_API_KEY=your_key_here to your .env file.")
    try:
        from google import genai
        return genai.Client(api_key=api_key)
    except ImportError:
        print("[X] Error: 'google-genai' package is not installed.")
        print("    Run: pip install google-genai python-dotenv")
        sys.exit(1)

def generate_response(prompt: str, model: str = "gemini-2.5-flash"):
    """Single prompt generation helper."""
    client = get_client()
    print(f"\n--- Generating response using {model} ---")
    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
        )
        print(response.text)
    except Exception as e:
        print(f"[X] API Error: {e}")

def start_interactive_chat(model: str = "gemini-2.5-flash"):
    """Start a multi-turn chat session."""
    client = get_client()
    chat = client.chats.create(model=model)
    
    print("=" * 50)
    print("      LLM Interactive Chat Session")
    print("      Type 'exit' or 'quit' to end")
    print("=" * 50 + "\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit"):
                print("Goodbye!")
                break

            response = chat.send_message(user_input)
            print(f"\nLLM: {response.text}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nSession closed.")
            break
        except Exception as e:
            print(f"\n[X] Error: {e}\n")

if __name__ == "__main__":
    # If prompt passed as command line argument: python app.py "Explain quantum computing"
    if len(sys.argv) > 1:
        prompt_arg = " ".join(sys.argv[1:])
        generate_response(prompt_arg)
    else:
        # Otherwise run interactive chat
        start_interactive_chat()
