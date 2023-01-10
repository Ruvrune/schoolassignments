class Vehicle:
    def __init__(self, brand, year, mileage, price, licencePlate=""):
        self.__brand =  brand
        self.__year = year
        self.__mileage = mileage
        self.__price = price
        self.__licencePlate = licencePlate
        self.__tickets = []
        
    def getType(self):
        return self.__brand

    def getYear(self):
        return self.__year

    def getMileage(self):
        return self.__mileage

    def getPrice(self):
        return self.__price

    def getLicencePlate(self):
        return self.__licencePlate

    def getTickets(self):
        return self.__tickets

    def setType(self, brand):
        self.__brand = brand

    def setYear(self, year):
        self.__year = year

    def setMileage(self, km):
        self.__mileage = km

    def setPrice(self, price):
        self.__price = price

    def setLicencePlate(self, licencePlate):
        self.__licencePlate = licencePlate

    def addTicket(self, number, ticketTuple, speedLimit):
        ticket = SpeedTicket(number, ticketTuple[0],ticketTuple[1], speedLimit )
        self.__tickets.append(ticket)

    def __str__(self):
        return f"{self.__brand} Year: {self.__year} Milage: {self.__mileage} Price: {self.__price}"

class Car(Vehicle):
    def __init__(self,brand, year, mileage, price, doors):
        super().__init__(brand, year, mileage, price)
        self.__doors = doors

    def getDoors(self):
        return self.__doors   

    def setDoors(self, doors):
        self.__doors = doors
    
    def __str__(self):
         return f"{super().__str__()} Doors: {self.__doors}"
   
class  Truck(Vehicle):
    def __init__(self,brand, year, mileage, price, drive):
        super().__init__(brand, year, mileage, price)
        self.__drive = drive
    
    def getDrive(self):
        return self.__drive

    def setDrive(self, drive):
        self.__drive = drive

    def __str__(self):
         return f"{super().__str__()} - {self.__drive}"

class SUV(Vehicle):
    def __init__(self,brand, year, mileage, price, passengers):
        super().__init__(brand, year, mileage, price)
        self.__passengers = passengers

    def getPassengers(self):
        return self.__passengers  

    def setPassengers(self, passengers):
        self.__passengers = passengers
    
    def __str__(self):
         return f"{super().__str__()} Passengers: {self.__passengers}"

class SpeedTicket(Vehicle):
    def __init__(self, number,speed, timeOfRegistration, speedLimit):
        self.__number = number
        self.__timeOfRegistration = timeOfRegistration
        self.__speed = speed
        self.__speedLimit = speedLimit

    def getNumber(self):
        return self.__number

    def getTimeOfRegistration(self):
        return self.__timeOfRegistration

    def getSpeed(self):
        return self.__speed

    def getSpeedLimit(self):
        return self.__speedLimit

    def setNumber(self, number):
        self.__number = number

    def setTimeOfRegistration(self, time):
        self.__timeOfRegistration = time

    def setSpeed(self, speed):
        self.__speed = speed

    def setSpeedLimit(self, speedLimit):
        self.__speedLimit = speedLimit

    def __str__(self):
        return f"Regnummer: {self.__number} hadde snittfart på {self.__speed} i en {self.__speedLimit}-sone. Tidspunkt: {self.__timeOfRegistration}"