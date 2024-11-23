import time
from radio_announcement import radio_announcement
from fetch_news import fetch_news
from text_to_speech import speak_news
from pydub import AudioSegment

def combine_audio(audio_files, background_music="background_music.mp3"):
    """
    Birden fazla ses dosyasını birleştirir ve arka planda müzik çalar.
    """
    combined = AudioSegment.empty()

    # Arka plan müziği yükleniyor
    music = AudioSegment.from_mp3(background_music)
    music = music - 5  # Müziğin ses seviyesini düşürüyoruz, -5dB daha az

    # Ses dosyalarını sırayla birleştiriyoruz
    for file in audio_files:
        sound = AudioSegment.from_mp3(file)
        # Müziği tekrar ederek, her ses dosyasına müzik ekliyoruz
        sound_with_music = sound.overlay(music, position=0)  # Arka planda müzik ekleniyor
        combined += sound_with_music

    # Sonuç olarak birleşmiş dosyayı kaydediyoruz
    combined.export("combined_output.mp3", format="mp3")
    print("Ses dosyaları başarıyla birleştirildi ve 'combined_output.mp3' olarak kaydedildi.")

def main():
    city = "Elazığ"  # Şehri buradan değiştirebilirsiniz
    openweather_api_key = "fdabba8dfb28bdcd5ad4fc12a0c30fcb"
    collect_api_key = "apikey 0F8vW3zxeue3CLTwa1n1jV:7IGgUkIfF7tA81YrSkmo4Y"

    # Ses dosyalarını saklamak için liste
    audio_files = []

    # 1. Selamlama ve hava durumu
    announcement = radio_announcement(city=city, api_key=openweather_api_key)
    print(announcement)  # Yazılı çıktı
    speak_news(announcement, filename="announcement.mp3")  # Seslendirme
    audio_files.append("announcement.mp3")  # Bu dosyayı birleştirmek için listeye ekliyoruz

    # 2. Haberler
    news = fetch_news(collect_api_key, country='tr', tag='general', page_size=1)
    if news:
        for idx, article in enumerate(news, start=1):
            title = article.get("name", "Başlık Yok")
            description = article.get("description", "Açıklama Yok")
            news_content = f"{idx}. Haber: {title}. Açıklama: {description}."
            print(news_content)  # Yazılı çıktı
            speak_news(news_content, filename=f"news_{idx}.mp3")  # Seslendirme
            audio_files.append(f"news_{idx}.mp3")  # Bu dosyayı birleştirmek için listeye ekliyoruz
            time.sleep(2)  # Dinleyiciye süre tanıma
    else:
        error_msg = "Haberler çekilemedi."
        print(error_msg)  # Yazılı çıktı
        speak_news(error_msg, filename="error.mp3")  # Seslendirme
        audio_files.append("error.mp3")  # Hata mesajını sesli olarak kaydediyoruz

    # 3. Kapanış mesajı
    closing_message = "Ve böylelikle bugünkü haber bültenimizin sonuna geldik. Dinlediğiniz için teşekkür ederiz. Bir sonraki yayınımızda görüşmek üzere, hoşça kalın!"
    print(closing_message)
    speak_news(closing_message, filename="closing_message.mp3")
    audio_files.append("closing_message.mp3")  # Kapanışı sesli olarak kaydediyoruz

    # Ses dosyalarını birleştiriyoruz, arka plan müziği ekliyoruz
    combine_audio(audio_files, background_music="background_music.mp3")

if __name__ == "__main__":
    main()
