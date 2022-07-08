from datetime import datetime
import qrcode
import smtplib
import imghdr
from email.message import EmailMessage
import pandas as pd

today = datetime.now()
d1 = today.strftime("%d/%m/%y")

list1 = [i for i in range(201, 272)]
for j in list1:
    k = str(j)
    k = k+" "
    img = qrcode.make(k + d1)
    stk = "attendence of "+k+".jpg"
    img.save(stk)

df = pd.read_csv(r"C:\\Users\\Dell\\Desktop\\sanskar\\python mini project\\Book1.csv")
for i in range(0, len(df.axes[0])):
    j = df.email[i]

    msg = EmailMessage()
    msg['Subject'] = 'Qr code for '+d1
    msg['From'] = 'sanskars.cse20@sbjit.edu.in'
    msg['To'] = j
    msg.set_content("Scan this Qr code to mark your attendance for "+d1)
    k = df.roll[i]
    k = str(k)
    location = "C:\\PythonMiniProject\\miniproject\\attendence of "+k+" .jpg"
    with open(location, "rb") as m:
        file_data = m.read()
        file_type = imghdr.what(m.name)
        file_name = m.name
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('sanskars.cse20@sbjit.edu.in', 'party hard')
        smtp.send_message(msg)
    print("mail sent to "+j)
