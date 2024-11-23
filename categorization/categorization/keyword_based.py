def categorize_news(news_text):
    """
    Haber metinlerini anahtar kelimelerle kategorilere ayırır.
    :param news_text: Haber metni (string).
    :return: Haber kategorisi (string).
    """
    # Kategoriler ve anahtar kelimeler
    categories = {
        "Spor": ["futbol", "basketbol", "tenis", "olimpiyat", "spor"],
        "Ekonomi": ["borsa", "ekonomi", "dolar", "piyasa", "yatırım"],
        "Teknoloji": ["yapay zeka", "teknoloji", "gadget", "inceleme", "yazılım"],
        "Dünya": ["dünya", "uluslararası", "ülkeler", "kriz", "savaş"],
        "Politika": ["seçim", "hükümet", "politika", "meclis", "kanun"],
    }

    # Küçük harfe çevirerek metni normalize et
    news_text = news_text.lower()

    # Kategorileri kontrol et
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in news_text:
                return category  # İlk eşleşen kategori döndürülür

    # Eğer hiçbiri eşleşmezse 'Genel' kategorisi atanır
    return "Genel"
