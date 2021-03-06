# Importing required modules
# importing pyttsx3
# pip install pyttsx3, speechrecognition
# pip install pyaudio
# pip install pipwin
# pipwin install pyaudio
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# importing os module
import os

# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        # storing audio/sound to audio variable
        audio = r.listen(source)
        try:
            print("Recognizing")
            # Recognizing audio using google api
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Повторите снова Сэр...")
            # returning none if there are errors
            return "None"
    # returning audio as text
    import time
    time.sleep(2)
    return Query


# creating Speak() function to giving Speaking power
# to our voice assistant
def Speak(audio):
    # initializing pyttsx3 module
    engine = pyttsx3.init()
    # anything we pass inside engine.say(),
    # will be spoken by our voice assistant
    engine.say(audio)
    engine.runAndWait()

#Speak("Do you want to shutdown your computer sir?")
Speak("Сэр, желаеете выключить компьютер?")
while True:
    command = take_commands()
    if "no" in command:
        Speak("Спасибо Сэр, я не буду отключать компьютер.")
        break
    if "yes" in command:
        # Shutting down
        Speak("Выключаю компьютер.")
        os.system("shutdown /s /t 30")
        break
    Speak("Повторите снова Сэр.")