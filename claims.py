import fitz  # PyMuPDF
import requests
import json

def extract_text_from_pdf(path):
    """Extract raw text from PDF"""
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def summarize_claim(context):
    """Ask Ollama to extract and summarize claims info"""
    prompt = f"""
    You are an AI assistant that extracts structured information from claims documents.
    From the following text, create a clear summary with all key details:

    Required fields:
    - Insured Name
    - Claim Status
    - Date of Loss
    - UCR
    - Cedent Claim No
    - Loss Description
    - Contract With
    - UMR
    - Coverage Period
    - Limit xs Retention
    - Aggregate Limit
    - Gross Loss (Paid, Outstanding, Incurred)
    - Gross Expense (Paid, Outstanding, Incurred)
    - Subject Loss
    - Ceded Loss
    - Net Due From ABC Limited
    - Placement %
    - Incurred Loss at Placement

    Document:
    {context}

    Return the result in JSON format.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma3",  # or whichever gemma3 variant you have
            "prompt": prompt,
            "stream": False
        }
    )

    if response.ok:
        data = response.json()
        return data.get("response", "").strip()
    else:
        return f"❌ Ollama error: {response.text}"

def main():
    pdf_path = input("Enter path to claims PDF: ")
    text = extract_text_from_pdf(pdf_path)

    print("\n⏳ Extracting information from claims document...")
    summary = summarize_claim(text)

    print("\n✅ Extracted Information Summary:\n")
    print(summary)

    # Optional: save to file
    with open("claims_summary.json", "w") as f:
        f.write(summary)
        print("\n💾 Saved summary to claims_summary.json")

if __name__ == "__main__":
    main()
