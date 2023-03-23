# SCM-Project.
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"\nUSER : {data}")
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understanding...")
            print("Speak again...")
            return sptext()

def speechtx(x):
    print(f"JATIN : {x}\n")
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(x)
    engine.runAndWait()

if "name" == "main":
    os.system("cls")
    speechtx("Say 'hello Jatin' to activate the software")
    if sptext() == "hello jatin":
        speechtx("Hello sir, Namaste")
        while True:
            time.sleep(2)
            data1 = sptext()
            if "your name" in data1:
                speechtx("My name is Jatin")
            elif "time" in data1:
                speechtx(datetime.datetime.now().strftime("%I%M%p"))
            elif "open google" in data1:
                webbrowser.open("https://www.google.com/")
            elif "joke" in data1:
                speechtx(pyjokes.get_joke(language="en", category="all"))
            # elif "play song" in data1:
            #     address = "D:\\Songs"
            #     listsong = os.listdir(address)
            #     print(listsong)
            #     os.startfile(os.path.join(address, listsong[0]))
            elif "repeat" in data1:
                speechtx(sptext())
            elif "exit" in data1:
                speechtx("Thank You")
                break
            else:
                speechtx("Sorry, I didn't get that.")
                speechtx("Please try anything else.")
    else:
        speechtx("bye")
