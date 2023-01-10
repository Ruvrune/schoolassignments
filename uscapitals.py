import os.path

def main():
    #Dette fordrer at fila ligger i rotmappa. Eventuell path kan legges til her
    if os.path.isfile("USCapitals.txt"):
        statesAndCapitals = loadFile()
        while True:
            findCapital(statesAndCapitals)
            while True:
                again = input(str("Check another state, y/n? ")).lower()
                if again not in ("yn"):
                    print("wrong character, try again")
                    continue 
                else:
                    break       
            if again == 'y':
                continue
            elif again == 'n':
                break 
    elif not os.path.isfile("USCapitals.txt"):
        print("File 'USCapitals.txt' not found.")
     
def findCapital(statesAndCapitals):
    while True:
        try:
            state = input(str("Enter state to show capital: ")).title() 
            city = statesAndCapitals[state]
            print(f"The capital of {state} is {city}")
            break
        
        except (NameError, KeyError):   #Fanger opp om bruker taster inn en verdi som ikke finnes i dictionary.
            print("Sure that's correct? State not found. Try again.")
            continue

def loadFile():

    filename = ("USCapitals.txt").strip()
    inputFile = open(filename, "r") # Åpner fil
    statesAndCapitals = {} # lager en tom dictionary
    for line in inputFile:
        key, value = line.split(",")
        statesAndCapitals[key] = value.strip() #strip for å fjerne newline etter by
    inputFile.close()
    return statesAndCapitals
            

if __name__ == '__main__':
      main()
