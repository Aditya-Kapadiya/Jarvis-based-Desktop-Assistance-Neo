import pyttsx3  # pip install pyttsx3 # pip install PyAudio # pip install pipwin # pip install wheel # install c++ 14.0
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui # pip install pyautogui
import pyjokes # pip install pyjokes
import json # pip install json
import requests # pip install requests

######################################################################################################################################################

######################################################################################################################################################

# Connecting a sapi5 voice

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


# Creating a User define function.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# For Wishing.

def wishMe():
    hour = int(datetime.datetime.now().hour) # For date and Time.
    if hour>=0 and hour<12:                  # Wish according to the time.
        speak("Good Morning Sir!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir!")   

    elif hour>=16 and hour<21:
        speak("Good Evening Sir!") 

    else:
        speak("Good Night Sir!")

    speak("I am your assistance neo. Please tell me how may I help you.")    # Welcome. 


#It takes microphone input from the user and returns string output

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        #audio = r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

# For sending email.

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587) # start connection to gmail.com
    server.ehlo()
    server.starttls()   # start tls service.
    server.login("adikapadiya@gmail.com", "Write_Your_Password_here") # credentials for login.
    server.sendmail("adikapadiya@gmail.com", to, content) # The From email.
    server.close() # Close the connection.

######################################################################################################################################################

######################################################################################################################################################

