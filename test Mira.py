from pickle import TRUE
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess as sp
import requests
import wolframalpha

engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


paths ={"calculator":"C:\\Windows\\System32\\calc.exe",
        "notepad":"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories"}

contacts ={"dad":9948152365,"mom":7416786220,"mirzu":7330834565,'adil':8019786102,'arshi':6303286665,'jakeer':9391768669}



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def open_calculator():
    sp.Popen(paths["calculator"])
    
def open_notepad():
    sp.Popen(paths["notepad"])
    
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Boss!")
    elif hour>=12 and hour<18:
        speak("Good afternoon Boss!")
    else:
        speak("Good evening Boss!")
        
def open_cmd():
    os.system("start cmd")
    
    
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        
    
    except Exception as e:
        speak('Sorry, I could not understand. Could you please say that again?')
        print('say something...')
        query = 'None'
    return query
    


if __name__ == "__main__":
    wishMe()
    speak("I am Mira your personal assistant")
    loop=True
    while loop==True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak ('searching Wikipedia')
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H hours %M minutes %S seconds")
            speak(f"The time is{strTime}\n")
            print(strTime)
        
        elif 'who am i' in query:
            speak("your name is Adil Samdani Shaik and you are my boss")
        
        elif 'who are you' in query:
            speak("I am Mira your personal A I ,and i am at your service ")

        elif "when is my birthday" in query:
            speak("march thirty, two thousand two")

        elif "my mum" in query:
            speak("Nafeesa Shaik")

        elif "brother" in query:
            speak("mirza ali shaik")

        elif "my dad" in query:
            speak("Sadik Shaik")

        elif ' best friend' in query:
            speak("Ramu garu")

        elif 'mama' in query:
            speak("maa ma  mooddha petara")

        elif "my friends" in query:
            speak("Gopi,Afrose and Lohit")

        elif "my room mates" in query:
            speak("Ganesh,Revanth,Murali,Chinmai,Rohit surya")
            print("Ganesh,Revanth,Murali,Chinmai,Rohit Surya")

        elif 'my phone number' in query:
            print("9948922769")
            speak("9948922769")

        elif "open spotify" in query:
            webbrowser.open("https://open.spotify.com/playlist/7g2IG6t7rERO1f5Exfr7WI?si=qQRHjOzmTECR9sXbC8JCfQ")
        
        elif 'friends song' in query:
            chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
            webbrowser.get(chrome).open("https://www.youtube.com/watch?v=oqBH-NsHIJU")
        
        elif "believer" in query:
            webbrowser.open("https://www.youtube.com/watch?v=7wtfhZwyrcc")


        elif "play songs" in query:
            webbrowser.open("https://open.spotify.com/album/1c7rXbKxSkeuHSKk0U74P7")


        elif "you and me" in query:
            webbrowser.open("https://www.youtube.com/watch?v=GpIwZiXK_rk&list=PLDisKgcnAC4RWvCaHFDu6QhO8o4pu-6D6&index=2")


        elif "it's hard" in query:
            webbrowser.open("https://www.youtube.com/watch?v=mJq8xXAfczo&list=PLDisKgcnAC4RWvCaHFDu6QhO8o4pu-6D6&index=10")
        elif "give me drugs" in query:
            webbrowser.open("https://www.youtube.com/watch?v=DeltGLnu2U8")
        elif "Jai balayya" in query:
            webbrowser.open("https://www.youtube.com/watch?v=zWZUiCe8T-k&t=95s")
        elif "who is my girlfriend" in query:
            speak("hmmm.. am I not enough for you!!")
        elif "bye" in query:
            speak("bye sir !! have a nice day")
            loop = False
        elif "shut down" in query:
            speak("hope we meet soon")
            loop = False
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        
        elif "jai balayya" in query:
            speak("jai jai balayya")
        
        elif "chandramukhi" in query:
            speak("lakha lakha lakha laka laka")
        
        elif "open camera" in query:
            speak("opening camera")
            open_camera()
            
            
        elif "open calculator" in query:
            speak("opening calculator")
            open_calculator()
            
        elif "open command prompt" in query:
            open_cmd()
            
        elif "open notepad" in query:
            open_notepad()
            
        elif "joke" in query:
            speak(f"i hope you like this one")
            joke=get_random_joke()
            print(joke)
            speak(joke)
        elif 'what is' in query:
            app_id = "EA85GP-8Y57JRGKVU"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(query+':'+answer)
            
             
        