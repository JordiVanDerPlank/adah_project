import speech_recognition as sr
import random
import triggerWords
import webbrowser
import requests
import numpy
# import GetFromWebpage as getData

from tkinter import *

# Initialize the recognizer
r = sr.Recognizer()

import socket, string, threading, cursewords, time

global NICK, PASS

HOST = "irc.twitch.tv"
NICK = ""
PORT = 6667
PASS = ""


# -------------------------------ADAH FRAMES LOOKS---------------------------#

class Screen(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# SCREEN SIZE AND TITLE
gui = Tk()
gui.geometry("640x480")
gui.configure(bg="#18181b")
app = Screen(master=gui)
app.master.title("ADAH v1.7")
app.configure(bg="#18181b")

# STOP PROGRAM WHEN RED CROSS IS PRESSED
gui.protocol("WM_DELETE_WINDOW", gui.destroy)

scroll = Scrollbar(gui)
scroll.pack(side=RIGHT, fill=Y)

# TEXT SHOWN ON SCREEN
eula = Text(gui, wrap=NONE, yscrollcommand=scroll.set, bg="#18181b", foreground="white")

global connected


def showAdah():
    if btnText.get() == "Quit":
        sys.exit(0)

    else:
        if (btnText.get() != "Connect"):
            connected = True
        eula.pack(side="bottom")
        global NICK, PASS
        NICK = str.lower(nickName.get())
        PASS = auth.get()
        # connected = False
        firstStart()


def sendToAuth():
    webbrowser.open("https://twitchapps.com/tmi/")


btnText = StringVar()
btn = Button(app, textvariable=btnText, command=showAdah, foreground="white")
btnText.set("Connect")
# Set the position of button on the top of window
btn.pack(side='top')
btn.configure(bg="#9147ff")

btnOAuth = Button(app, text="Get OAuth", command=sendToAuth, foreground="white")
btnOAuth.pack(side='right', padx="5")
btnOAuth.configure(bg="#9147ff")

# nickname input
nickNameLabelText = StringVar()
nickNameLabelText.set("Nickname")
nickNameLabelDir = Label(app, textvariable=nickNameLabelText, height=4)
nickNameLabelDir.configure(foreground="white", bg="#18181b")
nickNameLabelDir.pack(side="left")

nickName = Entry(app)
nickName.pack(side="left")

# authorization code chat
authLabelText = StringVar()
authLabelText.set("Authorization key")
authLabelDir = Label(app, textvariable=authLabelText, height=4)
authLabelDir.configure(foreground="white", bg="#18181b")
authLabelDir.pack(side="left")

auth = Entry(app, show="*")
auth.pack(side="left")

# ---------------------------------ADAH LISTENING AND REPLYING---------------------------------------#

global s
global usersInChat
usersInChat = []


# global connected

def send_message(message):
    s.send(bytes("PRIVMSG #" + NICK + " :" + message + "\r\n", "UTF-8"))


paused = False

restart = False

global cooldownOn
cooldownOn = False

global newUsersCounted
newUsersCounted = 0


def turnoffCooldown():
    # eula.insert("1.0", "TURNING OFF COOLDOWN")
    global cooldownOn
    cooldownOn = False
    return


def checkMessages():
    while restart == False:
        try:
            for line in str(s.recv(4096)).split('\\r\\n'):
                subscribed = False
                userMod = False
                # for line in str(s.setblocking(True)).split('\\r\\n'):
                parts = line.split(':')

                if len(parts) < 3:
                    continue

                if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                    message = parts[2][:len(parts[2])]

                usernamePart = 1

                for idx, val in enumerate(parts):
                    if "PRIVMSG" in val:
                        usernamePart = idx


                usernamesplit = parts[usernamePart].split("!")
                username = usernamesplit[0]

                if username == "theshelfman":
                    username = "the shelfman"


                if ";subscriber=" in username or ";flags" in username:
                    message = parts[3][:len(parts[2])]
                    usernamesplit = parts[2].split("!")
                    username = usernamesplit[0]

                elif "PRIVMSG" not in parts[1] and "tmi.twitch.tv" not in parts[1]:
                    continue

                global paused, cooldownOn, newUsersCounted

                usersToIgnore = [NICK, "streamlabs", "soundalerts", "nightbot", "streamcaptainbot", "grugsbot"]


                if (NICK == "theshelfman"):
                    usersToIgnore.append("the shelfman")

                if username not in usersInChat and "tmi.twitch.tv" not in username and username not in usersToIgnore:
                    usersInChat.append(username)
                    if cooldownOn is False:
                        cursewords.SpeakText("Hello " + username + ", welcome to the stream!")
                        cooldownOn = True
                        thread3 = threading.Timer(15, turnoffCooldown)
                        thread3.start()
                    else:
                        newUsersCounted += 1
                        if newUsersCounted >= 5:
                            newUsersCounted = 0
                            cursewords.SpeakText("Hello everybody. Welcome to the stream!")

                # seperate all tag information
                badgeInfoSplit = line.split(";")
                for i in badgeInfoSplit:
                    if "mod=1" in i:
                        userMod = True
                    else:
                        userMod = False

                badgeInfo = badgeInfoSplit[0].split("=")

                if len(badgeInfo) >= 2:
                    if "subscriber" in badgeInfo[1]:
                        subscribed = True

                if len(badgeInfoSplit) >= 2:
                    userBadges = badgeInfoSplit[1].split("=")
                eula.insert("1.0", username + " : " + message + "\n")

                if ("NOTICE *" in username):
                    nickNameLabelDir.pack(side='left')
                    nickName.pack(side='left')
                    authLabelDir.pack(side='left')
                    auth.pack(side='left')
                else:
                    connected = True
                    authLabelDir.pack_forget()
                    auth.pack_forget()
                    nickName.pack_forget()
                    nickNameLabelDir.pack_forget()
                    btnOAuth.pack_forget()
                    btn.pack_forget()
                    # btnText.set("Quit")

                message = message.lower()
    
                

                if (message == "pause" and (username == NICK or "mod" in userBadges[1] or username == "the shelfman")):
                    cursewords.SpeakText("I have been paused")
                    paused = True

                if (message == "unpause" and (username == NICK or "mod" in userBadges[1] or username == "the shelfman")):
                    cursewords.SpeakText("I am no longer paused")
                    paused = False
                    

                if (paused == False and connected):

                    if username.lower() == "streamlabs" and NICK == "theshelfman":
                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)

                    if username.lower == "danimilkman" and "danimilkman" not in usersInChat:
                        cursewords.SpeakText("You are a bitch, " + username)

                    if message == "adah go fuck yourself" or message == "go fuck yourself" or message == "adah, go fuck yourself" or message == "go fuck yourself adah" or message == "i don't like you" or message == "adah, i don't like you" or message == "i dont like you" or message == "adah, i dont like you" or message == "i don't like you adah" or message == "i don't like you adah" or message == "i don't like you, adah" or message == "i dont like you, adah":
                        if (cursewords.angerLevel == 1):
                            cursewords.SpeakText("That's not very nice of you, " + username)
                        if (cursewords.angerLevel == 2):
                            cursewords.SpeakText("Well fuck you too, " + username)
                        if (cursewords.angerLevel == 3):
                            cursewords.SpeakText(username + ", you motherfucker! I'll fuck you up!")
                    if message == "i like you adah":
                        if (cursewords.angerLevel == 1):
                            cursewords.SpeakText("I like you too " + username)
                        if (cursewords.angerLevel == 2):
                            cursewords.SpeakText("What's not too like, " + username)
                        if (cursewords.angerLevel == 3):
                            cursewords.SpeakText("Stop being such a kiss ass " + username)

                    if (message == "language"):
                        cursewords.SpeakText("watch your language! " + NICK)
                        
                    if ("who is the best streamer" in message):
                        cursewords.SpeakText("that would be " + NICK)
                    
                    if (message == "rip" or message == "rest in peace"):
                        cursewords.SpeakText("Let me guess. " + NICK + " died again?")

                    if ("adah happy birthday" in message and (username == NICK or "mod" in userBadges[1] or username == "the shelfman")):
                        birthdayUser = message.replace("adah happy birthday", "")
                        birthdayUser = birthdayUser.replace("@", "")
                        cursewords.SpeakText("Happy birthday    to you.    Happy birthday     to you.     Happy birthday dear " + birthdayUser + ".     Happy birthday   to you.")

                    if ("adah attack" in message and (username == NICK or "mod" in userBadges[1] or username == "the shelfman")):
                        userToAttack = message.replace("adah attack", "")
                        userToAttack = userToAttack.replace("@", "")
                        cursewords.SpeakText("You think you're cool, " + userToAttack + "? You're a pathetic troll. Find a different hobby. Goodbye")

                    if "quote" in message and "!quote" not in message and username == "streamlabs" and "successfully added" not in message:
                        messageWithOrigin = message.partition("[")
                        cursewords.SpeakText(messageWithOrigin[0])
                        
                    
                    if message == "karma":
                        cursewords.SpeakText("smells like karma to me, bitch!")
                            
                            
                    # ANGER CONTROL BY MODS
                    if message in triggerWords.angerControl and (
                            username == "jake_darb" or username == "the shelfman" or username == NICK or userMod or "mod" in
                            userBadges[1]):
                        cursewords.SpeakText("Anger mode changed to " + message)
                        cursewords.SetAngerMode(message)

                    if (message == "what time is it" or message == "what's your time"):
                        cursewords.SpeakText(
                            "Currently it is " + time.strftime("%I:%M", time.localtime()) + " for " + NICK)

                    if message == "rickroll" and NICK == "theshelfman":
                        cursewords.SpeakText("I'm sorry, the shelfman, but " + username + " made me do this")
                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=1)

                    sayBackwardTriggers = ["backwards", "say", "backwards?"]
                    countWordsInMesage = 0
                    listWordsInMessage = message.split()
                    for word in listWordsInMessage:
                        if word in sayBackwardTriggers:
                            countWordsInMesage += 1
                    if countWordsInMesage > 1 and ("backwards" in message or "backwards?" in message):
                        list = message.split()
                        newList = []

                        toDelete = ["backwards", "?", "backwards?", "say"]

                        for word in list:
                            if word not in toDelete:
                                newList.append(word)

                        wordsFlipped = []
                        for i in newList:
                            strLength = len(i)
                            slicedString = i[strLength::-1]
                            wordsFlipped.append(slicedString)

                        wordsFlipped = wordsFlipped[::-1]
                        cursewords.SpeakText(str(newList) + "said back words, is " + str(wordsFlipped))

                    greetings = ["hello adah", "hi adah", "heya adah", "hey adah", "hiya adah", "sup adah",
                                 "what's up adah", "whatsup adah", "whats up adah", "yo adah"]
                    if message in greetings:
                        cursewords.ChatRespond(username, "hello")


                    rockPaperScissors = ["adah rock", "adah paper", "adah scissors"]

                    if message in rockPaperScissors:
                        adahChoice = random.randint(0,2)
                        # url = 'http://adah.theshelfman.net/rpsPlayGame.php'
                        # myData = {'username': username, 'points': 1}
                        # x = requests.post(url, data=myData)


                        # if player has chosen rock
                        if message == rockPaperScissors[0]:
                            if adahChoice == 0:
                                cursewords.SpeakText("I also said rock, " + username + ", so we tied!")
                            elif adahChoice == 1:
                                cursewords.SpeakText("I said paper, " + username + ", so I won!")
                            else:
                                cursewords.SpeakText("I said scissors, " + username + ", so you won!")

                        # if player has chosen paper
                        elif message == rockPaperScissors[1]:
                            if adahChoice == 0:
                                cursewords.SpeakText("I said rock, " + username + ", so you won!")
                            elif adahChoice == 1:
                                cursewords.SpeakText("I also said paper, " + username + ", so we tied!")
                            else:
                                cursewords.SpeakText("I said scissors, " + username + ", so I won!")

                        # if player has chosen scissors
                        else:
                            if adahChoice == 0:
                                cursewords.SpeakText("I said rock, " + username + ", so I won!")
                            elif adahChoice == 1:
                                cursewords.SpeakText("I said paper, " + username + ", so you won!")
                            else:
                                cursewords.SpeakText("I also said scissors, " + username + ", so we tied!")



                    # BOOKY'S PERSONAL RESPONSES
                    if (username == "jake_darb"):
                        # check if message is equal to a string from the list of words
                        rdResponse = random.randint(0, 1)
                        if rdResponse == 0 and (
                                message != "i love you" and message != "i love you adah" and message != "i love you, adah"):
                            if message in triggerWords.chatWordsToActivate:
                                cursewords.ChatRespond(username, message)
                        else:
                            if message in triggerWords.chatWordsToActivate:
                                cursewords.BookyRespond(username, message)
                            
                    # EVERYONE ELSE'S RESPONSES
                    else:
                        if message in triggerWords.chatWordsToActivate and username.lower() != "streamlabs":
                            cursewords.ChatRespond(username, message)
        except:
            eula.insert("1.0", "There was an error, returning now...\n")
            threading.Timer(2.0, clearTextBox).start()
            return
    while restart == True:
        restartFalse()
        break


