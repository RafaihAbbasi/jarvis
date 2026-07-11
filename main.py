import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize engines ONCE globally
recognizer = sr.Recognizer()

def speak(text):
    # Initialize a clean engine instance inside the function
    engine = pyttsx3.init()

    # Optional: Slow down the speech rate slightly (default is 200, which can sound rushed)
    engine.setProperty('rate', 175) 
    
    print(f"Jarvis says: {text}") # Visual confirmation
    engine.say(text)
    engine.runAndWait()
    
    # This prevents the engine from locking up your audio driver
    del engine

def process_command(c):
    # Added a fallback print so you can see what Jarvis heard as the command
    print(f"Processing command: {c}")
    
    if "open google" in c.lower() or "open the google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower() or "open the youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower() or "open the facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower() or "open the linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in c.lower() or "open the github" in c.lower():
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    elif "open whatsapp" in c.lower() or "open the whatsapp" in c.lower():
        speak("Opening WhatsApp")
        webbrowser.open("https://web.whatsapp.com")
    else:
        speak("I heard the command, but I don't know how to do that yet.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    # Calibrate once at startup to avoid constant timeouts
    with sr.Microphone() as source:
        print("Calibrating mic for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Jarvis is ready.")

    while True:
        try:
            # Stage 1: Continuous listening for the wake word
            with sr.Microphone() as source:
                print("\nListening for wake word...")
                # phrase_time_limit=3 gives you plenty of time to say "Hey Jarvis"
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=3)
            
            print("Recognizing wake word...")
            word = recognizer.recognize_google(audio).lower()
            print(f"Heard: {word}")

            # Using 'in' instead of '==' keeps punctuation or background noise from breaking it
            if "jarvis" in word:
                speak("Yes, how can I help you?")
                
                # Stage 2: Promptly listen for the actual command
                with sr.Microphone() as source:
                    print("Jarvis Active... Listening for command...")
                    # Give them 5 seconds to say the command
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    
                    print("Recognizing command...")
                    command = recognizer.recognize_google(audio)
                    process_command(command)
                    
        except sr.UnknownValueError:
            # Silently pass on unrecognised ambient noise or mumbles during the wake word phase
            print("Did not recognize speech. Retrying...")
        except Exception as e:
            print(f"Error encountered: {e}")