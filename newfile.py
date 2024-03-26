import pyttsx3
import speech_recognition as sr
from AppOpener import open
import subprocess
# def open_apps():
#     pyttsx3.speak("Which app would you like me to open, sir...")
    
#     recognizer = sr.Recognizer()
    
#     with sr.Microphone() as mic:
#         recognizer.adjust_for_ambient_noise(mic)
#         try:
#             audio = recognizer.listen(mic, timeout=3)
#             app_to_open = recognizer.recognize_google(audio).lower()
            
#             apps = ["whatsapp", "telegram", "chrome", "ashpalt9", "microsoft word", "microsoft excel",
#                     "microsoft powerpoint", "calculator", "hill climb racing", 'notepad', "vs code",
#                     "this pc"]

#             for app in apps:
#                 if app.lower() in app_to_open:
#                     open(app)
#                     print(f"Opening {app}...")
#                     pyttsx3.speak(f"Opening {app}...")
#                     return
            
#             print(f"App '{app_to_open}' not recognized.")
#             pyttsx3.speak(f"Sorry, I didn't understand which app you want to open.")

#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand audio")
#             pyttsx3.speak("Sorry, I couldn't understand what you said.")
        
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")
#             pyttsx3.speak("Sorry, there was an error with the speech recognition service.")

#         except Exception as e:
#             print(f"An unexpected error occurred: {e}")
#             pyttsx3.speak("Sorry, an unexpected error occurred.")

# # Call the function to test
# open_apps()


def close_apps():
    pyttsx3.speak("closing the app")
    
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic)
        audio_to_close = recognizer.listen(mic, timeout=1.5)

    try:
        audio_text = recognizer.recognize_google(audio_to_close).lower()+".exe"
        print("Recognized Text:", audio_text)  # Add this line for debugging

        app_to_close = ["whatsapp.exe", "telegram.exe", "chrome.exe", "ashpalt9.exe", "microsoftword.exe",
                        "microsoftexcel.exe", "microsoftpowerpoint.exe", "calculator",
                        "hillclimbracing.exe", 'notepad.exe', "vs code", "this pc"]

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



close_apps()