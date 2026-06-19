def chatbot_reply(message):
    if message=="HELLO":
        print("hi")
    elif message=="HELLO":
        print("hi")
    elif message=="HOW ARE YOU":
     print("I am fine what about you.")
    elif message=="I AM FINE":
       print("good,How can I help you today?")
    elif message=="WHAT IS PYTHON":
        print(": Python is a programming language used for web development, data science, automation, and artificial intelligence.")
    elif message=="CAN YOU HELP ME LEARN CODING?":
        print("Of course! I can help you learn programming step by step.")
    elif message=="THANK YOU" :
        print("You're welccome")
    elif message=="BYE":
        print("Goodbye! Have a great day.")
    else:
        print("currently i am not able to answer this query ")
print("welcome to chatbot")
while True:
    message=input("say something or (write DONE for exit)").upper()
    if message=="DONE":
        print("Thanku for using me")
        break
    chatbot_reply(message)

print("--------------------------")
print("      | COME AGAIN |")
print("--------------------------\n")