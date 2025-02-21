def chatbot():
    print("Chatbot: Hey! How can I help you today?")
    print("(Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Okay, Have a great day ahead!")

        elif "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you?" in user_input:
            print("Chatbot: I'm just a ruled based chatbot! How about you?")
        elif "current time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "what day is today?" in user_input:
            from datetime import datetime
            current_day = datetime.now().strftime("%A")
            print(f"Chatbot: Today is {current_day}.")
        elif "where are you from?" in user_input:
            print("Chatbot: I'm a virtual assistant. I don't have a physical place of origin.")
        else:
            print("Chatbot: I'm Sorry, I don't understand that. Can you ask something else?")

chatbot()


