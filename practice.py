import smtplib, ssl
import certifi

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "developersatinder@gmail.com"  # Enter your address
receiver_email = "satindersingh772@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
hello this is my new email."""

context = ssl.create_default_context()
context.load_verify_locations(certifi.where())
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)