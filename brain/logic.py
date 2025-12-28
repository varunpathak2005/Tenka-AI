def reply(text):
    text = text.lower()

    if "time" in text:
        return "I don't wear a watch yet, but I'm always here."
    elif "who are you" in text:
        return "I am Tenka. Built by you."
    else:
        return "I heard you."
