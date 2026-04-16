import pyttsx3

engine = pyttsx3.init()

def speak_text(text):
    engine.say(text)

name = "User"

while True:
    user_text = input("Enter your message: ").lower()

    # Exit condition
    if user_text in ["exit", "quit", "bye"]:
        response = "Goodbye! Have a nice day."
        print(response)
        speak_text(response)
        engine.runAndWait()
        break

    # Name extraction (your logic kept)
    if "my name is" in user_text:
        name = user_text.split("my name is")[-1].strip()
    elif "name is" in user_text:
        name = user_text.split("name is")[-1].strip()

    # Greeting
    if user_text in ["hi", "hello"]:
        response = f"Hello {name}! How can I help you?"

    # When name is mentioned → start conversation flow
    elif "name" in user_text:
        response = f"Good morning {name}, what's your plans today?"
        print(response)
        speak_text(response)
        engine.runAndWait()

        # Take next input (plans)
        plans = input("Your plans: ")

        response = "That sounds great, have fun boss!"

    else:
        response = "Sorry, I didn't understand that."

    print(response)
    speak_text(response)
    engine.runAndWait()
