import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_USER = "kaannsoyturk@gmail.com"
GMAIL_APP_PASSWORD = "bjaoaugmzbyfrilv"
ALERT_RECIPIENT = "kaannsoyturk@gmail.com"

def send_alert_email(alert_type, src_ip, detail):
    try:
        msg = MIMEMultipart()
        msg["From"] = GMAIL_USER
        msg["To"] = ALERT_RECIPIENT
        msg["Subject"] = f"🚨 Network Auditor Uyarısı: {alert_type}"

        body = f"""
Network Auditor bir şüpheli aktivite tespit etti!

🔴 Uyarı Türü : {alert_type}
🌐 Kaynak IP  : {src_ip}
📋 Detay      : {detail}

Bu mail otomatik olarak gönderilmiştir.
        """

        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, ALERT_RECIPIENT, msg.as_string())
        server.quit()

        print(f"📧 Uyarı maili gönderildi: {alert_type} - {src_ip}")

    except Exception as e:
        print(f"❌ Mail gönderilemedi: {e}")