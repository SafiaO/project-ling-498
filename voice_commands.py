import speech_recognition as sr


def interpret_command(command):
    if "move forward" in command:
        return "forward"
    elif "move backward" in command:
        return "backward"
    elif "turn left" in command:
        return "left"
    elif "turn right" in command:
        return "right"
    elif "stop" in command:
        return "stop"
    elif "light" in command:
        return "light"
    elif "exit" in command:
        return "exit"
    else:
        return "unknown"


def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source)
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Error:", e)

if __name__ == "__main__":
    while True:
        recognized_text = recognize_speech()  # Store recognized speech in a variable
        action = interpret_command(recognized_text.lower())  # Interpret recognized speech
        if action == "exit":
            print("Exiting program...")
            break
        elif action != "unknown":
            print("Performing action:", action)
        else:
            print("Command not recognized. Please try again.")
