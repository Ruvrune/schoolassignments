import math

def getConvexHull(p):
    
    stack = convexHull(p)
    #Hvis det er mindre enn tre punkter
    if len(p) < 3:
        return None
    return stack

def getRightmostLowestPoint(p): # p en todim liste med koordinater 
    rightMostIndex = 0 
    rightMostX = p[0][0]
    rightMostY = p[0][1] 

    for i in range(1, len(p)): 
        #finn nytt rightmostlowest koordinatpar 
        if rightMostY > p[i][1]:        #Finner punkt med lavest Y-verdi
            rightMostY = p[i][1]
            rightMostX = p[i][0]
            rightMostIndex = i
        elif rightMostY == p[i][1] and rightMostX < p[i][0]:    #Hvis flere punkter har samme Y-verdi -> Velg det med høyest X
            rightMostX = p[i][0]
            rightMostIndex = i  

    return p[rightMostIndex] 

#Finner hvilken retning neste punkt vender (Låner funksjonen fra Grahams).
# Returnert verdi over 0 -> Mot klokka. Under 0 -> Med klokka. =0 -> rett.
def whichSide(x0, y0, x1, y1, x2, y2):
    return (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)

def convexHull(s):     
    convexHull = []
    # Sett startpunkt (lengst ned til høyre)
    h0 = getRightmostLowestPoint(s)
    convexHull.append(h0)
    t0 = h0

    while(True):
        #Sett t1 til første posisjon i lista, med mindre dette er samme verdi som t0
        if s[0] != t0:
            t1 = s[0]
        else:
            t1 = s[1]
        for p in range(len(s)):
            if whichSide(t0[0],t0[1],s[p][0],s[p][1],t1[0],t1[1]) > 0:
                t1 = s[p]
        # Hvis t1 er h0 så er vi ferdig, og H beskriver et convex hull.
        if(t1 == h0):
            break
        #  Hvis ikke, legg t1 til H, tilordne t1 til t0
        else:
            convexHull.append(t1)
            t0 = t1       
    # Print Result
    return convexHull
def distance(x1, y1, x2, y2): 
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
