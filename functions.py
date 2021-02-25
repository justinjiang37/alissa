import os
import time
import datetime
from datetime import datetime
import json
import requests
import pytz
import random
import re

from countryinfo import CountryInfo
import wikipedia
import subprocess

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
    if numSentences <= 5:
        return article
    else:
        sentences = article.split(". ")
        for i in range(3):
            final += sentences[i] + ". "
    return final

def getInfo(command):
    keywords = ""
    for i in command:
        keywords += i
        keywords + " "
    return summarize(getInfoHelper(keywords))

def getInfoHelper(keywords):
    return(wikipedia.summary(keywords))





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
