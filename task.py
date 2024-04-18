from celery import Celery
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




# Create Celery instance
celery = Celery('tasks', broker='redis://localhost:6379/0')

# Email configuration
email_host_user = 'abhisheksuda123@gmail.com'
email_host_password = 'eduq yzha uota wayx'
email_host = 'smtp.gmail.com'
email_port = 587

@celery.task
def send_email(receiver_email, subject, body):
    try:
        # Set up the SMTP server
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_host_user, email_host_password)

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = email_host_user
        msg['To'] = receiver_email

        # Attach body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Send the message via the SMTP server
        server.sendmail(email_host_user, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Failed to send email:", str(e))
