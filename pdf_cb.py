import fitz  # PyMuPDF
import requests
import json

def extract_text_from_pdf(path):
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip()
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ""

def ask_ollama(context, question):
    full_prompt = f"""You are an AI assistant reading a document. Here is the content of the document:\n\n{context}\n\nNow answer this question based on the document:\n{question}"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": full_prompt,
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
            print()
        else:
            print("❌ Ollama error:", response.text)

    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to Ollama. Is it running?")
    except Exception as e:
        print("❌ Error:", e)

def main():
    print("📄 PDF Analysis Chatbot with Gemma3:1b")
    pdf_path = input("Enter path to your PDF file: ")

    print("\n⏳ Extracting text from the PDF...")
    context = extract_text_from_pdf(pdf_path)

    if not context:
        print("❌ No text found. Exiting.")
        return

    print("✅ Text extracted. You can now ask questions about the PDF.")
    print("(Type 'exit' or 'quit' to end)\n")

    while True:
        question = input("You: ")
        if question.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break
        ask_ollama(context, question)

if __name__ == "__main__":
    main()
