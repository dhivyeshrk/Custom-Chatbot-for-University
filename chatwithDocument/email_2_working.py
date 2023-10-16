# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = ""  #sender email address
email_password = ""  # sender email password

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = ''
msg['To'] = ""
msg.set_content("This is email message")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)
