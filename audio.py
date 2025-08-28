import whisper
import sys
import os

def transcribe_audio(audio_path, model_size="base"):
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio not found: {audio_path}")

    print("🎤 Transcribing with Whisper...")
    # On CPU, set fp16=False to avoid errors
    model = whisper.load_model(model_size)  # "tiny", "base", "small", "medium", "large"
    result = model.transcribe(audio_path, fp16=False)  # verbatim-style transcription
    text = result.get("text", "").strip()
    return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python audio.py <path-to-audio> [whisper-size]")
        print("Example: python audio.py harvard.wav base")
        sys.exit(1)

    audio_path = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "base"

    text = transcribe_audio(audio_path, model_size=model_size)
    print("\n📝 Transcription (verbatim):\n")
    print(text)

if __name__ == "__main__":
    main()
