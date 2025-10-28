from elevenlabs import ElevenLabs
import config

# Initialize ElevenLabs client
client = ElevenLabs(api_key=config.ELEVENLABS_API_KEY)

print("=== Testing Speech-to-Text with Georgian ===\n")

audio_file_path = "test_output.mp3"

print(f"Reading audio file: {audio_file_path}")

try:
    print("Sending audio to ElevenLabs for transcription...\n")
    
    with open(audio_file_path, "rb") as audio_file:
        result = client.speech_to_text.convert(
            model_id="scribe_v1",  # Model ID for STT
            file=audio_file,
            language_code="ka"  # Georgian language code
        )
    
    print("✅ Transcription successful!\n")
    print(f"Transcribed text: {result.text}")
    print(f"\nOriginal text was: გამარჯობა, მე ვარ ხელოვნური ინტელექტის ოპერატორი.")
    
except Exception as e:
    print(f"❌ Error: {e}")