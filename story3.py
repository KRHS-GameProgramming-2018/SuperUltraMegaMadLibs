from getInput import *

def playMadlibs():
    Person1 = getWord ("please enter a person's name: ")
    place1 = getWord ("plese enter a place: ")
    object1 = getWord ("please enter an object: ")
    
    output = ""
    output += "One day I was calling " + Person1 + "on the phone"
    output += Person1 + "said we should meet up at" + place1
    output += "when I got to" + place1 + ", " + Person1 + " was holding a(n) " + object1
    output += "We never spoke again"
    output += "THE END"
    output += "Congradulations you are a lonley bastard"
