import pyttsx3

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read()

engine = pyttsx3.init()
engine.save_to_file(text, "output.mp3")
engine.runAndWait()
print("✅ Offline audio saved as output.mp3")
