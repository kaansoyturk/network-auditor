from collections import defaultdict
from database import log_alert
from emailer import send_alert_email
import time

packet_count = defaultdict(list)

PORT_SCAN_THRESHOLD = 20
LARGE_TRANSFER_BYTES = 500000

# Aynı IP için tekrar tekrar mail atmasın
alerted_ips = set()

def analyze(src_ip, dst_ip, protocol, size):
    now = time.time()

    packet_count[src_ip] = [t for t in packet_count[src_ip] if now - t < 10]
    packet_count[src_ip].append(now)

    # Port tarama tespiti
    if len(packet_count[src_ip]) > PORT_SCAN_THRESHOLD:
        detail = f"{len(packet_count[src_ip])} paket/10sn"
        log_alert("PORT_SCAN", src_ip, detail)
        print(f"[⚠️  UYARI] Port tarama tespit edildi: {src_ip}")

        if src_ip not in alerted_ips:
            send_alert_email("PORT_SCAN", src_ip, detail)
            alerted_ips.add(src_ip)

    # Büyük transfer tespiti
    if size > LARGE_TRANSFER_BYTES:
        detail = f"{size} byte → {dst_ip}"
        log_alert("LARGE_TRANSFER", src_ip, detail)
        print(f"[⚠️  UYARI] Büyük veri transferi: {src_ip} → {dst_ip} ({size} byte)")

        if src_ip not in alerted_ips:
            send_alert_email("LARGE_TRANSFER", src_ip, detail)
            alerted_ips.add(src_ip)