#First lets start with installing some modules


import pyttsx3 #pip install pyttsx3  #python library which will help us to convert text to speech. In short, it is a text-to-speech library
import datetime # its inbuilt python module no need to install
import speech_recognition as sr #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser #inbuilt module
import os #inbuilt module
import smtplib #inbuilt module



'''
IF YOU ARE UNABLE TO INSTALL SPEECH RECOGNITION MODULE USING THE FOLLOWING COMMAND THEN DO FOLLOW THESE STEPS:-
pip install pipwin
pipwin install PyAudio

use a good microphone or it not gonna recognize 
for better recognition change the voice threshould

'''


 


engine = pyttsx3.init('sapi5')  #Speech API developed by Microsoft,which helps in recognition of voice
voices= engine.getProperty('voices') 
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)   




'''
Voice id helps us to select different voices.
voice[0].id = Male voice 
voice[1].id = Female voice

'''






def speak(audio):  #it can convert our text to speech.
       engine.say(audio) #will start speaking
       engine.runAndWait()  #u can change the threshold values from here just ctrl+right click. u can change the delay time of listening and recognition and voice command control and so on


def wishme():# LOL, this will only wish au according to your system time
    hour = int(datetime.datetime.now().hour) #importing hour in 24 hr format,but the AI can convert according to the system time
    if hour>=0 and hour<12:  #we have stored the integer value of the current hour or time into a variable named hour. Now, we will use this hour value inside an if-else loop.
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" Hi I am Spikey.  How may I help you") #perma

def takeCommand():  #Before defining the takeCommand() function, we need to install a module called speechRecognition
    #it takes microphone input from the user and returns string op
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    #just testing either it works or not
        print("Say that again please...")   #error occurs when there is any distortion in voice
        return "None" #it will return none if Cypher doesn't detects anything or if there is some error in it.
    return query

def sendEmail(to,content):#An instance method called sendmail is present in the SMTP module. This instance method allows us to send an email. 
    server = smtplib.SMTP('smtp.gmail,com',587)#SMTP is a protocol that allows us to send emails and to route emails between mail servers.
    server.ehlo()
    server.starttls()
    server.login('yourmailid', 'yourpassword')  #use your own id and password either it not gonna send any mail.
    server.sendmail('yourmailid', to, content)  #your mail id is needed, the person who will receive the content is written in try block check that out
    server.close()#dont forget to enable the less secure app in your mail security,either it not gonna sendEmail 
if __name__ == '__main__': #Whatever you will write inside this speak() function will be converted into speech
       # speak("satya is noice af")
      wishme()
      #while True:  #if  i use while true then this program will never exit and keep on going for infinite times 
      if 1:  #i used if(1): becoz at a time only 1 task will be done
        query = takeCommand().lower()#i took lower because the urls are mostly in that cases

    #LOGIC
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed similarly for others
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif '          play music' in query: #locate your directory in os 
            music_direc = "D:\\musics"
            musics=os.listdir(music_direc)
            print(musics)
            os.startfile(os.path.join(music_direc,musics[0]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open pycharm' in query:
            codePath ="G:\PyCharm Community Edition 2020.1.2\bin\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to satya' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "yourfriend's mail id"  #the person to whom you gonna send it.
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("i am sorry, i not able to send this email at this moment")

