from elevenlabs import play
from elevenlabs.client import ElevenLabs

client = ElevenLabs(
  api_key="sk_28cf9575d9f9eab5e7204a4689f1714f6cc656fa6fad3789", # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
  text="Türkiye'de teknoloji hızla gelişiyor. 2024 yılında birçok yenilik bekleniyor.",
  voice="Sultan - Charming, Seductive Narrator",
  model="eleven_multilingual_v2"
)
play(audio)