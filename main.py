from speech.listen import listen_for_wake_word, listen_command
from speech.speak import speak
from brain.logic import reply

while True:
    if listen_for_wake_word():
        speak("Yes?")
        command = listen_command()
        if command:
            response = reply(command)
            speak(response)
