# Over all quit good, but you don't have any custom getters which is one of the major parts of this project. If you can write a custom getter we can up the grade significantly.
# 145/200 - P
from screens import *
from getInput import *
import story1
import story2
import story3

print showSplash()
raw_input("Press Enter to Start")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        go = False
        print "Goodbye and thanks for playing"
    elif response == "1":
        print story1.playMadlibs()
    elif response == "2":
        print story2.playMadlibs()
    elif response == "3":
        print story3.playMadlibs()
        raw_input("Press Enter to Continue")        #Sponer - Why is this the only story to get this message?
    elif response == "4":
        print showCredits()
        response = getMenuInput()
    elif response == "5":
        print showIndy()
        response = getMenuInput()
    else:
        print "OMG Got invalid menu option!!!"

