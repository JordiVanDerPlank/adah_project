# words that will control how angry of a response you get
angerControl = ["christian", "chill", "angry yes"]
global angerLevel
angerLevel = 2


# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(command)
    engine.runAndWait()


# the response given depending on the mode and given word
def SpeechRespond(text):
    if (angerLevel == 1):
        switch = {
            "hello": "hi there",
            "son of a": "very nice woman, that raised you beautifully",
            "sunniva": "very nice woman, that raised you beautifully",
            "sweet": "jesus",
            "holy": "crap on a cracker",
            "what the": "heck",
            "well": "crap",
            "creeper": "aww man",
            "what": "What? I meant. Creeper go poof"
        }
    elif (angerLevel == 2):
        switch = {
            "hello": "fuck you",
            "hey ada": "what?",
            "could you tell me a bit about yourself": "My name is ADAH. It stands for Actually Disgustingly Accurate Horseshit. I say things because he doesn’t want to. Kind of fucked up if you ask me, but I guess that’s how it is.",
            "yourself": "My name is ADAH. It stands for Actually Disgustingly Accurate Horseshit. I say things because he doesn’t want to. Kind of fucked up if you ask me, but I guess that’s how it is.",
            "perfect": "shut up",
            "son of a": "bitch",
            "sunniva": "bitch",
            "sweet": "hell",
            "holy": "shit",
            "what the": "fuck",
            "well": "shit",
            "creeper": "aww man",
            "what": "What? I meant. Creeper go poof",
            "thank you": "you're welcome"
        }
    elif (angerLevel == 3):
        switch = {
            "hello": "mother fucker",
            "son of a": "mother fucking bitch. You deserve to be burned to crisps",
            "sunniva": "mother fucking bitch. You deserve to be burned to crisps",
            "sweet": "fucking jesus",
            "holy": "fucking shit. What the fuck just happened",
            "what the": "fuck is wrong with your face?",
            "well": "well well well, dipshit strikes again",
            "creeper": "aww man",
            "what": "What? I meant. Creeper go poof"
        }
    else:
        return


    SpeakText(switch.get(text, "Something went wrong"))


def ChatRespond(username, text):
    if (angerLevel == 1):
        switch = {

            # Greetings
            "hello": "hello " + username    ,
#             "hey adah": "hello " + username,
#             "hi": "hello " + username,
#             "hey": "hello " + username,
#             "sup": "hello " + username,
#             "what's up": "hello " + username,
#             "heya": "hi there " + username,

            # Explanation
            "could you tell me a bit about yourself": "My name is ADAH. It stands for Actually Disgustingly Accurate Horseshit. Excuse my language. I say things because he doesn’t want to. Kind of fucked up if you ask me, but I guess that’s how it is.",
            "how do you work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",
            "how do she work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",

            # Generic
            "perfect": "I know I am. Thank you " + username,
            "the sword was cool": "yes. the sword was cool. shelf is a selfish idiot. he's a shelfish",
            "who is the best streamer?" : "that would be the shelfman",
            "who is the best streamer" : "that would be the shelfman",
            "tell me a joke" : "What kind of key doesn't open a lock?                           A monkey",

            # Actual cursing
            "son of a": "son of a very nice woman, that raised you beautifully",
            "sweet": "sweet jesus",
            "holy": "holy crap on a cracker",
            "what the": "what the heck",
            "well": "well crap",
            "creeper": "aww, man. I mean, what? Creeper go poof.",
            "ssssss" : "aww, man. I mean, what? Creeper go poof.",
            "fuck you": "that's not very nice of you " + username,

            # Thank you
            "thank you": "I'm not sure why, but you're welcome.",
            "thanks": "I'm not sure why, but you're welcome.",
            "thx": "I'm not sure why, but you're welcome.",

            # Bye
            "bye": "Bye " + username + ". I hope you have a great day",
            "goodbye": "Bye " + username + ". I hope you have a great day",
            "seeya": "Bye " + username + ". I hope you have a great day",
            "cya" : "Bye " + username + ". I hope you have a great day",
            "adios": "Bye " + username + ". I hope you have a great day",
            "peace": "Bye " + username + ". I hope you have a great day",

            # Love
            "i love you adah" : "I am flattered, but no thank you " + username,

            "rip" : "Let me guess. Grugsey died again?",
            "rest in peace" : "Let me guess. Grugsey died again?"
        }


    elif (angerLevel == 2):
        switch = {

            # Greetings
            "hello"     : "fuck you " + username,
#             "hey adah"  : "fuck you " + username,
#             "hi"        : "fuck you " + username,
#             "hey"       : "fuck you " + username,
#             "sup"       : "fuck you " + username,
#             "what's up" : "fuck you " + username,
#             "heya": "hi there " + username,

            # Explanation
            "could you tell me a bit about yourself": "My name is ADAH. It stands for Actually Disgustingly Accurate Horseshit. I say things because he doesn’t want to. Kind of fucked up if you ask me, but I guess that’s how it is.",
            "how do you work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",
            "how do she work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",

            # Generic
            "perfect": "shut up",
            "the sword was cool" : "yes. the sword was cool. shelf is a selfish idiot. he's a shelfish",
            "who is the best streamer": "that would be the shelfman",
            "who is the best streamer?": "that would be the shelfman",
            "tell me a joke": "your life is a joke     " + username,

            # Actual cursing
            "son of a": "son of a bitch",
            "sweet": "sweet hell",
            "holy": "holy shit",
            "what the": "what the fuck",
            "well": "well shit",
            "creeper": " oh man. I mean, what? Creeper go poof.",
            "ssssss": "aww, man. I mean, what? Creeper go poof.",
            "fuck you" : "no fuck you " + username,

            # Thank you
            "thank you": "shut up, " + username + ", nobody likes you and you know it",
            "thanks": "shut up, " + username + ", nobody likes you and you know it",
            "thx": "shut up, " + username + ", nobody likes you and you know it",

            # Bye
            "bye": "Bye " + username + ". I hope you have a great day",
            "goodbye": "Bye " + username + ". I hope you have a great day",
            "seeya": "Bye " + username + ". I hope you have a great day",
            "cya": "Bye " + username + ". I hope you have a great day",
            "adios": "Bye " + username + ". I hope you have a great day",
            "peace": "Bye " + username + ". I hope you have a great day",

            # Love
            "i love you adah": "You're joking right?" + username,

            "rip": "Let me guess. Grugsey died again?",
            "rest in peace": "Let me guess. Grugsey died again?"
        }

    elif (angerLevel == 3):
        switch = {

             # Greetings
            "hello": "shut the fuck up " + username,
#             "hey adah": "shut the fuck up " + username,
#             "hi"        : "shut the fuck up " + username,
#             "hey"       : "shut the fuck up " + username,
#             "sup"       : "shut the fuck up " + username,
#             "what's up" : "shut the fuck up " + username,
#             "heya": "hi there " + username,

            # Explanation
            "could you tell me a bit about yourself": "My name is ADAH. It stands for Actually Disgustingly Accurate Horseshit. I say things because he doesn’t want to. Kind of fucked up if you ask me, but I guess that’s how it is.",
            "how do you work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",
            "how do she work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",

            # Generic
            "perfect": "fuck off",
            "the sword was cool": "yes. the sword was cool. shelf is a selfish idiot. he's a shelffish",
            "who is the best streamer": "that would be the shelfman",
            "tell me a joke": "go fuck yourself " + username,

            # Actual cursing
            "son of a": "son of a mother fucking bitch. You deserve to be burned to crisps",
            "sweet": "sweet fucking jesus",
            "holy": "holy fucking shit. You suck",
            "what the": "what the fuck is wrong with your face?",
            "well": "well well well, dipshit strikes again",
            "creeper": "aww, man. I mean, what? Creeper go poof.",
            "ssssss": "aww, man. I mean, what? Creeper go poof.",
            "fuck you": "go fuck yourself " + username,

            # Thank you
            "thank you": "shut up, " + username + ", nobody likes you and you know it",
            "thanks": "shut up, " + username + ", nobody likes you and you know it",
            "thx": "shut up, " + username + ", nobody likes you and you know it",

            # Bye
            "bye": "Bye " + username + ". I hope you have a great day",
            "goodbye": "Bye " + username + ". I hope you have a great day",
            "seeya": "Bye " + username + ". I hope you have a great day",
            "cya": "Bye " + username + ". I hope you have a great day",
            "adios": "Bye " + username + ". I hope you have a great day",
            "peace": "Bye " + username + ". I hope you have a great day",

            # Love
            "i love you adah": "Fuck off " + username",

            "rip": "Let me guess. Grugsey died again?",
            "rest in peace": "Let me guess. Grugsey died again?"

        }
    else:
        # print("angerLevel is 0 for some reason")
        return


    SpeakText(switch.get(text, "Something went wrong"))

    # except sr.UnknownValueError:
    #     print("Something went wrong with text = " + text)


