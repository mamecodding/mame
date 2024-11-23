import http.client
import json

def fetch_news(api_key, country='tr', tag='general', page_size=1):
    """
    CollectAPI üzerinden haberleri çeker.

    Args:
        api_key (str): API anahtarı
        country (str): Ülke kodu (varsayılan Türkiye - 'tr')
        tag (str): Haber kategorisi (varsayılan 'general')
        page_size (int): Çekilecek haber sayısı (varsayılan 5)

    Returns:
        list: Haberlerin bir listesi (başlık, açıklama, kaynak ve URL içerir)
    """
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': f"apikey {api_key}"
    }

    try:
        # API'den haberleri çekiyoruz
        conn.request("GET", f"/news/getNews?country={country}&tag={tag}", headers=headers)
        res = conn.getresponse()

        # Eğer API isteği başarılı değilse hata mesajı yazdırılır
        if res.status != 200:
            print(f"API isteği başarısız oldu. Durum Kodu: {res.status}")
            return None

        # API yanıtını alıyoruz
        data = res.read()

        try:
            # JSON formatında veriyi çözümleyip, haberlerin listesini çıkarıyoruz
            articles = json.loads(data.decode("utf-8")).get("result", [])
        except json.JSONDecodeError:
            print("API yanıtı JSON formatında değil.")
            return None

        # Eğer haberler varsa, istenilen sayıda haber döndürüyoruz
        if articles:
            return articles[:page_size]
        else:
            print("Haberler bulunamadı veya API hatası oluştu.")
            return None
    except Exception as e:
        # Hata durumunda mesaj yazdırıyoruz
        print(f"API isteği sırasında hata oluştu: {e}")
        return None
    finally:
        # Bağlantıyı kapatıyoruz
        conn.close()
