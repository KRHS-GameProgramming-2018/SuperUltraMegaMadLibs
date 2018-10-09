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
    noun1 = getWord ("Please Enter a Noun: ")
    transport1 = getWord ("Please Enter a Mode of Transportation: ")
    breakout1 = getWord ("Please Enter an Escape Method: ")
    time1 = getWord ("Please Enter an Amount of Time [I.E. 1 year]: ")
    
    output = ""
    output += "One " + daytime1 + ", " + name1 + " was sneaking around. "
    output += "As a " + job1 + ", it was a part of " + name1 + "'s job description. "
    output += name1 + " had to be " + sneak1 + ", so they wore their " + color1 + " " + objects1 + ". "
    output += "Suddenly, " + name1 + " heard the sound of a wailing " + sound1 + ", so they hid inside of a " + object2 + ". "
    output += "When they got out, they were " + verb1 + " by " + name2 + ", who was a " + job2 + ". "
    output += name1 + " was subsequently put in " + noun1 + ", but he had a plan. "
    output += "The plan was to escape by " + transport1 + ", and the way " + name1 + " would get out to begin with would be by " + breakout1 + "."
    output += "When the breakout occured, the " + guards1 + " immediately started searching the " + noun1 + "."
    output += name1 + " was soon caught again, and would be stuck in " + noun1 + " for " + time1 + "."
  
    return output

