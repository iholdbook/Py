# Importing required modules
# importing pyttsx3
# pip install pyttsx3, speechrecognition
# pip install pyaudio - если не установилась, ниже
# pip install pipwin
# pipwin install pyaudio
import pyttsx3
# importing speech_recognition
import speech_recognition as sr
# creating take_commands() function which
# can take some audio, Recognize and return
# if there are not any errors
def take_commands():
    # initializing speech_recognition
    r = sr.Recognizer()
    # opening physical microphone of computer
    with sr.Microphone() as source:
        print('Listening')
        Speak("Слушаю вас")
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
            print("Say that again sir")
            # returning none if there are errors
            return "None"
    # returning audio as text
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


# Driver Code
if __name__ == '__main__':
    # using while loop to communicate infinitely
    while True:
        command = take_commands()
        if "exit" in command:
            Speak("Сэр, так точно Сэр! До новых встреч, пока!")
            break
        if "insta" in command:
            Speak("Не знаю товоей инсты Сэр!")
        if "book" in command:
            Speak("Да Сэр, хорошие книги!")
        if "fun" in command:
            Speak("ХаХаХа, вот это шутка Сэр!")
        if "Cheburashka" in command:
            Speak("Привет, чебурашка, я Гена!")