import speech_recognition as sr
import pyttsx3
# import pywhatkit as kit
# import os
from func_for_file import *
# import openai
import webbrowser
from AppOpener import open 
import subprocess


# openai.api_key ="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"
# def answers_with_gpt(input_text):
#     try:
#         response = openai.completions.create(
#             engine = "text-davinci-002",
#             prompt = input_text,
#             max_tokens=100
#         )
#         return response.choices[0].text.strip()
#     except Exception as e:
#         print(e)



def youtube():
    pyttsx3.speak(f"which website you want me to open sir....")
    recognizer = sr.Recognizer()  # Define recognizer here
    
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        print("tell me the name of the website")
        audio = recognizer.listen(mic, timeout=5)
    
    try:
        video_to_play = recognizer.recognize_google(audio)
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["chatgpt","https://www.chatgpt.com"],["github","https://www.github.com"],
                 ["instagram","https://www.instagram.com"],[]]
        
        for site in sites:
            if site[0].lower() in video_to_play.lower():
                webbrowser.open(site[1])
                return f"Opening {site[0]}..."

    except sr.UnknownValueError:
        return "Speech Recognition could not understand the command."
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    
    return pyttsx3.speak(f"opening {video_to_play}")
    
def close_apps():
    pyttsx3.speak("closing the app")
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        audio_to_close = recognizer.listen(mic, timeout=3)

    try:
        audio_text = recognizer.recognize_google(audio_to_close).lower()+".exe"
        print("Recognized Text:", audio_text)  # Add this line for debugging

        app_to_close = ["whatsapp.exe", "telegram.exe", "chrome.exe", "ashpalt9.exe", "microsoftword.exe",
                        "microsoftexcel.exe", "microsoft powerpoint.exe", "calculator",
                        "hillclimbracing.exe", 'notepad', "vs code", "this pc"]

        if audio_text in app_to_close:
            result = subprocess.run(["taskkill", "/f", "/im", audio_text], capture_output=True, text=True)

            if result.returncode == 0:
                print(f"{audio_text.capitalize()} closed")
            else:
                print(f"Failed to close {audio_text.capitalize()}. Error: {result.stderr.strip()}")
        else:
            print(f"{audio_text.capitalize()} is not in the list of applications to close.")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def oepn_apps():
    pyttsx3.speak("Which app would you like me to open, sir...")
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        try:
            audio = recognizer.listen(mic, timeout=3)
            app_to_open = recognizer.recognize_google(audio).lower()
            
            apps = ["whatsapp", "telegram", "chrome", "ashpalt9", "microsoft word", "microsoft excel",
                    "microsoft powerpoint", "calculator", "hill climb racing", 'notepad', "vs code",
                    "this pc"]

            for app in apps:
                if app.lower() in app_to_open:
                    open(app)
                    print(f"Opening {app}...")
                    pyttsx3.speak(f"Opening {app}...")
                    return
            
            print(f"App '{app_to_open}' not recognized.")
            pyttsx3.speak(f"Sorry, I didn't understand which app you want to open.")

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")
            pyttsx3.speak("Sorry, I couldn't understand what you said.")
        
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            pyttsx3.speak("Sorry, there was an error with the speech recognition service.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            pyttsx3.speak("Sorry, an unexpected error occurred.")

        

def talk_back(input_text):
    if "hello" in input_text.lower():
        return greet()
    
    elif "how are you" in input_text.lower():
        return "I am good. How are you, sir?"
    
    elif "where are you from" in input_text:
        return "I am a training model"
    
    elif "goodbye" in input_text:
        return "Goodbye, have a nice day"
    
    elif "open a website" in input_text.lower():
        return youtube()
    
    elif "close the app" in input_text.lower():
        return close_apps()
    
    elif "open apps" in input_text.lower():
        return  oepn_apps()
    else:
        pass
        #return answers_with_gpt(input_text)

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            print("Say something:")
            recognizer.adjust_for_ambient_noise(mic)
            audio = recognizer.listen(mic, timeout=1)

        text = recognizer.recognize_google(audio)
        print("Listened line is:", text)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        continue

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    except Exception as e:
        print(f"Exception: {e}")

    try:
        response = talk_back(text)
        print('Response:', response)

        enjin = pyttsx3.init()
        enjin.setProperty("rate", 200)

        voice = enjin.getProperty("voices")
        enjin.setProperty("voices", voice[0].id)

        enjin.say(response)
        enjin.runAndWait() 

    except Exception as e:
        print(e)

