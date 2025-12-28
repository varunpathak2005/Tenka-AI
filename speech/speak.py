import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("🤍 Tenka:", text)
    engine.say(text)
    engine.runAndWait()