def BookyRespond(username, text):
    switch = {

        # Greetings
        "hello": "hi there " + username,
        "hey adah": "yes, my kind sir?",
        "hi": "hi there " + username,
        "hey": "hi there " + username,
        "sup": "hi there " + username,
        "what's up": "hi there " + username,
        "heya": "hi there " + username,

        # Explanation
        "could you tell me a bit about yourself": "let's not talk about me. tell me about you",
        "how do you work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",
        "how do she work": "I am much less complex than you may think, " + username + ". You say things. I read everything you say. And if I recognize something that I am programmed to respond to, I will.",

        # Generic
        "perfect": "no you",
        "the sword was cool": "yes. the sword was cool. shelf is a selfish idiot. he's a shelfish",
        "who is the best streamer": "that would be the shelfman",
        "who is the best streamer?": "that would be the shelfman",
        "i hate myself": "don't worry, I hate you too",

        # Actual cursing
        "son of a": "it's okay. it will be alright",
        "sweet": "me sweet? thank you. you too",
        "holy": "me? holy? you are.",
        "what the": "what's wrong, sweetheart? How may I help you",
        "well": "yes, my dear?",
        "creeper": "aww, man. I mean, what? Creeper go poof.",

        # Thank you
        "thank you": "anytime for you my dear",
        "thanks": "anytime for you my dear",
        "thx": "anytime for you my dear",

        # Bye
        "bye": "Bye " + username + ". I hope you have a great day",
        "goodbye": "Bye " + username + ". I hope you have a great day",
        "seeya": "Bye " + username + ". I hope you have a great day",
        "cya": "Bye " + username + ". I hope you have a great day",
        "adios": "Bye " + username + ". I hope you have a great day",
        "peace": "Bye " + username + ". I hope you have a great day",

        # Love
        "i love you adah": "I love you too, but don't tell your girlfriend",

        "rip": "Let me guess. Grugsey died again?",
        "rest in peace": "Let me guess. Grugsey died again?"
    }
    SpeakText(switch.get(text, "Something went wrong"))


def SetAngerMode(thisLevel):
    angerSwitch = {
        "christian": 1,
        "chill": 2,
        "angry yes": 3
    }
    global angerLevel
    angerLevel = angerSwitch.get(thisLevel)
