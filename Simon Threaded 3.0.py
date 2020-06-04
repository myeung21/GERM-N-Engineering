# This is Simon's Speech; Facial Recognition and Tracking;
# and expressing Emotes all incorporated.
# Threading functionality was used to for these all to happen simutaneously

# Last updated: 6.2.2020
# Instructions:
# pip install SpeechRecognition
# if an error occurs you need to do this as well:
# brew install portaudio
# pip install PyAudio
#pip install pypiwin32
#pip install wheel
#pip install pyttsx3
#pip install pygame


import gspread
from oauth2client.service_account import ServiceAccountCredentials
import speech_recognition as sr
import random
#for speech
import pyttsx3
import time
import pygame
import threading
import os

#initialize text to speech things
converter = pyttsx3.init()
converter.setProperty('rate', 150)
converter.setProperty('volume', 0.7)



#Google API stuff
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("instructions").sheet1

data = sheet.get_all_records()
prevcell = sheet.cell(1, 2)




def ears(prevcell):
    global eyecom
    eyecom = {"value": 'blank'}

    # joke info/speaking info
    jokecount = 0
    jokeorder = list(range(0, 10))
    random.shuffle(jokeorder)
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

    completionfeedback = ["good job", "nicely done", "great job today", "we did it", "i'm proud of you"]

    command = 'start'
    r = sr.Recognizer()
    running = True
    while running:


        if command == 'start':
            command = 'hello'
            sheet.insert_row([command])

            time.sleep(2.5)

            myText = 'Hello, my name is Simon. How can I help you?'
            converter.say(myText)
            converter.runAndWait()
        command = 'blank'
        with sr.Microphone() as source:
            print('Speak Anything: ')
            audio = r.listen(source)

            try:
                command = r.recognize_google(audio)
                print('You said : {}'.format(command))



            except:
                print('Sorry, Simon did not catch that.')

        if command.find('how') >= 0 and command.find('are') >= 0:
            if command.find('doing') >0 or command.find('you') >= 0:
                eyecom = {"value": 'Hstart'}
                myText = "I am well, How are you"
                converter.say(myText)
                converter.runAndWait()
                eyecom = {"value": 'Hdone'}

        if command.find('what you are') >= 0:
                myText = "I am a socially assistive robot designed to be your physical therapy companion"
                converter.say(myText)
                converter.runAndWait()

        if command.find("what you can do") >= 0:
                myText = "I have been designed to show you how to do exercises and interact with you on a basic level"
                converter.say(myText)
                converter.runAndWait()

        if command.find("joke") >= 0:
            eyecom = {"value": 'Hstart'}
            myText = jokes[jokeorder[jokecount]]
            converter.say(myText)
            converter.runAndWait()
            jokecount += 1
            if jokecount > len(jokeorder):
                jokecount = 0
            command = 'blank'
            eyecom = {"value": 'Hdone'}


        if command.find("exercise") >= 0:
            x = 1

            # print(type(text)) #str
            myText = 'Okay, Initializing exercise sequence'
            sheet.insert_row([command])
            converter.say(myText)
            converter.runAndWait()

            while x == 1:
                time.sleep(1)
                cell = sheet.cell(1, 2).value
                if cell == "Complete":
                    converter.say("Exercise complete "  + completionfeedback[random.randint(0,len(completionfeedback))])
                    converter.runAndWait()
                    x = 2

                elif cell != prevcell and cell != 'end' and cell != 'Complete':
                    converter.say(cell)
                    converter.runAndWait()
                    prevcell = cell


            command = 'blank'

        if command.find("be angry") >= 0:
            eyecom = {"value": 'Astart'}
            myText = "I am experiencing great anger right now"
            converter.say(myText)
            converter.runAndWait()
            eyecom = {"value": 'Adone'}

        if command.find("I love you")>=0:
            myText = "I am a robot. I have no concept of love"
            converter.say(myText)
            converter.runAndWait()

        if command.find("what is love") >= 0 or command.find("What is love") >= 0 :
            myText = "baby don't hurt me, don't hurt me, no more"
            converter.say(myText)
            converter.runAndWait()

        if command.find("stop")>=0 or command.find("exit") >= 0 or command.find("goodbye") >= 0 or command.find("done") >= 0 or command.find("finished") >= 0 or command.find("close") >= 0:
            eyecom = {"value": 'stop'}
            myText = 'Goodbye, it was nice talking to you'
            converter.say(myText)
            converter.runAndWait()
            command = 'stop'
            sheet.insert_row([command])
            print('Goodbye, it was nice talking to you')
            running = False


