import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Streamlit app setup
st.title("Email Sending Demo")

# User input for email details
recipient_email = st.text_input("Recipient Email:")
subject = st.text_input("Subject:")
message = st.text_area("Message:")

# Sender's Gmail credentials
sender_email = 'nived21bcs28@iiitkottayam.ac.in'  # Replace with your Gmail email
sender_password = 'nithu2003'      # Replace with your Gmail password

# Send email function using SMTP and less secure apps (for testing purposes)
def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Create an SMTP server connection to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to your Gmail account
        server.login(sender_email, sender_password)

        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the SMTP server connection
        server.quit()

        return True

    except Exception as e:
        st.error(f"Error: {e}")
        return False

# Send email button
if st.button("Send Email"):
    if send_email(sender_email, sender_password, recipient_email, subject, message):
        st.success(f"Email sent successfully to {recipient_email}!")
    else:
        st.error("Failed to send email. Please check your credentials and try again.")