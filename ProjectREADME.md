# IoloJones_1302
 ChatBot ReadMe - Iolo Jones
About the project
The chatbot will be trained on the dataset which contains categories, patterns and responses. We will use a recurrent neural network to classify which the user’s message belongs to and then we will give a random response from the list of responses.
The data set used is ‘intents.json’. This JSON file contains a collection of patterns the chatbot must find and also holds all of the responses that will be returned to the user. It holds a series of user patterns and a number of corresponding responses that make contextual and logical sense.
I set out to build a chatbot using Python3. First, I needed to look at the files needed for the project and their structures. We are to use and create 6 files; ‘intents.json’, ‘train_chatbot.py’, ‘words.pkl’, ‘classes.pkl’, ‘chatbot_model.h5’ and ‘MainChatbot.py’. The intents file holds the patterns and responses as stated before. The train_chatbot file is a python file that was used to build and train the chatbot. We then have pickle files words.pkl and classes.pkl, which holds our vocabulary and categories. Information about the trained model is held in the model chatbot_model. Finally, the python file chatgui.py is where the GUI for the chatbot is implemented and allows user-friendly interaction.
How to run the code
1. Go to Mainchatbot.py.
2. Run the code on your machine
3. Ask drug related questions (from intents.json file).
Implementing the project
There were 5 steps required in the building of a working chatbot. These steps are defined as follows:
1. Import and load a data file.
2. Preprocess the data.
3. Split the data into training and testing data.
4. Building the model.
5. Predicting the response.
The libraries needed for a successful back-end of the project are nltk, numpy, json,
pickle, tensorflow and random. For the front-end GUI, tkinter must be imported.
Object-oriented coding
To rewrite the code to where this is an object-oriented design, where a user must only implement a pre-defined class, we would have to look at our procedural code and move the logic from the procedure into a base class.
To apply the chatbot to another datasource
A chatbot could be used to collect user feedback. For such a task, we could have a JSON file which contains a number of questions to be asked by the chatbot, as well as responses to feedback. For example, the chatbot may ask the user to rate their experience on a scale 1 through 5, and then alter the response based upon what the user answered. So to apply the chatbot to another data source should be fairly simple.
