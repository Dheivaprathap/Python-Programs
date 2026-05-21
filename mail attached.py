import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
sender_email = "dheivaprathap473@gmail.com"
app_password = "uqoe ajzd qwdu xpyj"
receiver_email = "manojimanol2345@example.com"
file_path = "sample.pdf"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Python Email with Attachment"
body = "Hello,\n\nPlease find the attachment."
message.attach(MIMEText(body, "plain"))
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename={file_path}",
)
message.attach(part)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )
    print("Email with attachment sent successfully!")
except Exception as e:
    print("Error:", e)
finally:
    server.quit()
