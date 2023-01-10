from LinkedList import LinkedList

testListe = LinkedList()

testListe.add("Elg") 
testListe.add("Tiur")
testListe.add("Gaupe")
testListe.add("Fasan")
testListe.add("Mår")
testListe.add("Grevling")
testListe.add("Elg")
testListe.add("Elefant")

print(testListe)
print("Inneholder listen Fasan? ",testListe.contains("Fasan"))
print("Inneholder listen Huskatt? ", testListe.contains("Huskatt"))
print("Element på index 2 er: ", testListe.get(2))
print("Siste plassering til Elg er: ", testListe.lastIndexOf("Elg"))
print(testListe.remove("Mår")) #Returnerer True hvis Mår er i lista
print(testListe.remove("Øgle")) #Returnerer ingenting om Øgle ikke er i lista
print("Oppdatert liste, uten mår: \n", testListe)
print("Index til Elefant er: ", testListe.indexOf("Elefant"))
testListe.set(testListe.indexOf("Elefant"),"Hare")
print("Bytter ut Elefant med Hare. Ny liste er: \n", testListe)
#print("Dette er bare tullball, sletter hele listen ")

testListe.clear()
print(testListe)
#print("Liste slettet")
