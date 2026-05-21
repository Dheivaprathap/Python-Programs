import smtplib
import schedule
import time
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def send_email():
    sender_email = "dheivaprathap473@gmail.com"
    app_password = "fsvx aypr pofp zevs"
    receiver_email = "receiver@gmail.com"
    file_path = "sample.pdf"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Scheduled Email from Python"
    body = "Hello,\n\nThis email was sent automatically with attachment."
    message.attach(MIMEText(body, "plain"))
    if os.path.exists(file_path):
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(file_path)}"
        )
        message.attach(part)
    else:
        print("Attachment file not found!")
        return
    server = None
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email,app_password)
        server.sendmail(
            sender_email,
            receiver_email,
            message.as_string()
        )
        print("Email sent successfully!")
    except Exception as e:
        print("Error:", e)
    finally:
        if server:
            server.quit()
schedule.every().day.at("18:30").do(send_email)
print("Scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(1)
