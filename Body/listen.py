import speech_recognition as sr
from googletrans import Translator 

def MicExecution():
    
    # It takes microphone input from the user and return string output.

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)  # Till 8sec goes into listening mode...
 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #language='hi' for hindi 
        print(f"You saidddd: {query}\n")
        if "jarvis" in query:
            query = query.replace("jarvis",'')
 
    except Exception as e:
        # print(e)
        print("sorry, say that again please...")
        return "None"
    query=str(query).lower()
 
    return query
    


 