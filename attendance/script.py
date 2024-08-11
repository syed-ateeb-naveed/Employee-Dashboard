import random
from .models import *
import random
from datetime import datetime, timedelta

def create_employee_login():
    departments = ["Software", "Computer Systems", "Mechanical", "Electrical", "Civil"]
    designations = ["Professor", "Associate Professor", "Assistant Professor", "Lecturer", "Lab Assistant"]
    names = ["John Doe", "Jane Doe", "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Mallory", "Oscar", "Peggy", "Trent", "Walter", "Wendy"]
    password = "123456"

    for id in range(6, 18):
        emp = EMPLOYEE_LOGIN()
        emp.EMP_DIG_ID = id
        emp.EMP_PNO = id
        emp.EMP_NAME = random.choice(names)
        emp.EMP_DESIGNATION = random.choice(designations)
        emp.EMP_DEPTT = random.choice(departments)
        emp.EMP_PASSWORD = password
        emp.save()

def create_attendance():
    for id in range(1, 17):
        att = EMP_ATTENDANCE_REC()
        att.EMP_DIG_ID = EMPLOYEE_LOGIN.objects.get(EMP_DIG_ID=id)
        checkin_time = datetime.strptime("08:00:00", "%H:%M:%S") + timedelta(minutes=random.randint(0, 90))
        checkout_time = datetime.strptime("15:00:00", "%H:%M:%S") + timedelta(minutes=random.randint(0, 60))
        current_date = datetime.now().date()
        att.EMP_CHECKIN_DATETIME = checkin_time.replace(year=current_date.year, month=current_date.month, day=current_date.day).strftime("%Y-%m-%d %H:%M:%S")
        att.EMP_CHECKOUT_DATETIME = checkout_time.replace(year=current_date.year, month=current_date.month, day=current_date.day).strftime("%Y-%m-%d %H:%M:%S") if random.choice([True, False]) else None
        att.save()