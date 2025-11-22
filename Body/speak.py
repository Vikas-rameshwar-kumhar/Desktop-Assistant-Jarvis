## windows based voice
## offline

import pyttsx3
def speak(Text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate',120) #speed of ai voice
    print("")
    print(f"Jarvis said: {Text}.")
    print("")
    engine.say(Text)
    # engine.save_to_file('file_name')   #to save the command
    engine.runAndWait()





