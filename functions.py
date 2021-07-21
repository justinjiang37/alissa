import os
import time
import datetime
from datetime import datetime
import json
import requests
import pytz
import random
import re
from word2number import w2n
from countryinfo import CountryInfo
import wikipedia
import subprocess

from audioInit import speak, getAudio

import geocoder

# init
with open("C:\\Users\\Justi\\OneDrive\\Desktop\\API keys\\weatherstack_api.txt", "r") as apiKey:
    key = apiKey.readlines()
key = key[0]
baseURL = "http://api.weatherstack.com/"
getWeatherUrl = baseURL + "/current?access_key=" + key

geocoder = geocoder.ip('me')
geocoder = str(geocoder)
geocoder = geocoder[24: -2]
currentLocation = geocoder.split(", ")
currentCity = currentLocation[0].lower()
currentCountry = requests.get(
    getWeatherUrl + "&query=" + currentCity).json()['location']['country'].lower()

# put data files in dirve and open with url so it dosent crash
cities = open("data/cities.txt", "r", encoding='utf8').read().splitlines()
countries = open("data/countries.txt", "r",
                 encoding='utf8').read().splitlines()

def getWeather(command):
    for possibleCity in command:
        if possibleCity in cities:
            city = possibleCity
            print(city)
            print(getWeatherHelper(city))
            return getWeatherHelper(city)
    for possibleCountry in command:
        if possibleCountry in countries:
            country = possibleCountry
            country = CountryInfo(country)
            return getWeatherHelper(country.capital())
    return getWeatherHelper(currentCity)

def getWeatherHelper(city):
    response = requests.get(getWeatherUrl + "&query=" + city)
    response = response.json()
    weather = "In " + response['location']['name'] + \
        ", " + response['location']['country'] + " it is currently " + \
        str(response['current']['temperature']) + " degrees with a " + \
        response['current']['weather_descriptions'][0] + "weather."
    return weather


def getTime(command):
    for country in command:
        if country in countries:
            return getTimeHelper(1, country)
    for city in command:
        if city in cities:
            return getTimeHelper(0, city)
    return getTimeHelper(0, currentCity)

def getTimeHelper(id, name):
    if (id == 0):
        response = requests.get(getWeatherUrl + "&query=" + name)
        response = response.json()
        hour = int(response['location']['localtime'][11:13])
        if hour > 12:
            hour = abs(hour - 12)
        time = "The time in " + name + " right now is " +\
            str(hour) + " " +\
            response['location']['localtime'][14:]
        return time

    elif (id == 1):
        capital = CountryInfo(name).capital()
        response = requests.get(getWeatherUrl + "&query=" + capital)
        response = response.json()
        hour = int(response['location']['localtime'][11:13])
        if hour > 12 or hour == 0:
            hour = abs(hour - 12)
        time = "The time in the capital of " + name + " right now is " + \
            str(hour) + " " +\
            response['location']['localtime'][14:]
        return time


def summarize(article):
    final = ""
    # get the number of sentences
    sentence_break = ". "
    numSentences = article.count(sentence_break)
    # regex - regular expression
    article = re.sub("[\(\[].*?[\)\]]", "", article)
    if numSentences <= 4:
        return article
    else:
        sentences = article.split(". ")
        for i in range(2):
            final += sentences[i] + ". "
    return final

def getInfo(command):
    if ("who" in command):
        for word in command:
            if (word == "who"):
                command = command[command.index("who") + 2:]
        keywords = ""
        for i in command:
            keywords += i
            keywords += " "
        return summarize(wikipedia.summary(keywords))
    if ("where" in command):
        for word in command:
            if (word == "where"):
                command = command[command.index("where") + 2:]
        keywords = ""
        for i in command:
            keywords += i
            keywords += " "
        return summarize(wikipedia.summary(keywords))
    if ("how" in command):
        for word in command:
            if (word == "how"):
                command = command[command.index("how") + 2:]
        keywords = ""
        for i in command:
            keywords += i
            keywords += " "
        return summarize(wikipedia.summary(keywords))

def getInfoHelper(keywords):
    return(wikipedia.summary(keywords))

def setTimer(command):
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
    ]

    tens = ["", "", "twenty", "thirty", "forty",
            "fifty", "sixty", "seventy", "eighty", "ninety"]

    scales = ["hundred", "thousand", "million", "billion", "trillion"]
    words = ["hour", "hours", "minutes","minute","second", "seconds"]
    for i in command:
        if i not in units or i not in tens or i not in scales or i not in words :
            command.remove(i)
    timeString = ""
    for i in command:
        timeString += i
        timeString += " "

    hours = 0
    minutes = 0
    seconds = 0
    if "hour" in timeString :
        hours = timeString[:timeString.find("hour")]
        timeString = timeString[timeString.find("hour") + 4:]
    if "hours" in timeString:
        hours = timeString[:timeString.find("hours")]
        timeString = timeString[timeString.find("hours") + 5:]

    if "minutes" in timeString:
        minutes = timeString[:timeString.find("minutes")]
        timeString = timeString[timeString.find("minutes") + 7:]
    if "minute" in timeString:
        minutes = timeString[:timeString.find("minute")]
        timeString = timeString[timeString.find("minute") + 6:]

    if "seconds" in timeString:
        seconds = timeString[:timeString.find("seconds")]
        timeString = timeString[timeString.find("seconds") + 7:]
    if "second" in timeString:
        seconds = timeString[:timeString.find("second")]
        timeString = timeString[timeString.find("second") + 6:]

    finalTimeSeconds = 0
    finalTimeSeconds += w2n.word_to_num(hours) * 3600
    finalTimeSeconds += w2n.word_to_num(minutes) * 60
    finalTimeSeconds += w2n.word_to_num(seconds)

    for i in range (finalTimeSeconds):
        time.sleep(1)
    speak("times up ")


# def greeting():
#     # get name and remember - good morning smth

def easterEggs(command):
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
