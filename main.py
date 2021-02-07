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

# speak info

engine = tts.init('sapi5')  # nsss for mac
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 135
engine.setProperty('rate', newVoiceRate)

with open("../../weatherstack_api.txt", "r") as apiKey:
    key = apiKey.readlines()
key = key[0]
baseURL = "http://api.weatherstack.com/"
getWeatherUrl = baseURL + "/current?access_key=" + key

geocoder = geocoder.ip('me')
geocoder = str(geocoder)
geocoder = geocoder[24: -2]
currentLocation = geocoder.split(", ")

# speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# recognizes mic input
def getAudio():
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

def main():
    speak(getCommand(getAudio()))

# return information from command
def getCommand(command):
    str_command = command.lower()
    command = command.lower().split()

    '''
    Weather
    '''
    with open("cities.txt", 'r', encoding='utf8') as cities:
        data = cities.read()
        cities = data.splitlines()
        countries = open("countries.txt", "r").read()
        if "weather" in command:
            currentCity = currentLocation[0]
            print(command)
            for possibleCity in command:
                if possibleCity in cities:
                    currentCity = possibleCity
                    return getWeather(currentCity)
            for possibleCountry in command:
                if possibleCountry in countries:
                    currentCountry = possibleCountry
                    currentCountry = CountryInfo(currentCountry)
                    return getWeather(currentCountry.capital())
            return getWeather(currentCity)

    '''
    Time
    '''
    with open("countries.txt", "r") as countries:
        data = countries.read()
        countries = data.splitlines()
        if "time" in command:
            for country in command:
                if country in countries:
                    return getTime(country)
            return getTime("Canada")

    '''
    alarm
    '''
    # if "set" in command or "alarm" in command:
    #     # get th time user wants to set at in command
    #     # call set alarm method


    '''
    Easter eggs
    '''
    # dad
    if "i'm" in command:
        dad = "Hi "
        for i in range(1, len(command)):
            dad += command[i]
            dad + " "
        dad += "I'm dad."
        return dad
    # love
    if "i" in command and "love" in command and "you" in command:
        i = 0
        if i == 0:
            return "I love you too!   mwah"
        if i == 1:
            return "Thanks! I think you're pretty cute too"
        if i == 2:
            return "I am yours forever"
        if i == 3:
            return "Sorry I already have a boy friend"
        if i == 4:
            return "Nah im out of your league"
    if "who" in command and "your" in command and "boyfriend" in command:
        return "Justin Jiang is my long eternal love"
    # joke
    if "tell" in command and "joke" in command:
        return "Why did the chicken cross the road! to get to the other side! haha"
    # CIA
    # print("hi")
    # if "CIA" in command and "listening" in command:
    #     print("hi")
    #     return "The CIA is always listening! Always"

    '''
    wiki
    '''
    keywords = ""
    for i in command:
        keywords += i
        keywords + " "
    return get_info(keywords)



def getWeather(city):
    response = requests.get(getWeatherUrl + "&query=" + city)
    response = response.json()
    weather = "In " + response['location']['name'] + \
        ", " + response['location']['country'] + " it is currently " + \
        str(response['current']['temperature']) + " degrees with a " + \
        response['current']['weather_descriptions'][0] + "weather."

    return weather


def getTime(country):
    capital = CountryInfo(country).capital()
    response = requests.get(getWeatherUrl + "&query=" + capital)
    response = response.json()
    hour = int(response['location']['localtime'][11:13])
    if hour > 12:
        hour = hour - 12
    time = "The time in " + country + " right now is " + \
        str(hour) + " " +\
        response['location']['localtime'][14:]
    return time


# def set_alarm(time):


# def get_date():


def get_info(keywords):
    return(wikipedia.summary(keywords))

# def get_youtube(keywords):


def greeting():
    hour = datetime.datetime.now().hour

    speak("Hello Daisy, Good Morning")
    print("Hello Justin, Good Morning")

# def map():

if __name__ == "__main__":
    main()
