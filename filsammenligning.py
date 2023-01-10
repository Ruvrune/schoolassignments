
def main():
    #Hent inn sett fra brukerangitte filer
    setOne = createListFromFile()
    setTwo = createListFromFile()

    print(f"Det er tilsammen {len(setOne)+len(setTwo)} unike ord i filene\n")
    #Kunne skrevet ut set'ene direkte, men ville ha uten {}-form 
    print(f"Dette er alle unike ord fra begge filer: ")
    printResults(setOne.union(setTwo))
    print(f"Disse ordene har begge listene til felles:")
    printResults(setOne.intersection(setTwo))
    print(f"Disse ordene er i fil 1, men ikke i fil 2: ")
    printResults(setOne.difference(setTwo))
    print(f"Disse ordene er i fil 2, men ikke i fil 1: ")
    printResults(setTwo.difference(setOne))
    print(f"Disse ordene er i enten første eller andre fil, men ikke i begge:")
    printResults(setOne.symmetric_difference(setTwo))
    
#Bruker funksjonene fra count occurence of words-oppgaven. Som nevnt i oppgaveteksten.
# Men modifisert til å benytte set istedenfor Dictionaries.
def processLine(line, wordSet): 
    line = replacePunctuation(line) # Replace punctuation with space
    words = line.split() # Get words from each line
    for word in words:
        wordSet.add(word)

# Replace punctuation in the line with space
def replacePunctuation(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=~<>?/,.;:!{}[]|'\"":
            line = line.replace(ch, " ")

    return line

def createListFromFile():
    while True:
        try:
            filename = input("Enter a filename: ").strip()
            inputFile = open(filename, "r") # Åpner filen
            wordSet = set() # lager et tomt sett
            for line in inputFile:
                processLine(line.lower(), wordSet)
            inputFile.close()
            return wordSet
            
        except FileNotFoundError:
            print("File doesn't exist, try again.")
            continue
def printResults(setComparison):
    #skriv ut resultat, hvis set-sammenligningen inneholder noe
    if len(setComparison)>0:
        for word in setComparison:
            print(word, end=" ")
        print("\n")
    else:
        print("Ingen ord samsvarer med sammenligningen\n")

if __name__ == '__main__':
      main()
