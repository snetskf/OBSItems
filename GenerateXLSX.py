import smtplib
from email import encoders
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

def SendEmail(filepath,name):

    smtpServer = 'mailrelay.skf.com'
    fromAddr = 'bhavdip.shah@skf.com'
    toAddr = 'bhavdip.shah@skf.com;bhavdeep.sh31@gmail.com'
    #text = "This is a report of OBSItems branch 4470."
    server = smtplib.SMTP('mailrelay.skf.net:25')
    msg = MIMEMultipart()
    msg['From'] = fromAddr
    msg['To'] = toAddr
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = name
   # msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename='+str(name)+'')
    msg.attach(part)
    server.ehlo()
    server.send_message(msg)
    server.quit()
#
