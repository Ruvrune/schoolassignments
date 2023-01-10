## This program creates a Car object, a Truck object,
# and an SUV object.
import vehicles
import pickle
import os.path
import radars

# Constants for the menu choices
NEW_CAR_CHOICE = 1
NEW_TRUCK_CHOICE = 2
NEW_SUV_CHOICE = 3
FIND_VEHICLE_CHOICE = 4
SHOW_VEHICLES_CHOICE = 5
SPEEDING_CHOICE = 6
QUIT_CHOICE = 7

def main():
    # Create empty list for vehicles
    vehicles_list = loadVehicleListFromFile()
    # Create a Car object for a used 2001 BMW
    # with 70,000 miles, priced at $15,000, with
    # 4 doors.
    car = vehicles.Car('BMW 320', 2001, 70000, 15000.0, 4)
    car.setLicencePlate("DN19091")
    vehicles_list.append(car)
    # Create a Truck object for a used 2002
    # Toyota pickup with 40,000 miles, priced
    # at $12,000, with 4-wheel drive.
    truck = vehicles.Truck('Toyota RAV4', 2002, 40000, 12000.0, '4WD')
    truck.setLicencePlate('FY99401')
    vehicles_list.append(truck)
    # Create an SUV object for a used 2000
    # Volvo with 30,000 miles, priced
    # at $18,500, with 5 passenger capacity.
    suv = vehicles.SUV('Volvo XC60', 2010, 30000, 18500.0, 5)
    vehicles_list.append(suv)

    choice = 0
    while True:
        try:
            while choice != QUIT_CHOICE:
                # display the menu.
                display_menu()

                # Get the user's choice.
                choice = int(input('Enter your choice: '))

                # Perform the selected action.
                if choice == NEW_CAR_CHOICE:
                    print('Add a new car')
                    car = vehicleInput(NEW_CAR_CHOICE)
                    vehicles_list.append(car)
                    print("\n Added " + car.__str__() +" to database \n")
                elif choice == NEW_TRUCK_CHOICE:
                    print('Add a new truck')
                    truck = vehicleInput(NEW_TRUCK_CHOICE)
                    vehicles_list.append(truck)
                    print("\n Added " + truck.__str__() +" to database \n")
                elif choice == NEW_SUV_CHOICE:
                    print('Add a new SUV')
                    suv = vehicleInput(NEW_SUV_CHOICE)
                    vehicles_list.append(suv)
                    print("\n Added " + suv.__str__() +" to database \n")
                elif choice == FIND_VEHICLE_CHOICE:
                    print('Find vehicle by name')
                    findVehicle(str(input('Search for: ')).lower(), vehicles_list)
                elif choice == SHOW_VEHICLES_CHOICE:
                    #show all vehicles
                    print('The following cars are in inventory:')
                    vehicles_list.sort(key=lambda x: (x.getType(), x.getYear())) #Bruker lambdafunksjon for å sortere etter bilmerke og år
                    for item in vehicles_list:
                        print(item)
                elif choice == SPEEDING_CHOICE:
                    print('Check number for speeding history')
                    checkForSpeeding(vehicles_list)
                elif choice == QUIT_CHOICE:
                    saveVehicleFile(vehicles_list)
                    print('Exiting the program...') 
                else:
                    print('Error: invalid selection.')
            break  
        except ValueError:
            print("Digits only. Please try again.")
            continue  


# The display_menu function displays a menu.
def display_menu():
    print('        MENU')
    print('1) New car')
    print('2) New truck')
    print('3) New SUV')
    print('4) Find vehicles by make')
    print('5) Show all vehicles')
    print('6) Check speeding')
    print('7) Quit')

