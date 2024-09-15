# import lib
from smtplib import SMTP
from email.mime.text import MIMEText
import password_manager
#
# #
password = "Your password"  # App generating password
subject = "Hello Praveen"
body = "Connection Successfully"
msg = MIMEText(body, "plain")
msg['From'] = "Your email"
msg["To"] = "Reciver eamil"
msg["Subject"] = subject
#
# #
with SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user= "Your email", password=password)
    connection.sendmail(from_addr="Your email",
                        to_addrs="Reciver eamil",
                        msg=msg.as_string())
print("Send Successfully")


i
