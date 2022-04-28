# -*- coding: utf-8 -*-
"""train_chatbot.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1loVt9tJx24c9CUBNcClmodhzDr6jZPg-
"""

import nltk 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD
import random

words = [] # create an empty list to hold the words 
classes = [] # create an empty list to hold the classes (convo types)
documents = [] # create an empty list to hold the documents
ignore_words = ['?', '!'] # we want to ignore punctuation such as "?" and "!"
data_file = open('intents.json').read() # read the json file to get our patterns and responses
intents = json.loads(data_file) # define intents

for intent in intents['intents']: # for element of intents
    for pattern in intent['patterns']: # iterate through the patterns column of intents
        w = nltk.word_tokenize(pattern) # split up into individuals
        words.extend(w) # add w to the end of the words list
        documents.append((w, intent['tag'])) # append to documents list
        if intent['tag'] not in classes: # if not in the classes list
            classes.append(intent['tag']) # add to the classes list

# group together the different forms of a word (upper and lower etc) so they can be analyzed as a single item
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words] # if not in ignore_words, words = [words with removed duplicate words with uppers and lowers etc]
words = sorted(list(set(words))) # sort the words list
classes = sorted(list(set(classes))) # sort the classes list
print (len(documents), "documents") # see how many documents there are
print (len(classes), "classes", classes) # see how many classes there are
print (len(words), "unique lemmatized words", words) # see how many words we have in our vocab list

pickle.dump(words,open('words.pkl','wb')) # steralize the object heirarchy of words
pickle.dump(classes,open('classes.pkl','wb')) #  steralize the object heirarchy of classes

training = [] # create an empty list to hold our training data
output_empty = [0] * len(classes) # create an empty list the length of our classes to hold the output

for doc in documents: # look through the training set of data
    bag = [] # create an empty list to hold our words 
    pattern_words = doc[0] # list of pattern words after splitting the larger body of multiple patterns
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words] # group together the different forms of the patterns
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0) # if w is found in the current pattern
    output_row = list(output_empty) 
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row]) # add to training data list

random.shuffle(training) # shuffle features of training data
training = np.array(training) # create a numpy array from our shuffled training data

# create training and testing datas
train_x = list(training[:,0]) # patterns
train_y = list(training[:,1]) # intents -  classes
print("Training data created") # to show we have trained the data

# create a 3 layered model, first layer 128 neurons, second 64 and third with the number of intents to predict output intent-neurons using 'softmax'
model = Sequential() # grouping
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu')) # first layer
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu')) # second layer
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax')) # third layer

sgd = SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True) # stochastic gradient descent using Neterov = True to calculate the decay of the model
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy']) # compile the model

hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1) # fitting the model
model.save('chatbot_model.h5', hist) # saving the model as chatbot_model.h5
print("model created") # to show the model has been created