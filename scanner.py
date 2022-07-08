import cv2
from pyzbar.pyzbar import decode
import pandas as pd
from datetime import datetime


present = []
capture = cv2.VideoCapture(0)
received_data = None
while True:
    _, frame = capture.read()

    decoded_data = decode(frame)
    try:
        data = (decoded_data[0][0])
        if data != received_data:
            present.append(data)
            received_data = data
            print(received_data)
    except:
        pass

    cv2.imshow('QR Code Scanner', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

attendance = []
present_students = []
present = set(present)
present = list(present)
present.sort()
today = datetime.now()
d1 = today.strftime("%d/%m/%y")
for i in present:
    str1 = i.decode('UTF-8')
    present_students.append(str1)
for i in present_students:
    if d1 not in i:
        present_students.remove(i)

for i in range(0, len(present_students)):
    present_students[i] = (present_students[i].removesuffix(d1))

total_students = [i for i in range(201, 272)]

for i in range(0, len(present_students)):
    present_students[i] = int(present_students[i])

for i in total_students:
    if i in present_students:

        attendance.append("p")
    else:
        attendance.append("a")

excel_file_path = "C:\\Users\\Dell\\Desktop\\sanskar\\python mini project\\present.csv"
df = pd.read_csv(excel_file_path)
df[d1] = attendance
df.to_csv(excel_file_path, index=False)
