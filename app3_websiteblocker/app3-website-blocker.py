import time
from datetime import datetime as dt

# To run on ...
# Linux or Mac type 'sudo python app3-website-blocker.py'
# Windows open cmd as administrator and type 'python app3-website-blocker.py'

# To run in the background 
# For Windows:
# change file extension to '.pyw' and double click the file
# Seek 'Python' in Task Manager window

# To run application as soon as the computer starts
# For Windows:
# Task Scheduler > Create Task > Run with highest privileges (Administtariv rights)
# > Begin the program : At startup
# > Action: Start a program & choose 'app3-website-blocker.pyw'
#
# For Linux and Mac: use crontab

# Scheduling a Python Program on a Server: https://www.pythonanywhere.com


hosts_temp = r"C:\MyProj\py\app3_websiteblocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
#hosts_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
#hosts_path="/etc/hosts" Linux & Mac OS
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)
