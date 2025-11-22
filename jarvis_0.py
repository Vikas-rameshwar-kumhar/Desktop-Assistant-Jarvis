print("Just wait for 3 seconds")
from Body.listen import MicExecution
import datetime 
import webbrowser
import pywhatkit
from time import sleep 
import os
import keyboard
import pyautogui
from Body.speak import speak 
import sys
import psutil
import random

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 12:
    speak("good morning sir")
elif hour >= 12 and hour < 18:
    speak("good Afternoon sir")
else:
    speak("good evening sir")


print("To start the Jarvis")
print("Say - hello jarvis or wake up jarvis")
# speak("To start the Jarvis")
# speak("Say - hello jarvis")


def MainExecution():
    
    while True:
        Data = MicExecution()
        Data = str(Data)

        if len(Data)<3:
            pass

        elif "morning" in Data: #example 
            msg = ["morning sir ", "thanks sir same to you", "good morning"]
            speak(random.choice(msg))

        elif "time" in Data or "timing" in Data:
            time = datetime.datetime.now().strftime("%I %M %p")
            # print("current time is " + time)
            speak("current time is " + time)

        elif "date" in Data :
            date = datetime.datetime.now().day
            day = datetime.datetime.now().strftime("%A")   
            month = datetime.datetime.now().strftime("%B")   
            year = datetime.datetime.now().year
            speak(f"Its {day}.  {date}. {month}. {year}")

        elif "how are you" in Data or "do you feel better" in Data or "how do you feel" in Data or "how r u" in Data: 
            msg = ["i'm good , thank you for asking. I hope you're doing well too.", "I'm fine sir", "I'm good sir, I hope you're doing well too." ]
            speak(random.choice(msg))

        elif "i am fine" in Data:
            msg = ["I'm glad to hear it!"]
            speak(random.choice(msg))


        elif "screenshot" in Data or "take ss" in Data:
            ss = pyautogui.screenshot()
            now = datetime.datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"D:\\screenshot\\ss_{timestamp}.png"
            ss.save(filename)
            speak("screenshot took sir")
            # print(f"Screenshot saved as {filename}")

    
        elif "close" in Data and "notification" in Data:
            speak("ok,sir")
            pyautogui.hotkey('win', 'n')

        elif "notification" in Data:
            speak("on your left side sir")
            pyautogui.hotkey('win', 'n')
        
        #chrome auto
        elif "close this tab" in Data or "close the tab" in Data:
            speak("ok sir")
            pyautogui.hotkey('ctrl', 'f4')

        elif "new tab" in Data:
            speak("ok sir")
            pyautogui.hotkey('ctrl', 't')

        elif "previous tab" in Data:
            speak("ok sir")
            pyautogui.hotkey('ctrl','shift','t')

        elif "reload" in Data:
            speak("ok sir")
            pyautogui.hotkey('ctrl', 'f5')

        elif "tab " in Data:
            if "1" in Data or "one" in Data:
                speak("ok sir")
                pyautogui.hotkey('ctrl', '1')
        
            elif "2" in Data or "to" in Data or "two" in Data:
                speak("ok sir")
                pyautogui.hotkey('ctrl', '2')

            elif "3" in Data:
                speak("ok sir")
                pyautogui.hotkey('ctrl', '3')

            elif "4" in Data:
                speak("ok sir")
                pyautogui.hotkey('ctrl', '4')

        #youtube auto
        elif "play" in Data and "video" in Data:
            speak("ok sir")
            pyautogui.hotkey('k')

        elif ("pause" in Data and "video" in Data) or ("stop" in Data and "video" in Data):
            speak("ok sir")
            pyautogui.hotkey('k')

        elif "full screen" in Data:
            speak("ok sir")
            pyautogui.hotkey('f')


        elif "close it" in Data or "close this window" in Data:
            speak("ok sir")
            pyautogui.hotkey('alt', 'f4')

        elif "minimise" in Data and "window" in Data:
            speak("ok sir")
            with pyautogui.hold('win'):
                pyautogui.press(['down'])
                pyautogui.press(['down'])


        elif "exit" in Data: #
            speak("ok, see you later sir ")
            sys.exit()
          
        elif "you" in Data and "take" in Data and "rest" in Data: #sleep 
            # speak("ok sir, you can call me anytime")
            msg = ["I love to do this job", "thanks sir, you can call me anytime ", "finally i can take rest now", "thank you for being so considerate. if you need any help, just call." ]
            speak(random.choice(msg))
            # playsound("D:\\JARVIS\\jarvis by kaushik\\sound\\breathing2.mp3")
            break

        elif "sleep" in Data: #sleep     
            msg = ["I love to do this job", "thanks sir, you can call me anytime ", "finally i can sleep", "thank you for being so considerate. if you need any help, just call." ]
            speak(random.choice(msg))
            # playsound("D:\\JARVIS\\jarvis by kaushik\\sound\\breathing2.mp3")
            break 

        elif "good bye" in Data or "goodbye" in Data: #exit terminal
            speak("Goodbye sir, I love to see you again.")
            sys.exit()


        elif percent < 15 and not plugged:
            speak("sir, the battery level is less than 15 percent.")
            speak("I need power to live. otherwise i will die . ")
            speak("so, please charge me")

        elif "None" in Data:
            speak("")


        elif "open" in Data:
            openApp = Data.replace("open ","")
            
            if "file" in Data:
                speak("opening file manager")
                os.startfile("explorer.exe")

            elif 'google' in Data or "chrome" in Data:
                speak("Opening chrome browser")
                os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

            elif 'youtube' in Data:
                print("    Opening YouTube")
                speak("opening Youtube")
                webbrowser.open("youtube.com")
            

            else:
                pyautogui.press('win')    #pressing window key
                sleep(0.5)
                keyboard.write(openApp)   #searching 
                sleep(0.5)
                keyboard.press('enter')
                sleep(0.5)
                continue

        elif "launch" in Data:
            webName = Data.replace("launch ","")
            link = "https://www." + webName + ".com/"
            webbrowser.open(link)

        elif 'search' in Data and 'in google' in Data:  # searching in google.  
            search = Data.replace("search ", "").replace("in google ", "")
            print("searching " + search)
            speak("searching " + search)
            pywhatkit.search(search)

        elif 'search' in Data and 'on youtube' in Data: #searching on youtube.
            search = Data.replace("search ", "").replace(" on youtube", "")
            speak("searching " + search)
            result = "https://www.youtube.com/results?search_query=" + search
            webbrowser.open(result)
            speak("this is what I found")
 
        elif 'play' in Data:  # playing song in Youtube.
            song = Data.replace("play", "").replace("on youtube ", "")
            print("Playing" + song)
            speak("playing" + song)
            pywhatkit.playonyt(song)

        elif "shutdown" in Data and "system" in Data:
            speak("shutting down in 5 seconds")
            speak("count down begins now. 5. 4. 3. 2. 1. ")
            sleep(0.5)
            os.system("shutdown /s /t 1")

        elif "restart" in Data and "system" in Data:
            speak("restarting in 5 seconds")
            speak("count down begins now. 5. 4. 3. 2. 1. ")
            sleep(0.5)
            os.system("shutdown /r /t 1")

        elif "lock" in Data and "system" in Data: # put the system in sleep mode
            speak("system will sleep in 3 seconds")
            speak("count down begins now. 3. 2. 1. ")
            import ctypes
            ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

        elif "gpt" in Data or "ask gpt" in Data or "ask chat gpt" in Data or "ppt" in Data :
            Data = Data.replace("ask gpt", "").replace("gpt", "").replace("ppt", "").replace("ask chat gpt", "").replace("ask chatgpt", "")
            speak("asking gpt")
            webbrowser.open('https://chat.openai.com/')
            pyautogui.sleep(4) 
            pyautogui.typewrite(Data)
            sleep(0.5)
            pyautogui.press('tab')
            pyautogui.press("enter")
            speak("this is what he found")

        else:
            speak("sorry i didn't get it!")
            # Reply = ReplyBrain(Data)
            # speak(Reply)


if __name__ == "__main__":
    while True:
        order = MicExecution()

        if "hey jarvis" in order or "hello jarvis" in order or "no" in order:
                # speak("  ")
                msg = ["hello sir.", "hey sir."]
                speak(random.choice(msg))
                msg = ["I'm here to assist you sir.","waht would you like, to do today"]
                speak(random.choice(msg))
                MainExecution()

        elif "wake up" in order :
                # from playsound import playsound
                # playsound("D:\\JARVIS\\jarvis by kaushik\\sound\\yawn.mp3")
                msg = ["i'm right here sir", "i am back sir", "i was in the deep sleep, anyway" ]
                # speak(random.choice(msg))
                # speak("I was in the deep sleep, anyway")

                msg = ["I'm here to assist you sir.", "how can i help you sir" ]
                speak(random.choice(msg))
                MainExecution()


        elif "good bye" in order or "bye" in order or "exit" in order :
            speak("Goodbye sir, I love to see you again.")
            sys.exit()

        elif percent < 15 and not plugged:
            speak("sir, the battery level is less than 15 percent.")
            speak("I need power to live. otherwise i will die . ")
            speak("so, please charge me")


