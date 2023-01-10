def main():

    firstWord, secondWord = str(input("Skriv inn ett ord: ")).lower()

    dictionaryOne = stringToDictionary(firstWord)
    dictionaryTwo = stringToDictionary(secondWord)

    if dictionaryOne==dictionaryTwo:
        print(f"'{firstWord}' og '{secondWord}' er anagrammer")
    else:
        print(f"'{firstWord}' og '{secondWord}' er ikke anagrammer")
        
def stringToDictionary(string):
    dictionary = {}
    #Går gjennom hver bokstav i ordet, teller opp på key eller legger til ny hvis den ikke allerede finnes
    for letter in string:
        if letter in dictionary:
            dictionary[letter] +=1
        elif letter not in dictionary:
            dictionary[letter] = 1
    return dictionary
    
if __name__ == '__main__':
      main()