import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = "dheivaprathap473@gmail.com"
app_password = "toog pcix boiu ruyl"
receiver_email = "manojimanol2345@example.com"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"
body = "Hello! This email was sent using Python SMTP and Gmail App Password."
message.attach(MIMEText(body, "plain"))
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print("Error:", e)
finally:
    server.quit()
