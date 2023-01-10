import os
from tkinter import * # Import tkinter

class findWordInFile():
    def __init__(self):
        window = Tk()
        window.title("Find word in files")
        #Sett inn frame:
        frame1 = Frame(window)
        frame1.pack()
        #Sett inn felt for location, word og søkeknapp
        self.location = StringVar(value="Directory or filename")
        self.word = StringVar(value="Enter word")
        #Legger inn søkefelt og søkeknapp (måtte .grid'e og .bind'e over egne linjer for at det skulle funke)
        self.inputLocation = Entry(frame1, textvariable = self.location, justify = CENTER,width=60, borderwidth=2)
        self.inputLocation.grid(row = 1, column = 1)
        #Bruker lambda for å passe inn argument til funksjonen
        self.inputLocation.bind("<FocusIn>",lambda event, arg=self.location : self.clearText(event, arg))
        self.searchWord = Entry(frame1, textvariable = self.word, justify = CENTER,width=40, borderwidth=2)
        self.searchWord.grid(row = 1, column = 2)
        self.searchWord.bind("<FocusIn>",lambda event, arg=self.word : self.clearText(event, arg))
        Button(frame1, text = "Search", command = self.searchFile).grid(row = 1, column = 3)
  
        #Plasserer tekstbox for søkeresultat
        frame2 = Frame(window)
        frame2.pack()
        #Legger til scrollbar
        scrollbar=Scrollbar(frame2)
        scrollbar.pack(side=RIGHT,fill=Y)
        #Plasserer listbox for tekst
        self.resultBox=Text(frame2, width = 100, height = 40, wrap = WORD, yscrollcommand=scrollbar.set)
        self.resultBox.pack()
        scrollbar.config( command = self.resultBox.yview)

        window.mainloop() # Eventloop

    def clearText(self,event, arg):
        arg.set("")

    def searchFile(self):
        self.resultBox.delete("0.0",END)
        path = self.location.get()
        word = self.word.get()
        foldersFilesOccurences = [0,0,0]
       
        self.resultBox.insert(END,"Search start.\n---------------------------------------------------\n")
        resultsDictionary = self.findWord(path,word, foldersFilesOccurences)
        try:
            if resultsDictionary["Occurences"]==0:
                self.resultBox.insert(END,f"'{word}' doesn't exist.")
            else:
                self.resultBox.insert(END,"\n---------------------------------------------------\nSearch end.\n")
                self.resultBox.insert(END, f"Searched {resultsDictionary['Folders']} folders and {resultsDictionary['Files']} files, found {resultsDictionary['Occurences']} occurences of '{word}'")
        except:
            self.resultBox.insert(END,"Directory or file does not exist")

    def findWord(self, path, word, foldersFilesOccurences):
        if not os.path.isfile(path):   #Hvis inntastet verdi er mappe istedenfor fil
            foldersFilesOccurences[2]+=1 #Teller mappe
            lst = os.listdir(path) # All files and subdirectories
            for subdirectory in lst:
                self.findWord(path + "\\" + subdirectory, word, foldersFilesOccurences)
        else: # Base case - når det er snakk om en fil
            foldersFilesOccurences[1] += 1 #Teller fil
            for line in open(path,errors="ignore").read().split("\n"): #Åpner fil, ser bort fra encoding-feil(trolig ikke relevant for oppgaven)
                if word in line:
                    foldersFilesOccurences[0] += 1 #Teller treff på søkeord
                    self.resultBox.insert(END, str(path)+": "+str(line)+"\n") #Kunne eventuelt kjørt ut til liste, men tar det heller direkte til tekstbox
                     
        return {"Occurences":foldersFilesOccurences[0], "Files":foldersFilesOccurences[1], "Folders":foldersFilesOccurences[2]}

findWordInFile()

