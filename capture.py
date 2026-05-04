from scapy.all import sniff, IP, TCP, UDP
from database import init_db, log_packet
from detector import analyze

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        else:
            protocol = "OTHER"

        log_packet(src_ip, dst_ip, protocol, size)
        analyze(src_ip, dst_ip, protocol, size)
        print(f"[+] {protocol} | {src_ip} → {dst_ip} | {size} byte")

if __name__ == "__main__":
    init_db()
    print("🔍 Ağ trafiği dinleniyor... (Durdurmak için Ctrl+C)")
    sniff(prn=process_packet, store=False)