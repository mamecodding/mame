def categorize_news(news):
    """
    Haberleri anahtar kelimelerle kategorilere ayırır.
    :param news: Haberlerin listesi.
    :return: Kategorize edilmiş haberler (dict).
    """
    # Kategoriler ve anahtar kelimeler
    categories = {
        "Spor": ["futbol", "basketbol", "tenis", "olimpiyat", "spor"],
        "Ekonomi": ["borsa", "ekonomi", "dolar", "piyasa", "yatırım"],
        "Teknoloji": ["yapay zeka", "teknoloji", "gadget", "inceleme", "yazılım"],
        "Dünya": ["dünya", "uluslararası", "ülkeler", "kriz", "savaş"],
        "Politika": ["seçim", "hükümet", "politika", "meclis", "kanun"],
    }

    categorized = {category: [] for category in categories}
    categorized["Genel"] = []

    for article in news:
        title = article['name'].lower()  # Başlığı küçük harfe çevir
        matched = False
        for category, keywords in categories.items():
            if any(keyword in title for keyword in keywords):
                categorized[category].append(article)
                matched = True
                break
        if not matched:
            categorized["Genel"].append(article)

    return {k: v for k, v in categorized.items() if v}
