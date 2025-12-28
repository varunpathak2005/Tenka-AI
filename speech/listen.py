import speech_recognition as sr

WAKE_WORD = "hello"

def listen_for_wake_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🟣 Waiting for wake word...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print("👂 Heard:", text)
        return WAKE_WORD in text
    except:
        return False


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening for command...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return ""
