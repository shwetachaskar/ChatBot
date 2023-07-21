from tkinter import *
import pyttsx3 as pp
from PIL import Image, ImageTk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer



'''engine= pp.init()

voices=engine.getProperty('voices')
print('voices')

engine.setProperty('voice', voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()'''




chatbot= ChatBot ('My Bot')

conversation = [
    "Hello",
    "Hi there!",
    "My name is Bot, i am created by Shweta.",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

#answer=chatbot.get_response("thank you")
#print(answer)

#print("Talk to bot")
#while True:
#    query = input()
#    if query == 'exit' :
#        break
#    answer = chatbot.get_response(query)
#    print("bot :", answer)

main = Tk()
main.geometry("650x650")

main.title("My Chat bot")

image=Image.open("PicsArt_02-29-03.20.38.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(main, image=photo)
label.pack(pady=5)

def ask_from_bot():
    query=text.get()
    answer_from_bot=chatbot.get_response(query)
    msgs.insert(END, "you :" + query)
    msgs.insert(END, "bot :" + str(answer_from_bot))
    speak(answer_from_bot)
    text.delete(0,END)
    msgs.yview(END)

frame=Frame(main)

sc=Scrollbar(frame)
msgs=Listbox(frame, width=80, height=20, yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

text=Entry(main, font=("Verdana", 20))
text.pack(fill=X, pady=10)

btn=Button(main, text="Ask from bot",font=("Verdana", 20), command=ask_from_bot)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()

# going to bind main window with enter key...

main.bind('<Return>', enter_function)

main.mainloop()
