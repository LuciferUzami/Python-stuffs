from smtplib import SMTP
from email.mime.text import MIMEText
import requests
import password_manager as passwords
import time


# function for email sending
def emailSender():
    subject = "ISS finder message"
    body = "Get out from home bro ISS on your head TOP"
    my_email = "your email"
    respond_email = "receiver email"
    password = passwords.password
    # Create object
    msg = MIMEText(body, "plain")
    #  Add
    msg["Subject"] = subject
    msg["From"] = my_email
    msg["To"] = respond_email
    # Set connection
    with SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=respond_email,
                            msg=msg.as_string())

    print("Send")


# This function for get ISS currect lat and lon location
def locationForISS():
    # ISS API url
    respond = requests.get(url="http://api.open-notify.org/iss-now.json")
    respond.raise_for_status()

    # Get ISS lon and lat
    iss_longitude = respond.json()["iss_position"]["longitude"]
    iss_latitude = respond.json()["iss_position"]["latitude"]
    #
    return [iss_latitude, iss_longitude]

# Run program after 60 second per day
while True:
    # sleep 60 Seconds
    time.sleep(60)

    # Get my lon and lat
    home_longitude = "your longitude location"
    home_latitude = "your latitude location"

    # Call ISS location function
    longitude = float(locationForISS()[1])
    latitude = float(locationForISS()[0])

    # Compare my location and ISS location
    if (home_latitude + 5 <= latitude or home_longitude + 5 <= longitude and
            home_latitude - 5 <= latitude or home_longitude - 5 <= longitude):
        # Send email
        emailSender()
