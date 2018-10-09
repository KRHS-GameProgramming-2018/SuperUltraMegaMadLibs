def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True  
        elif (response == "2"
              or response == "Two"):
              response = "2"
              goodInput = True
        elif (response == "3"
              or response == "Three"):
              response = "3"
              goodInput = True
        elif (response == "4"
              or response == "Four"):
              response = "4"
              goodInput = True
        else:
            print "No, not that one!"
    return response
    
def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Do You kIss YouR mOthEr WitH tHat MouTh ?!?!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
        
            
    return word

def isSwear(word):
    swearList = ["piss",
                "fortnite",
                 "Nigger",
                 "nigger",
                 "shit",
                 "bitch",
                 "fuck",
                 "fuk",
                 "bloody wanka",
                 "faggot",
                 "ass",
                 "dab"
                 "bitch nigga'",
                 "assbag",
                 "arse",
                 "arsehole",
                 "ass jabber",
                 "dick",
                 "Dick",
                 "Dicks",]
    if word in swearList:
        return True
    else:
        return False
