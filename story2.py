from getInput import *

def playMadlibs():
    daytime1 = getWord ("Please Enter a Time of Day: ")
    name1 = getWord ("Please Enter a Name: ")
    job1 = getWord ("Please Enter a Job: ")
    sneak1 = getWord ("Please Enter an Adjective: ")
    color1 = getWord ("Please Enter a Color: ")
    objects1 = getWord ("Please Enter a Plural Noun: ")
    sound1 = getWord ("Please Enter a Sound: ")
    object2 = getWord ("Please Enter a Noun: ")
    verb1 = getWord ("Please Enter a Past Tense Verb: ")
    name2 = getWord ("Please Enter a Name: ")
    job2 = getWord ("Please Enter a Job: ")
    output = ""
    output += "One " + daytime1 + ", " + name1 + " was sneaking around. "
    output += "As a " + job1 + ", it was a part of " + name1 + "'s job description. "
    output += name1 + " had to be " + sneak1 + ", so they wore their " + color1 + " " + objects1 + ". "
    output += "Suddenly, " + name1 + " heard the sound of a wailing " + sound1 + ", so they hid inside of a " + object2 + ". "
    output += "When they got out, they were " + verb1 + " by " + name2 + ", who was a " + job2 + "."
  
  
    return output

