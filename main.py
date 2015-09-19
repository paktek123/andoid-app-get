import os
import flask
from flask import Flask
import requests
import bs4
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = True

@app.route('/')
def get_prayer_times():
    r = requests.get('http://www.eastlondonmosque.org.uk/')
    soup = BeautifulSoup(r.content)
    current_prayer = soup.findAll('div', attrs={'class':'salah-time-row'})[2]
    fajr = current_prayer.contents[-10].get_text()
    #sunrise = current_prayer.contents[-8].get_text()
    duhr = current_prayer.contents[-8].get_text()
    asr = current_prayer.contents[-6].get_text()
    maghrib = current_prayer.contents[-4].get_text()
    isha = current_prayer.contents[-2].get_text()

    if int(duhr.split(':')[0]) == 11:
      duhr = duhr + " AM"
    else:
      duhr = duhr + " PM"
      

    prayer_json = {
                    "fajr": fajr + " AM",
                    #"sunrise": sunrise,
                    "duhr": duhr,
                    "asr": asr + " PM",
                    "maghrib": maghrib + " PM",
                    "isha": isha + " PM"
                  }

    return flask.jsonify(**prayer_json)
            
if __name__ == "__main__":
      app.run()


