from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import os
import pygame
import tempfile
import time

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

VOICE_ID = "jGf6Nvwr7qkFPrcLThmD"   # keep this
MODEL_ID = "eleven_turbo_v2"  # ✅ FREE TIER MODEL

pygame.mixer.init()

def speak(text):
    print("🤍 Tenka:", text)

    audio_stream = client.text_to_speech.convert(
        text=text,
        voice_id=VOICE_ID,
        model_id=MODEL_ID,
        output_format="mp3_44100_128"
    )

    audio_bytes = b"".join(audio_stream)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        f.write(audio_bytes)
        path = f.name

    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
