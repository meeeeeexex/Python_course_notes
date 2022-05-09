import smtplib

PORT = 587
SMTP_SERVER = "smtp.gmail.com"
SENDER_MAIL = "somemail@gmail.com"
PASSWORD = 'testrestapi564'


def send_message(receiver_email, message_text):
    print('Message sent')
    with smtplib.SMTP(SMTP_SERVER, PORT) as server:
        server.starttls()
        server.login(SENDER_MAIL, PASSWORD)
        server.sendmail(SENDER_MAIL, receiver_email, message_text)
