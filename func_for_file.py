from datetime import datetime

def greet():
    hour = datetime.now().hour

    if 6 <= hour < 12:
        return "Good morning, sir! , I am Jarvis. How may I assist you sir?"
    elif 12 <= hour < 16:
        return "Good afternoon, sir! ,I am Jarvis. How may I assist you sir?"
    elif 16 <= hour < 19:
        return "Good evening, sir!, I am Jarvis. How may I assist you sir?"
    else:
        pass


def file_operations():
    pass


#API key
#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