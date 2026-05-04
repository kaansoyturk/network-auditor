# 🛡️ Network Auditor

Gerçek zamanlı ağ trafiği analiz ve anomali tespit sistemi.

## 🔍 Ne Yapıyor?

- Ağ trafiğini gerçek zamanlı dinler ve kaydeder
- Port tarama saldırılarını tespit eder
- Büyük veri transferlerini tespit eder
- Web dashboard üzerinden canlı izleme sağlar

## 🛠️ Teknolojiler

- **Python 3** — Ana dil
- **Scapy** — Paket yakalama
- **Flask** — Web dashboard
- **SQLite** — Veri depolama

## 🚀 Kurulum

```bash
# Repoyu klonla
git clone https://github.com/kaansoyturk/network-auditor.git
cd network-auditor

# Sanal ortam oluştur
python3 -m venv venv
source venv/bin/activate

# Kütüphaneleri yükle
pip install scapy flask
```

## ▶️ Kullanım

Terminal 1 — Paket yakalama:
```bash
sudo venv/bin/python3 capture.py
```

Terminal 2 — Dashboard:
```bash
python3 app.py
```

Tarayıcıda aç: `http://localhost:5050`

## 📸 Özellikler

- ✅ Gerçek zamanlı paket izleme
- ✅ Port tarama tespiti
- ✅ Büyük transfer uyarısı
- ✅ Web tabanlı dashboard
- ✅ SQLite veritabanı kaydı

## 👨‍💻 Geliştirici

Kaan Soytürk — [github.com/kaansoyturk](https://github.com/kaansoyturk)