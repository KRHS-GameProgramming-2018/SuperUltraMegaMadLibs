from getInput import *

def playMadlibs():
    daytime1 = getWord ("Please Enter a Time of Day: ")
    name1 = getWord ("Please Enter a Name: ")
    job1 = getWord ("Please Enter a Job: ")
    sneak1 = getWord ("Please Enter an Adjective: ")
    color1 = getWord ("Please Enter a Color: ")
    objects1 = getWord ("Please Enter a Plural Noun: ")
    ouput += ""
    output += "One " + daytime1 + ", " + name1 + "was sneaking around."
    output += "As a " + job1 + ", it was a part of " + name1 +"'s job description."
    output += name1 + "had to be " + sneak1 + ", so they wore their " + color1 + " " + objects1 + "."
  
  
    return output

