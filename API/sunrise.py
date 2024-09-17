import requests
import datetime as dt

parameters = {
    "lat": 11.099276,
    "lng": 439.799993,
    "date": "today",
    "formatted": 1,
}

respond = requests.get(url="https://api.sunrise-sunset.org/json",
                       params=parameters)
respond.raise_for_status()

# Current time
currentHours = dt.datetime.now().time().strftime("%H")
print(currentHours)


# Sunrise and Sunset time
sunrise = respond.json()["results"]["sunrise"]
sunset = respond.json()["results"]["sunset"]

print(sunrise)
print(sunset)
