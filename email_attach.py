import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
   
def send_email(to, filename):
    fromaddr = "cmpe272.face.recognition@gmail.com"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Attendance data"

    body = "PFA Attendance"

    msg.attach(MIMEText(body, 'plain'))

    filename = filename
    attachment = open(filename, "rb")

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, "cmpe272g19")

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()