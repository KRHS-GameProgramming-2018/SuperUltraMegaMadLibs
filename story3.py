from getInput import *

def playMadlibs():
    Person1 = getWord ("please enter a person's name: ")
    place1 = getWord ("plese enter a non egsistant place: ")
    object1 = getWord ("please enter an object: ")
    song1 = getWord ("please enter a song lyric")
    person2 = getWord ("please enter a song artistr")
    Place2 = getWord ("please enter another place")
    action1 = getWord ("please enter an action ending in ING ")
    game1 = getWord ("please enter a video game title")

    #You should have a custom getter

    output = ""
    output += "One day I was calling " + Person1 + " on the phone. "
    output += Person1 + " said we should meet up at " + place1 + "."
    output += " When I got to " + place1 + ", " + Person1 + " was holding a(n) " + object1 + ". "
    output += Person1 + " Invited a friend that i was not aware of."
    output += " The random friend was dancing while singing " + song1 + "."
    output += " I suddenly heard a breakout of cheering. when I turned around there was a concert for " + person2 + "."
    output +=  Person1 + " said that they had no idea that there was a concert in " + place1 + "."
    output += " We desided to go to a different place, this time I was picking where."
    output += " When we arived at " + Place2 + " There was a homless man" + action1 + "."
    output += " I suddenly heard a breakout of cheering. when i turneed around there was a consert for " + person2 
    output +=  Person1 + "said they had no idea that there was a concert in " + place1
    output += " we desided to go to a different place, this time i was picking where. "
    output += " when we arived at " + Place2 + " There was a homless man" + action1 + "."
    output += " At the end I just decided to go home and play " + game1 + "."
    

    return output
