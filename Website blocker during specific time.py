import time
from datetime import datetime as dt

hosts_temp=r"C:\Users\sagar\Desktop\Projects\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.instagram.com","www.youtube.com"]
hosts_original=r"C:\Windows\System32\drivers\etc\hosts"
# print("current blocked websites are", website_list)
# print("Wanna add sites you wana block Y/N")
# ans = input()
# if ans.lower() == 'y':
#
#     print("enter website names, use space for more than one sites")
#     website_list.extend(list(map(str, input().split())))
# print("if you added any website that wasn't already in the list, you should not close this program before the working hours fininsh or the sites will remain blocked!")
while True:
    if 20>dt.now().hour and dt.now().hour>9:
        print("Working hours...")
        file=open(hosts_original,'r+')
        content=file.read()   #this will seek the cursor at the end of the file
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect+" "+ website+"\n")
         file.close()
    else:
        file=open(hosts_original,'r+')
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()  # truncate will get everything withing the index passed from the current cursor,  default will be where the cursor is currently
        print("Fun hours...")
    time.sleep(20)
