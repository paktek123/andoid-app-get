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
    current_prayer = soup.findAll(True, {'class':['current']})
    fajr = current_prayer[0].contents[3].contents[0].get_text()
    sunrise = current_prayer[0].contents[3].contents[2].get_text()
    duhr = current_prayer[0].contents[5].contents[0].get_text()
    asr = current_prayer[0].contents[7].contents[0].get_text()
    maghrib = current_prayer[0].contents[9].contents[0].get_text()
    isha = current_prayer[0].contents[11].contents[0].get_text()

    prayer_json = {
                    "fajr": fajr,
                    "sunrise": sunrise,
                    "duhr": duhr,
                    "asr": asr,
                    "maghrib": maghrib,
                    "isha": isha
                  }

    return flask.jsonify(**prayer_json)
            



