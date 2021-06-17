from chatterbot import ChatBot
# chatterbot = ChatBot

# give the chatbot a name
chatbot = ChatBot("Hello, Am Your Mathematical Chatbot")

# add theese packages to train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# now add a personality to your chatbot
# name the personality equivalent with the program at hand
# here you will use question then answer form
personality_AIRR = []

trainer_personality = ListTrainer(chatbot)
trainer_personality = ListTrainer(chatbot)
# these are the personalities from Corpus
trainer = ChatterBotCorpusTrainer(chatbot)

# now after the personalities are set, do the actual training
trainer.train('chatterbot.corpus.english')
trainer_personality.train(personality)
trainer_personality.train(personality)
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import wikipedia
import pyttsx3
from wx.core import MenuBar
# Import for the GUI 
from chatbot_gui import ChatbotGUI
from chatterbot import ChatBot
# give the chatbot a name
#function to read text to speech
#function to read text to speech
def read_text_outloud(text_to_read):
    # initialize the converter
    converter = pyttsx3.init()
    converter.setProperty('rate',150)
    converter.setProperty('volume',0.7)
    converter.say(text_to_read)
    converter.runAndWait()
    user_main_topic_choice = input("") 
# and the string is the + with the variable attached to a print statement that makes a string
dual_output ="\t\t  " + user_main_topic_choice + " \n"
# give the AI the ability to research for us
# create a variable to hold the research results
dual_output = "\n\t " + user_main_topic_choice + " *** \n"
air_raw_research_results = wikipedia.page(user_main_topic_choice)
print(" " + user_main_topic_choice + "\n")
read_text_outloud(dual_output)
chatbot = ChatBot("")
app = ChatbotGUI(
    title="AI Research Robots ChatBot Devision -- Code Name -- 'AIRR CBD'//// KEY WORDS---Home, Optical, Meditation, Strategy, Grammer, Assess, ChatBot, Extra, Clear Chat, Bye",
    gif_path="AIRR Face.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 150,
        "volume": 2.0,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    }
)
trainer_personality = ListTrainer(chatbot)
trainer_personality = ListTrainer(chatbot)
# these are the personalities from Corpus     
trainer = ChatterBotCorpusTrainer(chatbot)
dual_output = (chatbot)
# now after the personalities are set, do the actual training
trainer.train('chatterbot.corpus.english')
trainer_personality.train(personality)
trainer_personality.train(personality_Researcher)


@app.event
def on_message(chat: ChatbotGUI, text: str):
    print("User Entered Message: " + text) 
 
    
    if text.lower().find("") != -1:
        chat.send_ai_message("")
    elif text.lower().find("") != -1:
        chat.clear("")
    elif text.lower().find("bye") != -1:
            # define a callback which will close the application
        def close():
            chat.exit()
        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("", callback=close)
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)
       
        #function to read text to speech
app.run() 