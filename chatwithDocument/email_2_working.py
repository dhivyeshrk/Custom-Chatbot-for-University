# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "dhivyesh21bcs84@iiitkottayam.ac.in"
email_password = "jesusloves"

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = 'dhivyesh.rk@gmail.com'
msg['To'] = "dhivyesh.rk@gmail.com"
msg.set_content("This is email message")

# send email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)