# simon_voice.py
''' This script is the basis for Simon's voice.
    Google Voice API is used to recognize words
    and translate to printed text using machine learning.
    We have customized this to Simon's unique personality to respond to users. '''

# Instructions:
# pip install SpeechRecognition
# if an error occurs you need to do this as well:
# brew install portaudio
# pip install PyAudio
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import speech_recognition as sr
import random
#for speech
from gtts import gTTS
import os
language = 'en-US'

jokes = ["Why do we tell actors to break a leg?\nBecause every play has a cast.",
		"What happens to a frog's car when it breaks down?\nIt gets toad away.",
		"Why isn't the turkey hungry at Thanks giving?\nBecause it's stuffed.",
		"Why do witches wear name tags?\nSo they know which witch is which.",
		"My friend thinks he is so smart, told me today that onion is the only food that makes you cry\nSo I threw a coconut at his face.",
		"What stays in one corner but travels around the world?\nA stamp.",
		"What do you call a pig that does karate?\nPork chop.",
		"Why does Humpty Dumpty love autumn?\nBecause he had a great fall last year.",
		"Did you hear about the kidnapping at school today?\nIt's alright, he's awake now.",
		"Does february march? I don't know, but april may"]

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("instructions").sheet1

data = sheet.get_all_records()
# print(data)

r = sr.Recognizer()
myText = 'Hello, my name is Simon. How can I help you?'
print(myText)

output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")
while True:
    command = 'blank'
    with sr.Microphone() as source:
        print('Speak Anything: ')
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print('You said : {}'.format(command))



        except:
            print('Sorry, Simon did not catch that.')

    if command.find("joke") >0:
        myText = jokes[random.randint(0, 9)]
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")

        #print(jokes[random.randint(0, 9)])

    if command.find("exercise") >= 0:
        sheet.insert_row([command])
        # print(type(text)) #str
        myText = 'Okay, Initializing exercise sequence'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
       # print('Initializing exercise sequence')


    if command.find("stop")>=0 or command.find("exit") >= 0 or command.find("goodbye") >= 0 or command.find("done") >= 0 or command.find("finished") >= 0 or command.find("close") >= 0:
        myText = 'Goodbye, it was nice talking to you'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
        print('Goodbye, it was nice talking to you')
        break;
        break;
