from getInput import *

def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a plural animal name: ")
    shoes1 = getWord("Enter a type of shoe: ")
    things1 = getWord("Enter a plural object: ")
    output = ""
    output += "One day I was walking with my friend, " + friend1
    output += ", when suddenly " + friend1
    output += " said that they saw " + numAnimals + " " + animals1
    output += ". We snuck up on them wearing our " + shoes1
    output += ", and took some great pictures with our " + things1
    output += ". Then the " + animals1 + " ran off, and we continued our walk."
    
    
    
    return output
