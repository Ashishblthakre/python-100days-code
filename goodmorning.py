import time
from datetime import datetime
current_datetime = datetime.now()
time_hour = int(current_datetime.strftime("%H"))
if time_hour>0 and time_hour<=5:
    print("Good night sir")
elif time_hour>5 and time_hour<=12:
    print("Good Morning sir")
elif time_hour>12 and time_hour<17:
    print("Good afternoon sir")
else:
    print("Good Evening or good night")
