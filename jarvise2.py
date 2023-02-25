import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import pyautogui
import time
import os
import cv2



def speak_joke():
    # Get a random joke from the pyjokes library
    joke = pyjokes.get_joke()

    engine.setProperty('rate', 150)
    
    # Speak the joke
    engine.say(joke)
    engine.runAndWait()


""" time code """
def speak_time():
    # Get current time
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")

    # Speak out current time using pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
    engine.say(f"The current time is {current_time}")
    engine.runAndWait()

""" date code"""
def date_today():
    today=datetime.date.today()
    todaydate = today.strftime("%B %d %Y")
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(f"Today is {todaydate}")
    engine.runAndWait()

"""chat gpt """
def chat():
    url="https://chat.openai.com/chat" 
    os.system("start brave" + url)

# Initialize speech recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Listen for the word "Jarvis" 
with sr.Microphone() as source:
    print("Say 'Jarvis' to activate.")
    while True:
        audio = r.listen(source,5,3)
        try:
            if "jarvis" in r.recognize_google(audio).lower():
                engine.say("varun!   How can I help you?")
                engine.runAndWait()
                break
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

# Take user input and perform a task based on the input
while True:
    with sr.Microphone() as source:
        print("Speak now.")    
        audio = r.listen(source,5,3)
        try:
            # Convert speech to text
            text = r.recognize_google(audio)
            print("You said: " + text)

            # Perform a task based on user input
            if "say"in text.lower():
                engine.say(text[4:])
                engine.runAndWait()
               
            elif "hello" in text.lower():
                engine.say("Hello varun! How are you?")
                engine.runAndWait()
                
            elif "goodbye" in text.lower():
                engine.say("Goodbye!")
                engine.runAndWait()
                break
            elif "date and time" in text.lower():
                speak_time()
                date_today()
                
            elif "chatgpt" in   text.lower(): 
                chat()

            elif "camera" in text.lower():
                cap = cv2.VideoCapture(0) 
                if not cap.isOpened():
                    print("Error opening video stream or file")
                while cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        cv2.imshow('Frame', frame)
                        if cv2.waitKey(25) & 0xFF == ord('q'):
                            break
                    else:
                        break
                cap.release(TimeoutError=3)
                cv2.destroyAllWindows()




                
            elif "open"in text.lower():
                pyautogui.typewrite(['command', 'space'], 0.2)
                pyautogui.press("win")
                pyautogui.typewrite(text[5:], 0.2) 
                pyautogui.typewrite(['enter'], 0.2)
                
            elif "show pictures of" in text.lower():
                pyautogui.typewrite(['command', 'space'], 0.2)
                pyautogui.press("win")
                os.system("start brave " + "https://www.google.com/search?q="+text[17:]+"&tbm=isch")
                pyautogui.typewrite(['enter'], 0.2)
                
            elif "play the song " in text.lower():
                pyautogui.typewrite(['command', 'space'], 0.2)
                pyautogui.press("win")
                os.system("start brave " + "https://www.youtube.com/results?search_query="+text[20:])
                pyautogui.typewrite(['enter'], 0.2) 
                
            elif "show videos of" in text.lower():
                pyautogui.typewrite(['command', 'space'], 0.2)
                pyautogui.press("win")
                os.system("start brave " + "https://www.youtube.com/results?search_query="+text[16:])
                pyautogui.typewrite(['enter'], 0.2)
                
            
                
            elif "joke" in text.lower():
                speak_joke()
                
            elif "time" in text.lower():
                speak_time()
                
            elif "date" in text.lower():
                date_today()
                
            else:
                engine.say("I'm sorry, I don't understand.")
                engine.runAndWait()
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
