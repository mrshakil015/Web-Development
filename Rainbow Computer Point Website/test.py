from datetime import datetime
import pytz

bangladesh_timezone = pytz.timezone('Asia/Dhaka')
now_in_bangladesh = datetime.now(bangladesh_timezone)
admissiondate = now_in_bangladesh.strftime('%d-%m-%Y')
print("Current date: ",admissiondate)
