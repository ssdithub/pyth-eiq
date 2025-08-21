import requests
import base64
import json

def ask_llava_with_image(image_path, question):
    # Convert image to base64
    with open(image_path, "rb") as f:
        image_base64 = base64.b64encode(f.read()).decode("utf-8")

    # Send request to Ollama
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llava",
            "prompt": question,
            "images": [image_base64]
        }
    )

    if response.ok:
        for line in response.iter_lines():
            if line:
                try:
                    data = line.decode('utf-8')
                    obj = json.loads(data)
                    print("LLaVA:", obj.get("response", obj))
                except Exception as e:
                    print(f"\n[Error parsing line]: {e}")
    else:
        print("❌ Error:", response.text)

# Example usage
ask_llava_with_image("images.jpeg", "Describe what is happening in this picture")