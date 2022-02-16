# Importing required modules
# importing pyttsx3
# pip install pyttsx3, speechrecognition
# pip install pyaudio
# pip install pipwin
# pipwin install pyaudio
import pyttsx3
import speech_recognition as sr
def take_commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        Speak("Слушаю вас")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio)
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
    return Query
    
def Speak(audio):
    engine = pyttsx3.init()
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