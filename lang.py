import whisper

# Load Whisper model (use "base" / "small" / "medium" / "large")
model = whisper.load_model("small")

# Transcribe the audio file (auto-detects language)
result = model.transcribe("hindiaud.mp3")

print("Detected language:", result["language"])
print("Transcription:\n", result["text"])
