import requests
from datetime import datetime
import smtplib

MY_LAT =  -23.602669# Your latitude
MY_LONG =  -46.919468# Your longitude
MY_EMAIL = "gustavo.100.days.of.code@gmail.com"
PASSWORD_APP = "ehtrnekaqypuuvkh"

# ISS position
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

 
# Then send me an email to tell me to look up.
if is_iss_overhead() and is_night():
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD_APP)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject:ISS OVER YOUR HEAD\n\nHEY LOOK UP!"
    )

connection = smtplib.SMTP('smtp.gmail.com', 587)
connection.starttls()
connection.login(user=MY_EMAIL, password=PASSWORD_APP)
connection.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
msg="Subject:ISS OVER YOUR HEAD\n\nHEY LOOK UP!"
)

# BONUS: run the code every 60 seconds.



