import os
import time
import datetime
import json
import requests

import webbrowser
import pyaudio
import wave
import speech_recognition as sr # voice recognition
import pyttsx3 as tts           # Text to Speech
import wikipedia

import subprocess
import wolframalpha

from ecapture import ecapture as ec

engine = tts.init('sapi5') # nsss for mac
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

# speak info
def main():
    speak(get_command)

# return information from command
def get_command (command):
    c = command.split()
    return info

# speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# recognizes mic input
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Expection: " + str(e))

    return said

# returns string weather
def get_weather(place):

# returns list time with
# [[hour,hour], [minute, minute]]

def get_time():

# activates alarm
def set_alarm(time):

# returns date with format
# [weekday, month, day, year] (speak in same format)
def get_date():

# get information from wiki or google
# return string of paragraph (info) from keywords
def get_info(keywords):

# search video from keywords on youtube
def get_youtube(keywords):

def greeting():
    hour = datetime.datetime.now().hour

    speak("Hello Daisy, Good Morning")
    print("Hello Justin, Good Morning")

if __name__ == "__main__":
    main()