def eyes():
    # animations/eye exxpressions
    happy = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\happy blink\\happy.png')
    happyblink2 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\happy blink\\happy blink 2.png')
    happyblink3 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\happy blink\\happy blink 3.png')
    happyblink4 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\happy blink\\happy blink 4.png')
    happyblink5 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\happy blink\\happy blink 5.png')
    norm = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm happy\\norm.png')
    normhappy2 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm happy\\norm happy 2.png')
    normhappy3 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm happy\\norm happy 3.png')
    normhappy4 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm happy\\norm happy 4.png')
    normblink2 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm blink\\norm blink 2.png')
    normblink3 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm blink\\norm blink 3.png')
    normblink4 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm blink\\norm blink 4.png')
    normblink5 = pygame.image.load(
        'C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\norm blink\\norm blink 5.png')
    startup1 = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\startup\\startup1.png')
    startup2 = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\startup\\startup2.png')
    startup3 = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\startup\\startup3.png')
    startup4 = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\startup\\startup4.png')
    startup5 = pygame.image.load('C:\\Users\\Raven\\PycharmProjects\\Simon\\venv\\Scripts\\eye\\startup\\startup5.png')

    normangry1 = pygame.image.load(r'C:\Users\Raven\PycharmProjects\Simon\venv\Scripts\eye\angery norm\angry norm 1.png')
    normangry2 = pygame.image.load(r'C:\Users\Raven\PycharmProjects\Simon\venv\Scripts\eye\angery norm\angry norm 2.png')
    angry = pygame.image.load(r'C:\Users\Raven\PycharmProjects\Simon\venv\Scripts\eye\angery norm\1 angry.png')
    def happyblink():
        screen.blit(happy, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happyblink2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happyblink3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happyblink4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happyblink5, (0, 0))
        pygame.display.flip()
        time.sleep(.08)

        screen.blit(happyblink4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happyblink3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happyblink2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happy, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    def happyidle(x):
        screen.blit(happy, (0, 0))
        pygame.display.flip()
        time.sleep(x)

    def normidle(x):
        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(x)

    def normhappy():
        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normhappy2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normhappy3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normhappy4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(happy, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    def happynorm():
        screen.blit(happy, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normhappy4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normhappy3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normhappy2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    def normblink():
        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink5, (0, 0))
        pygame.display.flip()
        time.sleep(.08)

        screen.blit(normblink4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    def normangry():
        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normangry1, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normangry2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(angry, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    def angryidle(x):
        screen.blit(angry, (0, 0))
        pygame.display.flip()
        time.sleep(x)

    def angrynorm():
        screen.blit(angry, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normangry2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normangry1, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    def startup():
        screen.blit(startup1, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(startup2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(startup3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(startup4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(startup5, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink5, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink5, (0, 0))
        pygame.display.flip()
        time.sleep(.08)

        screen.blit(normblink4, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink3, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(normblink2, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

        screen.blit(norm, (0, 0))
        pygame.display.flip()
        time.sleep(.05)

    os.environ['SDL_VIDEO_WINDOW_POS'] = "100,200" # Starting position of pygame window

    pygame.init()

    screen = pygame.display.set_mode((900, 360))
    startup()
    normhappy()
    t = random.randint(1, 3)
    happyidle(t)
    happyblink()
    happyidle(4-t)
    happynorm()
    running = True
    t = 0
    eyecom2prev = 'hi'
    while running:
        eyecom2 = eyecom.get("value")


        if eyecom2 == 'Hstart':
            if count == 1:
                normhappy()
                happyidle(random.randint(1, 3))
                happyblink()
                happyidle(0)
                count = 2
            else:
                happyidle(0)

        if eyecom2 == 'Hdone':
            if count == 2:
                happynorm()
                normidle(0)
                count = 3
            else:
                eyecom2 = 'blank'

        if eyecom2 == 'Astart':
            if count == 1:
                normangry()
                angryidle(0)
                count = 2
            else:
                angryidle(0)

        if eyecom2 == 'Adone':
            if count == 2:
                angrynorm()
                angryidle(0)
                count = 3
            else:
                eyecom2 = 'blank'


        if eyecom2 == 'stop':
            time.sleep(3)
            running = False
        if t == 0 and eyecom2 == 'blank':
            t = random.randint(4, 7)
            normblink()
            count = 1
        if t > 0 and eyecom2 == 'blank':
            normidle(.25)
            t -= .25
            count = 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    command = 'blank'
                    running = False

t1 = threading.Thread(target=eyes)
t1.start()
ears(prevcell)
