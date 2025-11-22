import os 
import keyboard
import pyautogui
import webbrowser
from time import sleep 
# from Body.speak import speak


def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        webName = Query.replace("visit ","")
        link = "https://www." + webName + ".com/"
        webbrowser.open(link)
        return True

    elif "launch" in Query:
        webName = Query.replace("launch ","")
        link = "https://www." + webName + ".com/"
        webbrowser.open(link)
        return True

    elif "open" in Query:
        openApp = Query.replace("open ","")

        if "chrome" in Query or "google" in Query:
            # speak("opening sir")
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True

        elif 'open youtube' in Query:
            # speak("opening Youtube")
            print("    Opening YouTube")
            webbrowser.open("youtube.com")
            # speak("what would you like to search?")
            print("what can i search for you, sir")
            search = Query.replace("open youtube", "")
            print("searching" + search)
            result = "https://www.youtube.com/results?search_query=" + search
            webbrowser.open(result)
            print("this is what i found")


            return True

        elif "file" in Query:
            # speak("opening file manager")
            codepath = "explorer.exe"
            os.startfile(codepath)
            return True

        # elif "vs code" in Query or "code" in Query:
        #     os.startfile(r"C:\Users\shank\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        else:
            pyautogui.press('win')    #pressing window key
            sleep(1)
            keyboard.write(openApp)   #searching 
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
            return True
    
    elif "start" in Query:
        openApp = Query.replace("start ","")

        if "chrome" in Query:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True

        elif "vs code" in Query:
            os.startfile(r"C:\Users\shank\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            return True

        else:
            pyautogui.press('win')
            sleep(1)
            keyboard.write(openApp)
            sleep(1)
            keyboard.press('enter')
            sleep(0.5)
            return True



# OpenExe("open code")
# OpenExe("open youtube")
# OpenExe("launch facebook")
# OpenExe("visit instagram")

