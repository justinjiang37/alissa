import pyaudio
import wave
import speech_recognition as sr  # voice recognition
import pyttsx3 as tts           # Text to Speech

engine = tts.init('sapi5')  # nsss for mac
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 135
engine.setProperty('rate', newVoiceRate)

# speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# recognizes mic input
def getAudio():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        print("1")

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Expection: " + str(e))
    return said
