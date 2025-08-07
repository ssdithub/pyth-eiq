import requests
import json

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )

        if response.ok:
            print("Gemma:", end=" ", flush=True)
            for line in response.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode('utf-8'))
                        print(data.get("response", ""), end="", flush=True)
                    except Exception as e:
                        print(f"\n[Error parsing line]: {e}")
            print()  # newline after response
        else:
            print("❌ Ollama error:", response.text)

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama. Is it running?")
    except Exception as e:
        print("❌ Error:", e)

def main():
    print("💬 Welcome to the Gemma3:1B Chatbot!")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        ask_ollama(user_input)

if __name__ == "__main__":
    main()
