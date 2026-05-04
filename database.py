import sqlite3
from datetime import datetime

DB_NAME = "network_auditor.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS packets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            size INTEGER
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            alert_type TEXT,
            src_ip TEXT,
            detail TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Veritabanı hazır!")

def log_packet(src_ip, dst_ip, protocol, size):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO packets VALUES (NULL,?,?,?,?,?)",
              (datetime.now().isoformat(), src_ip, dst_ip, protocol, size))
    conn.commit()
    conn.close()

def log_alert(alert_type, src_ip, detail):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO alerts VALUES (NULL,?,?,?,?)",
              (datetime.now().isoformat(), alert_type, src_ip, detail))
    conn.commit()
    conn.close()

def get_recent_packets(limit=50):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM packets ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows

def get_alerts():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 50")
    rows = c.fetchall()
    conn.close()
    return rows
