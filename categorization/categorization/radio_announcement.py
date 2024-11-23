from datetime import datetime
import locale
from fetch_weather import fetch_weather
import re

def clean_weather_description(weather_desc):
    """
    Hava durumu açıklamalarındaki gereksiz kısımları temizler.
    Örneğin 'Açıklama:' ve sonrasını siler.
    """
    # 'Açıklama:' ifadesini ve sonrasını temizler
    cleaned_desc = re.sub(r'\bAçıklama:[^\n]*', '', weather_desc)
    return cleaned_desc

def radio_announcement(city='Elazığ', api_key='fdabba8dfb28bdcd5ad4fc12a0c30fcb'):
    # Locale ayarı
    locale.setlocale(locale.LC_TIME, "tr_TR.UTF-8")

    # Güncel tarih ve saat bilgisi
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    weekday = now.strftime("%A")

    # Hava durumu bilgisi
    weather = fetch_weather(city, api_key)
    if weather:
        weather_desc, temp = weather
        weather_desc = clean_weather_description(weather_desc)  # Hava durumu açıklamasını temizle
        temp = round(temp)  # Sıcaklık tam sayıya yuvarlanır (kesirli kısımdan kurtulmak için)
        weather_info = f"{city} için hava durumu: {weather_desc}, sıcaklık: {temp} derece."
    else:
        weather_info = "Hava durumu bilgisi alınamadı."

    # Selamlama metni (Saat kısmında virgül ekledik)
    greeting = (
        f"Merhaba sevgili dinleyenler, bugün günlerden {weekday}. "
        f"Saat şu an {current_hour} {current_minute}, {weather_info}"  # Nokta yerine virgül
    )
    return greeting
