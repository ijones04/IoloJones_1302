# -*- coding: utf-8 -*-
"""MainChatbot.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KsZ65ZhsJJoCyDw1CUPy3Sog5Cw0uKV8
"""

from tensorflow.keras.models import load_model
model = load_model('chatbot_model.h5') # load model
import json # import neeeded libraries
import random 
intents = json.loads(open('intents.json').read()) # import intents
words = pickle.load(open('words.pkl','rb')) # import words pickle
classes = pickle.load(open('classes.pkl','rb')) # import classes pickle

def clean_up_sentence(sentence): # split sentence up
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words] # lemmatize each word
    return sentence_words # return bag of words, 0 if the word doesnt exist, 1 if the word does

def bow(sentence, words, show_details = True):
    sentence_words = clean_up_sentence(sentence) # tokenize the patter
    bag = [0]*len(words) # vocab matrix of n words
    for s in sentence_words: # for each s in sentence_words
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1 #if current word is in vocab position bag[i]=1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model): # class (type) prediction
    p = bow(sentence, words,show_details=False) # filtering out predictions lower than an error threshold
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25 # bottom 25%
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True) # sort by liklihood, most likely to least
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list
   
def getResponse(ints, intents_json): # for the response
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text): # to respond
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res

import tkinter
from tkinter import *
#Creating GUI using tkinter
def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + res + '\n\n')

        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = Tk()
base.title("Hello")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state = DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()