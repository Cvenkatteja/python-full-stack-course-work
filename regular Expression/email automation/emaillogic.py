import smtplib
import os
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "tejav7236@gamil.com"
SENDER_PASSWORD ="smho ltih amsq suuq"

def send_email(to_email,subject,body,attachment=None):
    try:
        msg = MIMEMultipart()
        msg["from"] = SENDER_EMAIL
        msg["To"] = to_email
        msg["Subject"] =subject
        msgg.attach(MIMEText(body, "plain"))


        if attachments:
            for  file_path in attachments:
                if os.path.exists(file_path):
                    with open(file_path,"rb") as f:
                        mime_base = MIMEBase("application","octet-stream")
                        mime_base.set_payload(f.read())
                        encoders.encode_base64(mime_base)
                        mime_base.add_header(
                            "content-Disportion",
                            f"attachment; filename={os.path.basename(file_path)}"

                         )
                        msg.attach(mime_base)
                else:
                    print(f"File'{file_path}' not found skipping....")




        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL,to_emaiL,msg.as_string())
        server.quit()


        print(f"email sent to {to_email}")


    except Exception as e:
        print(f"Error sending email {to_email}: {e}")
                        


