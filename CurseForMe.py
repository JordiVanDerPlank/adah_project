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
app.master.title("ADAH v1.4")
app.configure(bg="#18181b")

# STOP PROGRAM WHEN RED CROSS IS PRESSED
gui.protocol("WM_DELETE_WINDOW", gui.destroy)

scroll = Scrollbar(gui)
scroll.pack(side=RIGHT, fill=Y)

# TEXT SHOWN ON SCREEN
eula = Text(gui, wrap=NONE, yscrollcommand=scroll.set, bg="#18181b", foreground="white")

global connected


def showAdah():
    if btnText.get() == "Disconnect":
        global connected
        connected = False
        btnOAuth.pack(side='right', padx="5")
        nickNameLabelDir.pack(side='left')
        nickName.pack(side='left')
        authLabelDir.pack(side='left')
        auth.pack(side='left')

        eula.delete("1.0", "end")
        eula.insert("1.0", "Successfully disconnected!")
        btnText.set("Connect")
        global s
        s = socket.socket()
        s.close()
    #         # print("I am here")
    # restartFalse()

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

                usernamesplit = parts[1].split("!")
                username = usernamesplit[0]
                
                if ";subscriber=" in username:
                    message = parts[3][:len(parts[2])]
                    usernamesplit = parts[2].split("!")
                    username = usernamesplit[0]

                if (username not in usersInChat and "tmi.twitch.tv" not in username and username != NICK):
                    cursewords.SpeakText("Hello " + username + ", welcome to the stream!")
                    print(username)
                    usersInChat.append(username)
                
                # seperate all tag information
                badgeInfoSplit = line.split(";")
                for i in badgeInfoSplit:
                    #                     # print ("badgeInfo = " + i + "\n")
                    if "mod=1" in i:
                        userMod = True
                    else:
                        userMod = False

                badgeInfo = badgeInfoSplit[0].split("=")
                # for j in badgeInfo:
                #                 #     print ("user badge info = " + j)
                #                 # print ("badge info length = " + str(len(badgeInfo)))

                if len(badgeInfo) >= 2:
                    if "subscriber" in badgeInfo[1]:
                        subscribed = True

                if len(badgeInfoSplit) >= 2:
                    userBadges = badgeInfoSplit[1].split("=")
                    # for i in userBadges:
                #                     # print ("userbadges = " + i)

                #                 # print ("user badge info = " + badgeInfo[1])
                #                 # print ("user badge info = " + badgeInfo[0])
                #                 # print ("badgeInfo = " + badgeInfo)

                #                 # print(username + ": " + message + "badgeinfo: " + badgeInfo)
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
                    btnText.set("Disconnect")

                message = message.lower()

                global paused, cooldownOn

                if (message == "pause" and (username == NICK or "mod" in userBadges[1])):
                    cursewords.SpeakText("I have been paused")
                    paused = True

                if (message == "unpause" and (username == NICK or "mod" in userBadges[1])):
                    cursewords.SpeakText("I am no longer paused")
                    paused = False

                # if subscribed:
                # cursewords.SpeakText(username + " is subscribed to the channel")
                # print(username + " is subscribed to the channel")

                ##PREDEFINED RESPONSES
                # if message == "hey adah" or message == "hi adah" or message == "hello adah":
                #    cursewords.SpeakText("Go fuck yourself" + username)

                if (paused == False and connected):

                    if username.lower() == "streamlabs" and NICK == "theshelfman":
                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)

                    if username.lower == "danimilkman":
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

                    # ANGER CONTROL BY MODS
                    if message in triggerWords.angerControl and (
                            username == "bootlessbooky" or username == "theshelfman" or username == NICK or userMod or "mod" in
                            userBadges[1]):
                        cursewords.SpeakText("Anger mode changed to " + message)
                        cursewords.SetAngerMode(message)

                    if (message == "what time is it" or message == "what's your time"):
                        cursewords.SpeakText(
                            "Currently it is " + time.strftime("%I:%M", time.localtime()) + " for " + NICK)

                    if message == "rickroll" and NICK == "theshelfman":
                        cursewords.SpeakText("I'm sorry, theshelfman, but " + username + " made me do this")
                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=1)

                    sayBackwardTriggers = ["backwards", "say", "backwards?"]
                    countWordsInMesage = 0
                    listWordsInMessage = message.split()
                    for word in listWordsInMessage:
                        #                         # print (word)
                        if word in sayBackwardTriggers:
                            #                             # print("count: " + str(countWordsInMesage))
                            countWordsInMesage += 1
                    if countWordsInMesage > 1 and ("backwards" in message or "backwards?" in message):
                        list = message.split()
                        newList = []

                        toDelete = ["backwards", "?", "backwards?", "say"]

                        for word in list:
                            #                             # print ("current word: " + word)
                            if word not in toDelete:
                                newList.append(word)

                        wordsFlipped = []
                        # wordToFlip = newList[0]
                        # strLength = len(wordToFlip)
                        # slicedString = wordToFlip[strLength::-1]
                        # cursewords.SpeakText(wordToFlip + "said back words, is " + slicedString)
                        for i in newList:
                            strLength = len(i)
                            slicedString = i[strLength::-1]
                            wordsFlipped.append(slicedString)

                            # print(wordsFlipped)
                        wordsFlipped = wordsFlipped[::-1]
                        cursewords.SpeakText(str(newList) + "said back words, is " + str(wordsFlipped))

                    greetings = ["hello adah", "hi adah", "heya adah", "hey adah", "hiya adah", "sup adah",
                                 "what's up adah", "whatsup adah", "whats up adah", "yo adah"]
                    if message in greetings and cooldownOn == False:
                        # cooldownOn = True
                        # thread3 = threading.Thread(target=turnoffCooldown)
                        # thread3 = threading.Timer(60, turnoffCooldown)
                        # thread3.start()
                        cursewords.ChatRespond(username, "hello")
                    else:
                        # for each trigger word/sentence
                        for word in greetings:
                            # does the trigger word/sentence exist in my message
                            if (word in message and cooldownOn == False):
                                # if the found word is shorter than 5 characters
                                if (len(word) < 5):
                                    # divide the message in different words and check if one of the words is the same as my word
                                    wordsInMessage = message.split()
                                    for currentWord in wordsInMessage:
                                        if (currentWord == word):
                                            cooldownOn = True
                                            thread3 = threading.Thread(target=turnoffCooldown)
                                            thread3.start()
                                            cursewords.ChatRespond(username, "hello")
                                            break
                                        else:
                                            continue
                                else:
                                    thread3 = threading.Thread(target=turnoffCooldown)
                                    thread3.start()
                                    cooldownOn = True
                                    cursewords.ChatRespond(username, "hello")

                    # BOOKY'S PERSONAL RESPONSES
                    if (username == "bootlessbooky"):
                        # check if message is equal to a string from the list of words
                        rdResponse = random.randint(0, 1)
                        if rdResponse == 0 and (
                                message != "i love you" and message != "i love you adah" and message != "i love you, adah"):
                            if message in triggerWords.chatWordsToActivate:
                                cursewords.ChatRespond(username, message)
                            else:
                                wordsInMessage = message.split()
                                for currentWord in wordsInMessage:
                                    if (currentWord == "rickroll" and NICK == "theshelfman"):
                                        cursewords.SpeakText(
                                            "I'm sorry, theshelfman, but " + username + " made me do this")
                                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=1)
                                        break
                                # for each trigger word/sentence
                                for word in triggerWords.chatWordsToActivate:
                                    # does the trigger word/sentence exist in my message
                                    if (word in message):
                                        # if the found word is shorter than 5 characters
                                        if (len(word) < 5):
                                            # divide the message in different words and check if one of the words is the same as my word
                                            wordsInMessage = message.split()
                                            for currentWord in wordsInMessage:
                                                if (currentWord == word):
                                                    cursewords.ChatRespond(username, word)
                                                    break
                                                else:
                                                    continue
                                        else:
                                            cursewords.ChatRespond(username, word)
                        else:
                            if message in triggerWords.chatWordsToActivate:
                                cursewords.BookyRespond(username, message)
                            else:
                                wordsInMessage = message.split()
                                for currentWord in wordsInMessage:
                                    if (currentWord == "rickroll" and NICK == "theshelfman"):
                                        cursewords.SpeakText(
                                            "I'm sorry, theshelfman, but " + username + " made me do this")
                                        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=1)
                                        break
                                # for each trigger word/sentence
                                for word in triggerWords.chatWordsToActivate:
                                    # does the trigger word/sentence exist in my message
                                    if (word in message):
                                        # if the found word is shorter than 5 characters
                                        if (len(word) < 5):
                                            # divide the message in different words and check if one of the words is the same as my word
                                            wordsInMessage = message.split()
                                            for currentWord in wordsInMessage:
                                                if (currentWord == word):
                                                    cursewords.BookyRespond(username, word)
                                                    break
                                                elif (currentWord == "rickroll"):
                                                    cursewords.SpeakText(
                                                        "I'm sorry, theshelfman, but " + username + " made me do this")
                                                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ',
                                                                    new=1)
                                                    break
                                                else:
                                                    continue
                                        else:
                                            cursewords.BookyRespond(username, word)

                    # EVERYONE ELSE'S RESPONSES
                    else:
                        if message in triggerWords.chatWordsToActivate and username.lower() != "streamlabs":
                            cursewords.ChatRespond(username, message)
                        # else:
                        #     if username.lower() != "streamlabs":
                        #         wordsInMessage = message.split()
                        #         for currentWord in wordsInMessage:
                        #             if (currentWord == "rickroll"):
                        #                 cursewords.SpeakText("I'm sorry, theshelfman, but " + username + " made me do this")
                        #                 webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=1)
                        #                 break
                        #         # for each trigger word/sentence
                        #         for word in triggerWords.chatWordsToActivate:
                        #             # does the trigger word/sentence exist in my message
                        #             if (word in message):
                        #                 # if the found word is shorter than 5 characters
                        #                 if (len(word) < 5):
                        #                     # divide the message in different words and check if one of the words is the same as my word
                        #                     wordsInMessage = message.split()
                        #                     for currentWord in wordsInMessage:
                        #                         if (currentWord == word):
                        #                             cursewords.ChatRespond(username, word)
                        #                             break
                        #                         else:
                        #                             continue
                        #                 else:
                        #                     cursewords.ChatRespond(username, word)
        except:
            # print ("There was an error, returning now...")
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
    # print ("Restarting now!")
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
        # print("something went wrong, couldn't connect")
        eula.insert("1.0", "Something went wrong, couldn't connect")


app.mainloop()
