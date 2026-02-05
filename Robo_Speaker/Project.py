import pyttsx3
import speech_recognition as sr
if __name__=="__main__":
    print("Hello I am a robo speaker and I can speak for you.")
    engine = pyttsx3.init()
    while True:
        a=input("Choose whether you want me to recite or write or exit:")
        if(a.lower()=="recite"):
            s=input("Enter what you want me to recite:")
            engine.say(s)
            engine.runAndWait()
            if s=="exit":
                break
        elif(a.lower()=="write"):
            recognizer = sr.Recognizer()     
            with sr.Microphone() as source:
                print("Please speak something so that I can write it(you have 2 seconds to start)...")
                recognizer.adjust_for_ambient_noise(source)
                try:
                    # Listen with timeout
                    audio = recognizer.listen(source,timeout=2)
                    print("Recognizing...")
                    text = recognizer.recognize_google(audio)
                    print("You said: ",text)
                    if text=="exit": 
                        break
                except sr.WaitTimeoutError:
                    print("Timeout: No speech detected within 2 seconds.")
                except sr.UnknownValueError:
                    print("Sorry, I could not understand the audio.")
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
        elif(a.lower()=="exit"):
            break
        else:
            print("Invalid choice. Please type recite, write, or exit.")