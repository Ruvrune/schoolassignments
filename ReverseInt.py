from tkinter import * # Import tkinter

#Part 1
def reverseInteger(value):
    if value < 10: #Hvis det bare er ett siffer
        return str(value)
    else:
       return (reverseInteger(value%10) + reverseInteger(value//10)) #Finner bakerste siffer og jobber seg mot venstre

def main():
    number=int(input("Enter a positive number: "))
    print(f"Reverse of {number} is {reverseInteger(number)}")
    reverseNumber()

#Part 2
class reverseNumber():
    def __init__(self):
       
        window = Tk()
        window.title("Reverse number")
        #Sett inn frame:
        frame1 = Frame(window)
        frame1.pack()
        #Sett inn felt for entry, knapp og resultatfelt
        self.value = IntVar()
        self.resultatVar = StringVar()
        Entry(frame1, textvariable = self.value, justify = CENTER, borderwidth=2).grid(row = 1, column = 1)
        Button(frame1, text = "Reverse!", command = self.turnNumber).grid(row = 1, column = 3)
        Label(frame1, textvariable = self.resultatVar).grid(row = 3, column = 1)

        window.mainloop() # Eventloop

    def turnNumber(self):
        turnedNumber = self.reverseInteger(self.value.get())
        return self.resultatVar.set(turnedNumber)

    def reverseInteger(self,value):
        if value < 10: #Hvis det bare er ett siffer
            return str(value) #Legger til nummer i streng i reversert rekkefølge
        else:
            return (self.reverseInteger(value%10) + self.reverseInteger(value//10)) #Finner bakerste siffer og jobber seg mot venstre

#Kjører Part 1 og Part 2      
if __name__ == '__main__':
      main()