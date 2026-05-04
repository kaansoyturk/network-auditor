import urllib.request
import json

# Sorgu önbelleği — aynı IP'yi tekrar tekrar sorgulamayalım
cache = {}

def get_location(ip):
    # Yerel IP'leri atla
    if ip.startswith("192.168") or ip.startswith("10.") or ip.startswith("127."):
        return "Yerel Ağ"

    # Önbellekte varsa direkt döndür
    if ip in cache:
        return cache[ip]

    try:
        url = f"http://ip-api.com/json/{ip}?fields=country,city,isp"
        with urllib.request.urlopen(url, timeout=2) as response:
            data = json.loads(response.read())

        if data.get("country"):
            location = f"{data['city']}, {data['country']} ({data['isp']})"
        else:
            location = "Bilinmiyor"

        cache[ip] = location
        return location

    except:
        return "Sorgulanamadı"
    