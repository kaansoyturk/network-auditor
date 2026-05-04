from collections import defaultdict
from database import log_alert
import time

# Her IP'nin son 10 saniyedeki paket sayısını tut
packet_count = defaultdict(list)

PORT_SCAN_THRESHOLD = 20  # 10 sn içinde 20+ paket → şüpheli
LARGE_TRANSFER_BYTES = 500000  # 500 KB üzeri → uyarı

def analyze(src_ip, dst_ip, protocol, size):
    now = time.time()

    # Eski kayıtları temizle (10 saniye öncesi)
    packet_count[src_ip] = [t for t in packet_count[src_ip] if now - t < 10]
    packet_count[src_ip].append(now)

    # Port tarama tespiti
    if len(packet_count[src_ip]) > PORT_SCAN_THRESHOLD:
        log_alert("PORT_SCAN", src_ip, f"{len(packet_count[src_ip])} paket/10sn")
        print(f"[⚠️  UYARI] Port tarama tespit edildi: {src_ip}")

    # Büyük transfer tespiti
    if size > LARGE_TRANSFER_BYTES:
        log_alert("LARGE_TRANSFER", src_ip, f"{size} byte → {dst_ip}")
        print(f"[⚠️  UYARI] Büyük veri transferi: {src_ip} → {dst_ip} ({size} byte)")