import os.path
from datetime import datetime
import time

def main():

    filename = "box_a.txt"
    filename2 = "box_b.txt"
    
    listSpeeders(filename, filename2, 60, 5)

def fileToDictionary(filename):
    if not os.path.isfile(filename):
        #Returner tom dictionary om filen ikke finnes
        return {}
    inputFile = open(filename, "r") # Åpner fil
    box = {} # lager en tom dictionary
    for line in inputFile:
        key, value = line.split(",")
        box[key] = value.strip() #fjerner newline
    inputFile.close()
    return box
            
def listSpeeders(filename_a, filename_b, speed_limit, distance):
    boxA = fileToDictionary(filename_a)
    boxB = fileToDictionary(filename_b)
    speedersDictionary = {}
    
    for key in boxA:
        if key in boxB: #Returnerer verdi kun for biler som har passert begge boksene
           # print(f"box A: {key} {boxA[key]} box B: {key} {boxB[key]}")
            speed = float(convertTimeToSpeed(boxA[key],boxB[key],distance))
          #  print(F"hastigheten til {key} er {speed}")
            #Tar ut biler som er over marginen på 5%
            if margine(speed,speed_limit):
                speedersDictionary[key] = (float(speed),boxA[key]) #Putter reg nummer med hastighet og tidspunkt inn i dictionary

    return speedersDictionary

def convertTimeToSpeed(timeStartString, timeEndString, distance):
    #Start-tid
    timeStart = datetime.strptime(timeStartString, '%Y-%m-%d %H:%M:%S')
    timeStartTuple = timeStart.timetuple()
    timeStampStart = time.mktime(timeStartTuple)
    #Slutt-tid
    timeEnd = datetime.strptime(timeEndString, '%Y-%m-%d %H:%M:%S')
    timeTupleEnd = timeEnd.timetuple()
    timeStampEnd = time.mktime(timeTupleEnd)
    #Tidsdifferanse og konvertering til km/h
    timeDelta = (timeStampEnd - timeStampStart)
    hours = timeDelta/3600
    speed = "%.3f" % (distance/hours) #Finner km/t med tre desimaler
    return speed
#Sjekk om hastigheten er over eller under marginen på 5%
def margine(speed, speedLimit):
    if speed > speedLimit*1.05:
        return True
    else:
        return False
# Call the main function.
#if __name__ == '__main__':
  
  #    main()
