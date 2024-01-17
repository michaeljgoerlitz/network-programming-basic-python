import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

print('0')
load_dotenv()
print('0.5')

to_email = os.getenv('TO_EMAIL')
from_email = os.getenv('FROM_EMAIL')
password = os.getenv('PASSWORD')
app_password = os.getenv('GOOGLE_APP_PASSWORD')
print('0.7')

server = smtplib.SMTP('smtp.gmail.com', 587)
print('1')

server.starttls()  # Secure the connection
print('1.5')
server.ehlo() # starts the server process
print('2')

# want to log into account
# use .env
server.login(from_email, app_password)
print('3')

msg = MIMEMultipart()
msg['From'] = 'Michael Goerlitz'
msg['To'] = to_email
msg['Subject'] = 'Subject for Test Email'

with open('message.txt', 'r') as f:
    message = f.read()
print('4')

msg.attach(MIMEText(message, 'plain'))
print('5')

filename = 'coding.jpg'
attachment = open(filename, 'rb')
print('6')

p = MIMEBase('application', 'octet-stream') # payload object
p.set_payload(attachment.read())
print('7')

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
print('8')
msg.attach(p)
print('9')

text = msg.as_string()
print('10')
server.sendmail(from_email, to_email, text)
print('11')


