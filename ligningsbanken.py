import random
#Virker, men ser ikke veldig stilig ut?
def eq2text(integerList, pos=0, eqString=""):
    value = str(integerList[pos])
    if pos == 3:    #Slutten av lista - base case
        return eqString+positiveOrNegative(value)
    if pos==0 or pos==2:
        if value == "1":
            eqString += "x"
            return eq2text(integerList, pos+1,eqString)
        elif value == "-1":
            eqString += "-x"
            return eq2text(integerList, pos+1,eqString)
        else:
            eqString += value+"x"
            return eq2text(integerList,pos+1,eqString )
    if pos==1:
        eqString+= positiveOrNegative(value)+" = "
        return eq2text(integerList,pos+1,eqString)

#Sjekker om tallet skal ha fortegn eller ei
def positiveOrNegative(value):
    operator =" + "
    number=int(value)
    if number < 0:
        operator=" - "
        return operator+str(-number)
    else:
        return operator+value
    
def ok(L):
    if 0 in L:
        return False
    if L[0] == L[2]:
        return False
    elif L[1] == L[3]:
        return False
    else:
        return True

def make_eq():
  equationList = [random.randint(-20,20) for number in range(4)]
  #Sjekker om randomgenerert liste er innenfor kravene, ellers kjører den funksjonen på nytt
  if ok(equationList):
    return equationList
  else:
    return make_eq()

def make_n_eqs(n):
    equations = [make_eq() for eq in range(n)]
    if checkEqualEquations(equations) == False:
        return make_n_eqs() #Lager et nytt sett med likninger om noe skulle være utenfor kravene
    else:
        return equations

def checkEqualEquations(equations):
    #Sammenligner likningene og gir False om noen er identiske, eller ved tilfeller av [a,b,c,d] og[c,d,a,b] 
    for i in range(len(equations)):
        for j in range(i + 1, len(equations)):
            if(equations[i] == equations[j]):
                return False
            if (equations[i][0:2] == equations[j][2:4] or (equations[i][2:4] == equations[j][0:2])):
                return False
    return True
         
def make_test(students,n):
    testDictionary ={}
    for student in students:
        testDictionary[student]= make_n_eqs(n)
    return testDictionary

def answer_questions(D):
    while True:
        try:
            name = input(str("Enter your name: ")).title()
            print("Please solve these equations:") 
            for i in range(len(D[name])):
                print(chr(97+i),") ",eq2text(D[name][i]))
                while True:
                    try:
                        answer=float(input("x = "))
                        D[name][i].append(answer)
                        break
                    except(ValueError):
                        print("Numbers only")
                        continue
            break 
        except (NameError, KeyError):   #Fanger opp om bruker taster inn en verdi som ikke finnes i dictionary.
            print("Sure that's correct? Try again.")
            continue
    return D

def  main():

    tests=answer_questions(make_test(["Ola","Kari","Fredrik"],5))
    print(tests)

if __name__ == '__main__':
      main()