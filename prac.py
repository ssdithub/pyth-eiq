import requests

# Replace with your prompt
prompt = "hello what is today's weather in New York?"

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:1b",
        "prompt": prompt
    },
    stream=True
)

if response.ok:
    for line in response.iter_lines():
        if line:
            try:
                data = line.decode('utf-8')
                import json
                obj = json.loads(data)
                print(obj.get("response"), end="", flush=True)
            except Exception as e:
                print(f"\n[Error parsing line]: {e}")
    print()
else:
    print("Error:", response.text)
