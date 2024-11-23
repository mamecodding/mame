import http.client
import json
from urllib.parse import quote

def fetch_weather(city, api_key):
    """
    OpenWeather API'den hava durumu verilerini çeker. Şehir ve API anahtarı parametre olarak alınır.
    """
    city_encoded = quote(city)  # Şehir isminde Türkçe karakterler olabilir, bunları encode eder
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    endpoint = f"/data/2.5/weather?q={city_encoded}&appid={api_key}&lang=tr&units=metric"

    try:
        conn.request("GET", endpoint)
        res = conn.getresponse()
        if res.status != 200:
            print(f"Hata: API isteği başarısız oldu. Kod: {res.status}")
            return None

        data = json.loads(res.read().decode("utf-8"))
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        return weather, temp
    except Exception as e:
        print(f"API isteği sırasında hata: {e}")
        return None
