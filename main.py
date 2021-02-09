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

from functions import getWeather, getWeatherHelper
from functions import getTime, getTimeHelper
from functions import getInfo, getInfoHelper
from functions import easterEggs

from audioInit import speak, getAudio

'''
PUrpose of this main file is to initialize and call the
need instantiation for this program. Afterwards it will run a loop
where it constantly listens for input, and then makes calls into the
functions.py file where all of the function logic will lie.
All of the function logic will be separated by methods as finely as possible
and paired with perfect logging.

Mkae another file for running the voice logic and settings.
Basically extrapolate all of your functions into as many pieces.
'''

def main():
    speak(getCommand(getAudio()))

def getCommand(command):
    command = command.lower().split()

    if "weather" in command:
        return getWeather(command)

    if "time" in command:
        return getTime(command)

    # easterEggs(command)

    return getInfo(command)

if __name__ == "__main__":
    main()