def vehicleInput(vehicleChoice):
    make = str(input('Make: '))
    if len(make.split(' ')[0]) <= 3: #Gjør om til uppercase om det er en doning på mindre enn tre bokstaver, f.eks BMW
        make = make.upper()     
    while True:
        try:
            year = int(input('Year: '))
            milage = int(input('Milage: '))
            price = float(input('Price: '))
            break
        except ValueError:
            print("Digits only. Please try again.")
            continue

    if vehicleChoice == NEW_CAR_CHOICE:
        while True:
            try:
                doors = int(input("Doors: "))
                if doors > 5:
                    print("No car has  that many doors, that's silly. Try again.")
                    continue
                elif doors < 1:
                    print("How do you get to drive your car, if there are no doors? Try again.")
                    continue
                else:
                    break
            except ValueError:
                print("Digits only. Please try again.")
                continue

        return vehicles.Car(make, year, milage, price, doors)    
    if vehicleChoice == NEW_TRUCK_CHOICE:
        while True:
            try:
                wheels = int(input('2WD or 4WD (Enter 2 or 4): '))
                if wheels == 2 or wheels ==4:
                    wd = str(wheels)+"WD"
                    break
                else:
                    print("Input must be 2 or 4")
                    continue
            except ValueError:
                print("Digits only. Please try again.")
                continue
        return vehicles.Truck(make, year, milage, price, wd)    
    if vehicleChoice == NEW_SUV_CHOICE:
        while True:
            try:
                passengers = int(input("Passengers: "))
                if passengers > 10:
                    print("Seems like a bus to me, sure that's an SUV? Try again.")
                    continue
                elif passengers < 1:
                    print("No room for passengers? Are you sure? Try again.")
                    continue
                else:
                    break
            except ValueError:
                print("Digits only. Please try again.")
                continue
        return vehicles.SUV(make, year, milage, price, passengers)

def findVehicle(lookforVehicle, vehicles_list):
    sameMakeList = [vehicle for vehicle in vehicles_list if lookforVehicle in vehicle.getType().lower()]
    if len(sameMakeList) < 1:
        print(f"Could not find {lookforVehicle} in database")
    for brand in sameMakeList:
        print (brand)
    print("\n")

def checkForSpeeding(vehicles_list):
    #Lag et menyvalg for sjekk av fartsovertredelser. For hvert kjøretøy skal en 
    # gå igjennom dictionary fra listSpeeders, dersom bilnummer er registrert 
    # skal det opprettes et objekt av typen SpeedTicket og tas vare på for det aktuelle kjøretøy.
    print("check for speeding")
    filename = "box_a.txt"
    filename2 = "box_b.txt"
    speedLimit = 60
    #legg inn fartssone
    speeders = radars.listSpeeders(filename, filename2, speedLimit, 5)

    for vehicle in vehicles_list:
        licencePlate = vehicle.getLicencePlate() #Henter registreringsnummer til kjøretøyet
        if licencePlate != '': #Sjekker kun kjøretøyene der det er registrert et nummer
            if licencePlate in speeders: #Sjekker om nummeret forekommer i speeders-dictionaryen
                #Sjekker om det allerede er registrert bøter på kjøretøyet
                if len(vehicle.getTickets())>0:
                    #Går gjennom bøtene på kjøretøyet og sjekker at tidspunkt ikke er identisk med det som 
                    #er registrert fra før. (Man kan jo umulig få to bøter på nøyaktig samme tid)
                    for ticket in vehicle.getTickets():
                        if speeders[licencePlate][1] not in ticket.getTimeOfRegistration():
                            vehicle.addTicket(vehicle.getLicencePlate(),speeders[licencePlate], speedLimit)
                elif len(vehicle.getTickets())==0: 
                    vehicle.addTicket(vehicle.getLicencePlate(),speeders[licencePlate], speedLimit)
                for i in vehicle.getTickets():
                    print(i)
                
def loadVehicleListFromFile():
    if not os.path.isfile("vehicles.dat"):
        print("No stored list available, start from scratch")
        return [] # Return an empty list
    try:
        inputFile = open("vehicles.dat", "rb")
        vehicles_list = pickle.load(inputFile)
        print("Loaded data from file")
    #Exception ved feil i binærfil, f.eks txt-fil istedenfor binær
    except pickle.UnpicklingError:
        print("Something went wrong while loading file. Wrong format? Starting from scratch.")
        vehicles_list = []   
    except EOFError:
        vehicles_list = []        
    inputFile.close()
    return vehicles_list

def saveVehicleFile(vehicles_list):
    outputFile = open("vehicles.dat", "wb")
    vehicles_list.sort(key=lambda x: (x.getType(), x.getYear())) #Bruker lambdafunksjon for å sortere etter bilmerke og år
    pickle.dump(vehicles_list, outputFile)
    print("Stored to file.")
    outputFile.close()

# Call the main function.
if __name__ == '__main__':
      main()

