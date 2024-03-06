# Mail yollama uygulaması
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = 'gonderen_email_adresi@gmail.com'
password = 'gonderen_email_sifresi'
to_email = 'alici_email_adresi@gmail.com'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = to_email
msg['Subject'] = 'Python SMTP Modülü ile Gönderilen E-posta'

body = 'Merhaba,\n\nBu bir Python SMTP modülü ile gönderilen test e-postasıdır.'

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, to_email, text)
server.quit()

print('E-posta gönderildi!')