# thread2 = threading.Thread(target=checkMicInput)
# thread2.start()
def clearTextBox():
    eula.forget()
    eula.delete("1.0", "end")


def restartTrue():
    eula.insert("1.0", "Restarting now!\n")
    s.send(bytes("PRIVMSG #" + NICK + " : \r\n", "UTF-8"))
    restart = True
    threading.Timer(1.0, restartFalse).start()


def restartFalse():
    if (NICK == "" or PASS == ""):
        eula.delete("1.0", "end")
        eula.insert("1.0", "Nickname or Password has not been entered")
    else:
        nickName.delete('0', 'end')
        auth.delete('0', 'end')
        eula.insert("1.0", "Successfully restarted\n")

        # INVALID CAP COMMAND
        # s.send(bytes("CAP #theshelfman : REQ :twitch.tv/tags \r\n", "UTF-8"))
        s.send(bytes("CAP REQ :twitch.tv/tags \r\n", "UTF-8"))

        # s.send(":tmi.twitch.tv CAP * ACK :twitch.tv/tags")

        restart = False
        threading.Timer(300.0, restartTrue).start()
        thread3 = threading.Thread(target=checkMessages)
        thread3.start()
        # thread1 = threading.Thread(target=checkNames)
        # thread1.start()


def firstStart():
    try:
        global s
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
        s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
        s.send(bytes("JOIN #" + NICK + " \r\n", "UTF-8"))
        # s.send(bytes("PRIVMSG #" + NICK + " : \r\n", "UTF-8" + "hello"))
        # s.sendmsg("hello")
        restartFalse()



    except Exception as e:
        eula.insert("1.0", "Something went wrong, couldn't connect")


app.mainloop()