class jarvis():

    # For knowing current date.
    def date(self):
        YYYY=int(datetime.datetime.now().year) # For Year.
        MM=int(datetime.datetime.now().month) # For Month.
        DD=int(datetime.datetime.now().day) # For Day
        speak("current date is "+str(DD)+" "+str(MM)+" "+str(YYYY)) # Speak the date.

    # For knowing the time. 
    def time(self):
        TimeRightNow=datetime.datetime.now().strftime("%I:%M:%S")
        hour=0
        hour=datetime.datetime.now().hour
        if hour>=6 and hour<12:
            phase="morning"
        elif hour>=12 and hour<18:
            phase="afternoon"
        elif hour>=18 and hour<=24:
            phase="eveining"
        else:
            phase="night"
        speak("Its " + TimeRightNow+" of "+phase)

    # This function tells the joke.

    def jokes(self):
        speak(pyjokes.get_joke())

    # This function remember what is told to remember.

    def Knowing(self):
        remember=open('data.txt','r') # Open the file and read from it.
        speak("you said me to remember that"+remember.read())

    # code to remember and store the sentence that is spoken by the person.

    def Remember(self):
        speak("What should I remember?")
        Information=takeCommand()
        speak('you said me to remember that '+Information)
        rem = open('data.txt','w+b')  # open file and write in it.
        rem.write(Information) 
        rem.close()  # Close the file.
   
    # To take Screenshot.

    def screenshot(self):
        img = pyautogui.screenshot()
        speak("By what name should I save it?")
        ans=takeCommand()
        #Replace FolderPath with the path of folder where you want to save your screenshots in your computer 
        ans="C:\\Users\\kapad\\Pictures\\Jarvis"+ans+".png" # Stores the image at the given folder path.
        img.save(ans) # Saves the image.
        speak("Screenshot taken")

    def corona(self):
        r = requests.get('https://api.covid19api.com/country/india/status/confirmed/live').text
        parser = json.loads(r)
        l = parser[::-1]
        today = (l[0])
        print(f"There are {today['Cases']} confirmed corona cases in India.")
        speak(f"There are {today['Cases']} confirmed corona cases in India.")
    
    def reboot(self):
        speak("Ok Sir, rebooting system")
        codePath = "C:\\neo\\restart.cmd"
        os.startfile(codePath)

    def power_off(self):
        speak("Good Bye sir, system shutdown started")
        codePath = "C:\\neo\\shutdown.cmd"
        os.startfile(codePath)
    
    def logout(self):
        speak("Ok Sir, User logged out")
        codePath = "C:\\neo\\logout.cmd"
        os.startfile(codePath)

    def stop(self):
        speak("Ok Sir, Aborting Process done")
        codePath = "C:\\neo\\abort.cmd"
        os.startfile(codePath)

    def recycle_bin(self):
        speak("Ok Sir, recycle bin cleared")
        codePath = "C:\\neo\\emptybin.cmd"
        os.startfile(codePath)

    def visual_code(self):
        speak("Ok, sir Visual code up and running")
        codePath = "C:\\Users\\kapad\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    def task_manager(self):
        speak("Ok Sir, task manager is up and running")
        codePath = "C:\\WINDOWS\\system32\\Taskmgr.exe"
        os.startfile(codePath)

    def performance(self):
        speak("Ok Sir, performance monitor is up and running")
        codePath = "C:\\WINDOWS\\system32\\perfmon.msc"
        os.startfile(codePath)

    def resource(self):
        speak("Ok Sir, resource monitor is up and running")
        codePath = "C:\\WINDOWS\\system32\\resmon.exe"
        os.startfile(codePath)

    def scheduler(self):
        speak("Ok Sir, task scheduler is up and running")
        codePath = "C:\\WINDOWS\\system32\\taskschd.msc"
        os.startfile(codePath)

    def firewall(self):
        speak("Ok Sir, windows firewall setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\WF.msc"
        os.startfile(codePath)

    def fax(self):
        speak("Ok Sir, windows fax and scan is up and running")
        codePath = "C:\\WINDOWS\\system32\\WFS.msc"
        os.startfile(codePath)

    def OS(self):
        speak("Ok Sir, Windows information is as shown")
        codePath = "C:\\WINDOWS\\system32\\winver.exe"
        os.startfile(codePath)

    def disk_management(self):
        speak("Ok Sir, disk management setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\diskmgmt.msc"
        os.startfile(codePath)

    def disk_cleanup(self):
        speak("Ok Sir, disk cleanup setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\cleanmgr.exe"
        os.startfile(codePath)

    def optimise(self):
        speak("Ok Sir, drive optimization setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\dfrgui.exe"
        os.startfile(codePath)

    def device_manager(self):
        speak("Ok Sir, device manager setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\devmgmt.msc"
        os.startfile(codePath)

    def control_panel(self):
        speak("Ok Sir, control panel is up and running")
        codePath = "C:\\WINDOWS\\system32\\control.exe"
        os.startfile(codePath)

    def default_app(self):
        speak("Ok Sir, default apps setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\ComputerDefaults.exe"
        os.startfile(codePath)

    def command_prompt(self):
        speak("Ok Sir, command prompt is up and running")
        codePath = "C:\\WINDOWS\\system32\\cmd.exe"
        os.startfile(codePath)

    def snipping(self):
        speak("Ok Sir, snipping tool is up and running")
        codePath = "C:\\WINDOWS\\system32\\SnippingTool.exe"
        os.startfile(codePath)
        
    def colour_calibration(self):
        speak("Ok Sir, color calibration setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\dccw.exe"
        os.startfile(codePath)

    def volume(self):
        speak("Ok Sir, volume setting is up and running")
        codePath = "C:\\WINDOWS\\system32\\SndVol.exe"
        os.startfile(codePath)

    def calculator(self):
        speak("Ok Sir, calculator is up and running")
        codePath = "C:\\WINDOWS\\system32\\calc.exe"
        os.startfile(codePath)

    def teams(self):
        speak("Ok Sir, Microsoft Teams is up and running")
        codePath = "C:\\neo\\teams.cmd"
        os.startfile(codePath)

    def code_block(self):
        speak("Ok Sir, Codeblocks is up and running")
        codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
        os.startfile(codePath)

    def chrome(self):
        speak("Ok Sir, Chrome Browser is up and running")
        codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(codePath)

    def seven_zip(self):
        speak("Ok Sir, 7 zip is up and running")
        codePath = "C:\\Program Files\\7-Zip\\7zFM.exe"
        os.startfile(codePath)

    def photoshop(self):
        speak("Ok Sir, Adobe photoshop is up and running")
        codePath = "C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe"
        os.startfile(codePath)

    def backup(self):
        speak("Ok Sir, Google backup and sync is up and running")
        codePath = "C:\\Program Files\\Google\\Drive\\googledrivesync.exe"
        os.startfile(codePath)

    def google_doc(self):
        speak("Ok Sir, Google Docs is up and running")
        codePath = "C:\\Program Files\\Google\\Drive\\googledrivesync.exe"
        os.startfile(codePath)

    def google_sheet(self):
        speak("Ok Sir, Google sheet is up and running")
        codePath = "C:\\Users\\kapad\\Desktop\\sheet.cmd"
        os.startfile(codePath)

    def google_slide(self):
        speak("Ok Sir, Google slide is up and running")
        codePath = "C:\\Users\\kapad\\Desktop\\slide.cmd"
        os.startfile(codePath)

    def bluestack(self):
        speak("Ok Sir, bluestack emulator is up and running")
        codePath = "C:\\Program Files\\BlueStacks\\Bluestacks.exe"
        os.startfile(codePath)

    def brave(self):
        speak("Ok Sir, brave browser is up and running")
        codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(codePath)

    
    def google_drive(self):
        speak("Ok Sir, google drive is up and running")
        codePath = "C:\\neo\\drive.cmd"
        os.startfile(codePath)
    
    def tracer(self):
        speak("Ok Sir, Cisco packet tracer is up and running")
        codePath = "C:\\Program Files\\Cisco Packet Tracer 8.0\\bin\\PacketTracer7.exe"
        os.startfile(codePath)
    
    def discord(self):
        speak("Ok Sir, discord is up and running")
        codePath = "C:\\neo\\discord.cmd"
        os.startfile(codePath)
    
    def stream(self):
        speak("Ok Sir, Google Drive file stream is up and running")
        codePath = "C:\\Program Files\\Google\\Drive File Stream\\44.0.14.0\\GoogleDriveFS.exe"
        os.startfile(codePath)
    
    def charm(self):
        speak("Ok Sir, pycharm is up and running")
        codePath = "C:\\Users\\kapad\\AppData\\Local\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
        os.startfile(codePath)
    
    def memory(self):
        speak("Ok Sir, mem reduct is up and running")
        codePath = "C:\\Program Files\\Mem Reduct\\memreduct.exe"
        os.startfile(codePath)
    
    def nord(self):
        speak("Ok Sir, nord vpn is up and running")
        codePath = "C:\\Program Files\\NordVPN\\NordVPN.exe"
        os.startfile(codePath)
    
    def partition(self):
        speak("Ok Sir, partition wizard is up and running")
        codePath = "C:\\Program Files\\MiniTool Partition Wizard 12\\partitionwizard.exe"
        os.startfile(codePath)
    
    def screen_recorder(self):
        speak("Ok Sir, OBS studio is up and running")
        codePath = "C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
        os.startfile(codePath)
    
    def virtualbox(self):
        speak("Ok Sir, virtual box is up and running")
        codePath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
        os.startfile(codePath)
    
    def file_explorer(self):
        speak("Ok Sir, file explorer is up and running")
        codePath = "C:\\Windows\\explorer.exe"
        os.startfile(codePath)
    
    def notepad(self):
        speak("Ok Sir, notepad is up and running")
        codePath = "C:\\Windows\\notepad.exe"
        os.startfile(codePath)
    
    def registry(self):
        speak("Ok Sir, regedit is up and running")
        codePath = "C:\\Windows\\regedit.exe"
        os.startfile(codePath)
    
    def python(self):
        speak("Ok Sir, python IDLE is up and running")
        codePath = "C:\\Users\\kapad\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
        os.startfile(codePath)
    
    def signal(self):
        speak("Ok Sir, signal is up and running")
        codePath = "C:\\Users\\kapad\\AppData\\Local\\Programs\\signal-desktop\\Signal.exe"
        os.startfile(codePath)
    
    def specification_software(self):
        speak("Ok Sir, Speccy is up and running")
        codePath = "C:\\Program Files\\Speccy\\Speccy64.exe"
        os.startfile(codePath)
    
    def tor(self):
        speak("Ok Sir, TOR browser is up and running")
        codePath = "C:\\Users\\kapad\\Desktop\\Tor Browser\\Browser\\firefox.exe"
        os.startfile(codePath)
    
    def steam(self):
        speak("Ok Sir, Steam is up and running")
        codePath = "C:\\Program Files (x86)\\Steam\\steam.exe"
        os.startfile(codePath)
    
    def telegram(self):
        speak("Ok Sir, Telegram is up and running")
        codePath = "C:\\Users\\kapad\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
        os.startfile(codePath)
    
    def paint(self):
        speak("Ok Sir, Paint is up and running")
        codePath = "C:\\WINDOWS\\system32\\mspaint.exe"
        os.startfile(codePath)
    
    def system_config(self):
        speak("Ok Sir, system configuration is up and running")
        codePath = "C:\\WINDOWS\\system32\\msconfig.exe"
        os.startfile(codePath)
    
    def system_info(self):
        speak("Ok Sir, system information is up and running")
        codePath = "C:\\WINDOWS\\system32\\msinfo32.exe"
        os.startfile(codePath)
    
    def camera(self):
        speak("Ok Sir, camera is up and running")
        codePath = "C:\\neo\\camera.cmd"
        os.startfile(codePath)
    
    def connect(self):
        speak("Ok Sir, wifi connected")
        codePath = "C:\\neo\\wificonn.cmd"
        os.startfile(codePath)
    
    def wifi_down(self):
        speak("Ok Sir, wifi is down")
        codePath = "C:\\neo\\wifidisc.cmd"
        os.startfile(codePath)

    def wikipedia(self):
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    def music(self):
        speak("Ok sir, playing music")
        music_dir = 'C:\\Users\\kapad\\Music\\'
        songs = os.listdir(music_dir)
        print(songs)    
        os.startfile(os.path.join(music_dir, songs[0]))
    def help():
        speak("I have modules like")
        speak("pyttsx3")
        speak("pyaudio for audio input and output")
        speak("speech recognition for recognizing voice and language")
        speak("date time module for knowing date and time")
        speak("wikipedia module for searching content from wikipedia")
        speak("webbrowser module to interact with browser")
        speak("os for ")
        speak("smtplib module for performing task related to email sending")
        speak("pyautogui for ")
        speak("pyjokes for jokes")
        speak("json for ")
        speak("requests for ")

a=jarvis()

#####################################################################################################################################################

#####################################################################################################################################################


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() # stores the voice in query and match it with the keywords defined below.

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            a.wikipedia()

        elif 'youtube' in query:
            speak("Ok, sir loading youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Ok, sir loading google")
            webbrowser.get('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s').open_new('https://google.com')

        elif 'stackoverflow' in query:
            speak("Ok, sir loading stackoverflow")
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            a.music()

        elif 'the date' in query:
            a.date()

        elif 'the time' in query:
            a.time()

        elif 'help' in query:
            a.help()

        elif 'screenshot' in query:
            a.screenshot()

        elif 'joke' in query:
            a.jokes()

        elif 'knowing' in query:
            a.Knowing()
             
        elif 'remember' in query:
            a.remember()

        elif 'corona' in query:
            a.corona()

        elif 'open visual code' in query:
            a.visual_code()

        elif 'reboot system' in query:
            a.reboot()

        elif 'power off' in query:
            a.power_off()

        elif 'stop' in query:
            a.stop()

        elif 'log out' in query:
            a.logout()

        elif 'empty recycle' in query:
            a.recycle_bin()

        elif 'task manager' in query:
            a.task_manager()

        elif 'performance monitor' in query:
            a.performance()

        elif 'monitor' in query:
            a.resource()

        elif 'scheduler' in query:
            a.scheduler()
            

        elif 'firewall' in query:
            a.firewall()
            

        elif 'fax and scan' in query:
            a.fax()
            

        elif 'this operating system' in query:
            a.os()
            

        elif 'disk management' in query:
            a.disk_management()
            

        elif 'disk cleanup' in query:
            a.disk_cleanup()
            

        elif 'optimise' in query:
            a.optimise()
            

        elif 'device manager' in query:
            a.device_manager()
            

        elif 'control panel' in query:
            a.control_panel()
            

        elif 'default app' in query:
            a.default_app()
            

        elif 'command prompt' in query:
            a.command_prompt()
            

        elif 'snipping' in query:
            a.snipping()

        elif 'colour calibration' in query:
            a.colour_calibration()
            

        elif 'volume' in query:
            a.volume()
            

        elif 'calculator' in query:
            a.calculator()
            

        elif 'open team' in query:
            a.teams()
            

        elif 'code block' in query:
            a.code_block()
            
         
        elif 'chrome' in query:
            a.chrome()
            

        elif '7 zip' in query:
            a.seven_zip()
            

        elif 'photoshop' in query:
            a.photoshop()
            

        elif 'start backup' in query:
            a.backup()
            

        elif 'google document' in query:
            a.google_doc()
            

        elif 'google sheet' in query:
            a.google_sheet()
             

        elif 'google slide' in query:
            a.google_slide()
               

        elif 'blue' in query:
            a.bluestack()
            

        elif 'brave' in query:
            a.brave()
            

        elif 'google drive' in query:
            a.google_drive()
            

        elif 'tracer' in query:
            a.tracer()
            

        elif 'discord' in query:
            a.discord()
            

        elif 'stream' in query:
            a.stream()
            

        elif 'charm' in query:
            a.charm()
            

        elif 'memory' in query:
            a.memory()
            

        elif 'nord' in query:
            a.nord()
                

        elif 'partition' in query:
            a.partition()
              

        elif 'screen recorder' in query:
            a.screen_recorder()
            

        elif 'virtualbox' in query:
            a.virtualbox()
                  

        elif 'file explorer' in query:
            a.file_explorer()
            

        elif 'notepad' in query:
            a.notepad()
            

        elif 'registry editor' in query:
            a.registry()
            

        elif 'python' in query:
            a.python()
            

        elif 'signal' in query:
            a.signal()
            

        elif 'specification software' in query:
            a.specification_software()
            

        elif 'tor browser' in query:
            a.tor()
            

        elif 'steam' in query:
            a.steam()
            

        elif 'telegram' in query:
            a.telegram()
        

        elif 'paint' in query:
            a.paint()
            

        elif 'system configuration' in query:
            a.system_config()
            

        elif 'system information' in query:
            a.system_info()
            

        elif 'camera' in query:
            a.camera()
             

        elif 'connect' in query:
            a.connect()
            

        elif 'network down' in query:
            a.wifi_down()
            
        elif 'help' in query:
            a.help()

        elif 'my name' in query:
            speak("Sir, Your name is Aditya")

        elif 'my friend name' in query:
            speak("Your friend name is ")

        elif 'your name' in query:
            speak("My name is Neo, Sir")
            
        elif 'are you' in query:
            speak("I'm fine Sir")

        elif 'my birthday' in query:
            speak("Sir, Your birthday is on 5 10 2001")

        elif 'your birthday' in query:
            speak("I don't have birthday, Sir")

        elif "why you don't" in query:
            speak("Because i'm a machine, Sir")

        elif 'for your response' in query:
            speak("My pleasure Sir")

        elif 'your friend' in query:
            speak("You are the only friend of mine")

        elif 'your developer' in query:
            speak("My developers are Chintan, Harsil and You, Sir")

        elif 'developed' in query:
            speak("My developer's created me.")
        
        elif 'good morning' in query:
            speak("Good morning, Sir it's a bright day outside.")

        elif 'good afternoon' in query:
            speak("Good afternoon, Sir")

        elif 'good evening' in query:
            speak("Good evening, Sir")    

        elif 'good night' in query:
            speak("Good night, Sir. It's time to take some rest. See you tomorrow")

        elif 'good' in query:
            speak("Thank you Sir")
        
        elif 'exit' in query:
            speak("Exited sir")
            exit()

        elif 'email to aditya' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "adikapadiya@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'email to chintan' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mandaliyachintan12@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harshilsuthar710@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'do' in query:
            speak("Give input for two digit calculation")

            speak("What is the first digit")
            a=takeCommand()
            speak("What is the second digit")
            b=takeCommand()

            speak("What operation you want to perform")
            z=takeCommand()
            if z=='addition':
                c=int(a) + int(b)
                speak("Your Answer is")
                print("Your answer is: ",c)
                speak(c)
            elif z=='multiply':
                c=int(a) * int(b)
                speak("Your Answer is")
                print("Your answer is: ",c)
                speak(c)
            elif z=='substraction':
                c=int(a) - int(b)
                speak("Your Answer is")
                print("Your answer is: ",c)
                speak(c)
            elif z=='division':
                c=int(a) / int(b)
                speak("Your Answer is")
                print("Your answer is: ",c)
                speak(c)
            else:
                speak("Provide valid operation")
