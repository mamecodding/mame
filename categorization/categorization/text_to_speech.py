from elevenlabs import ElevenLabs

client = ElevenLabs(api_key="sk_f771057c6b8f381cafadbdecf0b5079c489810070ee88402")

def speak_news(news_text, filename="output.mp3"):
    """
    Metni seslendirme (Şu an sadece yazılı çıktı alır)
    """
    # Sadece metni yazdırıyoruz
    print(news_text)

    # Ses dosyasını oluşturma
    try:
        audio = client.generate(
            text=news_text,
            voice="Sultan - Charming, Seductive Narrator",
            model="eleven_multilingual_v2"
        )
        audio_bytes = b"".join(audio)
        with open(filename, "wb") as f:
            f.write(audio_bytes)
        print(f"Ses başarıyla oluşturuldu ve {filename} dosyasına kaydedildi.")
    except Exception as e:
        print(f"Ses oluşturma hatası: {e}")
