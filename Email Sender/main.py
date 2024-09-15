# import lib
from smtplib import SMTP
from email.mime.text import MIMEText
import password_manager
#
# #
password = password_manager.password
subject = "Hello Praveen"
body = "Connection Successfully"
msg = MIMEText(body, "plain")
msg['From'] = "pk9777066@gmail.com"
msg["To"] = "praveentechci2023@gmail.com"
msg["Subject"] = subject
#
# #
with SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user= "pk9777066@gmail.com", password=password)
    connection.sendmail(from_addr="pk9777066@gmail.com",
                        to_addrs="praveentechci2023@gmail.com",
                        msg=msg.as_string())
print("Send Successfully")


i
