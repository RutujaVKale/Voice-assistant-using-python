import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia
import datetime
import os


listener = sr.Recognizer()
# print('hello')
engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    talk('I am your alex. How can i help you')
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            print('listen')
            command = listener.recognize_google(voice)
            print('converting')
            command = command.lower()
            if 'alex' in command:
                # talk(command)
                command = command.replace('alex', '')
                print(command)

    except:
        pass
    return command

def run_alex():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search about' in command:
        command = command.replace('search about', '')
        info = wikipedia.summary(command, sentences=1)
        talk(info)
        print(info)
    elif 'single' in command:
        talk('I am in relationship with obamas daughter ')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I, %M %p')
        print(time)
        talk('The current time is ' + time)
    elif 'open' in command:
        talk('Opening notepad')
        os.system("Notepad")
    elif 'What can you do' in command:
        talk('Hello I am Alex. I can provide you information about anything you ask me.I can play song on youtube for you.I can tell you about myself, if you are interested in knowing.I can open apps for you from your system. Thats it. Thats all I do. I am a lazy guy.')


run_alex()






