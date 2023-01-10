import os



# - Få sti til mappe/fil og et ord å søke etter.
# - Dersom oppgitt sti peker til en fil eller mappe så skal den fortsette, ellers skal du skrive en feilmelding til 
#   TextArea. <- Try/Except
# - Ved hjelp av rekursjon skal den skal gå gjennom alle mapper og filer og søke etter et spesifikt ord.
#   -> Modifiser mappe/fil-rekursjon?
# - Dersom du finner et match så skal du skrive ut sti til fil og linje orden befinner seg på.
# - Til slutt skal du skrive ut hvor mange mapper og filer du har søkt gjennom samt antall ganger ordet har
#   kommet frem i filene.


def main():
    # Prompt the user to enter a directory or a file
    path = input("Enter a directory or a file: ").strip()   
    word = input("Enter word to search for: ")
   
    try:
        searchFile(path, word)
    except:
        print("Directory or file does not exist")

def searchFile(path,word):
    print("Search start")
    #
    foldersFilesOccurences =[0,0,0]
    resultsDictionary = findWord(path,word, foldersFilesOccurences)
    print("Search ended")
    print(resultsDictionary)

def findWord(path, word, foldersFilesOccurences):
    if not os.path.isfile(path):   #Hvis inntastet verdi er mappe istedenfor fil
        foldersFilesOccurences[2]+=1 #Teller mappe
        lst = os.listdir(path) # All files and subdirectories
        for subdirectory in lst:
            findWord(path + "\\" + subdirectory, word, foldersFilesOccurences)
    else: # Base case - når det er snakk om en fil
        foldersFilesOccurences[1] += 1 #Teller fil
        for line in open(path).read().split("\n"): 
            if word in line:
                foldersFilesOccurences[0] += 1 #Teller treff på søkeord
                print(f"{path}:{line}")
  
    return {"Occurences":foldersFilesOccurences[0], "Files":foldersFilesOccurences[1], "Folders":foldersFilesOccurences[2]}



main() # Call the main function
