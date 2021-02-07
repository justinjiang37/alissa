import os
import time
import datetime
from datetime import datetime
import json
import requests
import pytz
import random

from countryinfo import CountryInfo
import webbrowser
import pyaudio
import wave
import speech_recognition as sr  # voice recognition
import pyttsx3 as tts           # Text to Speech
import wikipedia

import subprocess
import wolframalpha

import geocoder

from ecapture import ecapture as ec

with open("../../weatherstack_api.txt", "r") as apiKey:
    key = apiKey.readlines()
key = key[0]
baseURL = "http://api.weatherstack.com/"
getWeatherUrl = baseURL + "/current?access_key=" + key

country = "canada"
capital = CountryInfo(country).capital()
response = requests.get(getWeatherUrl + "&query=" + capital)
response = response.json()
time = "The time in " + country + " right now is " + \
    response['location']['localtime'][11:13] + " " +\
    response['location']['localtime'][14:]
print(response)
print(time)
