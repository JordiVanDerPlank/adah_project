import base64
import requests
from http.client import HTTPConnection
import cursewords

def printData(username, number):
    # print("hi you've just fallen for my trapcard")
    import requests
    page = requests.get("http://adah.theshelfman.net/quote.html")
    webpage = str((page.text.encode('utf8')))
    # firstPart = str(webpage).strip().split('~')
    print(webpage)

    #Get all the relevant content from the webpage
    content = webpage.split("~")

    #Get all the quotes from the webpage
    userAndQuotes = content[1].split("-")
    print("userquotes " + str(userAndQuotes))
    # print("content: " + content[1])
    for userAndQuote in userAndQuotes:
        # print("userAndQuote: " + userAndQuote)
        if ("!" not in userAndQuote):
            continue
        user = userAndQuote.split("!")[0]
        print(user)
        quoteNumber = userAndQuote.split()[1].split(":")[0].replace("quote ", "")
        if user == username:
            print("a")
            #do the thing
            if quoteNumber == number:
                thisMessage = ""
                print("b")
                try:
                    print("c")
                    print("rest = " + str(userAndQuote.split("!")))
                    print("quote & message = " + str(userAndQuote.split("!")[1].split(":")))
                    # thisMessage = userAndQuote.split("!")[1].split(":")[1]
                    thisMessage = userAndQuote.split("!")[1].split(":")[1].replace("\\r\\n", "")
                    print(thisMessage)
                    cursewords.SpeakText(thisMessage)
                except:
                    print("d")
                    thisMessage = userAndQuote.split()[1].split(":")[1]
                    cursewords.SpeakText(thisMessage)



        else:
            continue


    # cursewords.SpeakText(quote)
