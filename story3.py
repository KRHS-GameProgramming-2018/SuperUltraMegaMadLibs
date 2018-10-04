from getInput import *

def playMadlibs():
    Person1 = getWord ("please enter a person's name: ")
    place1 = getWord ("plese enter a place: ")
    output = ""
    output += "One day I was calling " + Person1 + "on the phone"
    output += Person1 + "said we should meet up at" + place1

