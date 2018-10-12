from getInput import *

def playMadlibs():
    Person1 = getWord ("please enter a person's name: ")
    place1 = getWord ("plese enter a place: ")
    object1 = getWord ("please enter an object: ")
    song1 = getWord ("please enter a song lyric")
    output = ""
    output += "One day I was calling " + Person1 + " on the phone. "
    output += Person1 + " said we should meet up at " + place1 + "."
    output += " when I got to " + place1 + ", " + Person1 + " was holding a(n) " + object1 + "."
    output += Person1 + " Invited a friend that i was not aware of."
    output += " The random friend was dancing while singing " + song1 + "."
    
    
    return output
