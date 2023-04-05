import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailSender:
    def __init__(self, smtp_server, port):
        self.smtp_server = smtp_server
        self.port = port
        self.check_server()


    def check_server(self):
        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                print("\nAlright you con connect to SMTP_SERVER")
        except:
            exit("\nWarning! your parameters are uncorrect\n")


    def login(self, username, password):
        self.username = username
        self.password = password
        self.check_login()


    def check_login(self):
        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(self.username, self.password)
                print('SMTP server connection successful!')
        except:
            exit('SMTP server connection error: bad username or password')


    def send(self, receiver, subject, body):
        message = MIMEMultipart()
        message['From'] = self.username
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(self.username, receiver, message.as_string())
                print(f"Mail to {receiver} sended")
        except Exception as e:
            print(f"Warning! Something went wrong with sending mail to {receiver}")