import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from .models import Student
from attendence_sys.models import Student
   
def send_email(to, names):

    info = [["ID", "First Name", "Last Name"]]
    for id in names:
        print(id)
        st = Student.objects.get(registration_id = id)
        info.append([id,st.firstname,st.lastname])
        
    print(info)

    with open('Attendance.csv','w') as f:
        for row in info:
            for x in row:
                f.write(str(x) + ',')
            f.write('\n')

    fromaddr = "cmpe272.face.recognition@gmail.com"
    toaddr = to

    msg = MIMEMultipart()

    msg['From'] = fromaddr

    msg['To'] = toaddr

    msg['Subject'] = "Attendance data"

    body = "PFA Attendance"

    msg.attach(MIMEText(body, 'plain'))

    filename = "Attendance.csv"
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