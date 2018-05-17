'''Things i wanna do
    better system to choose the car
    better system to show the cars we've chose
    maye have them answer questions about subclasses ?
    more cars (not really)
    If it can choose anything it will choose the last added cars which are the perodua, needs a solution
'''
from Car import Car, Axia, Bezza, Alza, MyVi

carList = []
peroduaList= []
def add(list, x):
    list.append(x)

#### PROTON CARS
# Brand, Type, Model, Price
add(carList, Car("Proton","Sedan","Saga 1.3", 41425))  
add(carList, Car("Proton","Sedan","Perdana 2.0", 110540))
add(carList, Car("Proton","Sedan","Perdana 2.4", 134820))
add(carList, Car("Proton","Sedan","Persona 1.6", 48200))
add(carList, Car("Proton","Sedan","Prevé 1.6", 60610))
add(carList, Car("Proton","Hatchback","Suprima S 1.6", 68110))
add(carList, Car("Proton","Hatchback","Iriz 1.3", 45315))
add(carList, Car("Proton","MPV","Exora 1.6", 65700))
add(carList, Car("Proton","MPV","Ertiga 1.4", 62770))

### PERODUA
add(carList, Car("Perodua","Sedan","Bezza", 37500))
add(carList, Car("Perodua","MPV","Alza", 53565))
add(carList, Car("Perodua","Hatchback","Axia", 35660))
add(carList, Car("Perodua","Hatchback","Myvi", 46300))

### more details
add(peroduaList, Axia("Perodua","Hatchback","Axia", 24000, "Standard E", "Manual", 22.5, "No", "Fabric", "No"))
add(peroduaList, Axia("Perodua","Hatchback","Axia", 33720, "Standard G", "Manual", 22.5, "Radio and USB", "Fabric", "Yes"))
add(peroduaList, Axia("Perodua","Hatchback","Axia", 35660, "Standard G", "Auto", 21.6, "Radio and USB", "Fabric", "Yes"))
add(peroduaList, Axia("Perodua","Hatchback","Axia", 36635, "Standard E", "Manual", 22.5, "Radio and USB and Bluetooth", "SE Fabric", "Yes"))
add(peroduaList, Axia("Perodua","Hatchback","Axia", 38580, "Standard E", "Auto", 21.6, "Radio and USB and Bluetooth", "SE Fabric", "Yes"))
add(peroduaList, Axia("Perodua","Hatchback","Axia", 41500, "Standard E", "Auto", 21.6, "No", "Leather", "Yes"))

add(peroduaList, Bezza("Perodua","Sedan","Bezza", 35500, "GXTRA", 1.0, "Manual", 22.8, "Radio and USB and Bluetooth", "Fabric", "Yes"))
add(peroduaList, Bezza("Perodua","Sedan","Bezza", 37500, "GXTRA", 1.0, "Auto", 21.3, "Radio and USB and Bluetooth", "Fabric", "Yes + USB"))
add(peroduaList, Bezza("Perodua","Sedan","Bezza", 41400, "PREMIUM X", 1.3, "Manual", 21.7, "Radio and USB and Bluetooth", "Fabric", "Yes + USB"))
add(peroduaList, Bezza("Perodua","Sedan","Bezza", 43350, "PREMIUM X", 1.3, "Auto", 21, "Radio and USB and Bluetooth", "Fabric", "Yes + USB"))
add(peroduaList, Bezza("Perodua","Sedan","Bezza", 49200, "ADVANCE", 1.3, "Auto", 22, "Full with navigation", "Leather", "Yes + USB"))

add(peroduaList, Alza("Perodua","MPV","Alza", 50650, "1.5 S", "Manual", "Radio and USB and Bluetooth", "Fabric", "Without"))
add(peroduaList, Alza("Perodua","MPV","Alza", 53565, "1.5 S", "Auto", "Radio and USB and Bluetooth", "Fabric", "Without"))
add(peroduaList, Alza("Perodua","MPV","Alza", 54540, "1.5 SE", "Manual", "Radio and USB and Bluetooth", "SE Fabric", "With"))
add(peroduaList, Alza("Perodua","MPV","Alza", 57455, "1.5 SE", "Auto", "Radio and USB and Bluetooth", "SE Fabric", "With"))
add(peroduaList, Alza("Perodua","MPV","Alza", 62900, "1.5 Advance", "Auto", "Full with navigation", "Leather", "With"))

add(peroduaList, MyVi("Perodua","Hatchback","Myvi", 44300, "G", 1.3, "Manual", 20.5, "Radio and USB", "No", "No"))
add(peroduaList, MyVi("Perodua","Hatchback","Myvi", 46300, "G", 1.3, "Auto", 20.1, "Radio and USB", "No", "No"))
add(peroduaList, MyVi("Perodua","Hatchback","Myvi", 48300, "X", 1.3, "Auto", 21.1, "Radio and USB and Microphone", "Yes", "No"))
add(peroduaList, MyVi("Perodua","Hatchback","Myvi", 51800, "H", 1.5, "Auto", 20.1, "Radio and USB and Microphone", "Yes", "No"))
add(peroduaList, MyVi("Perodua","Hatchback","Myvi", 55300, "AV", 1.5, "Auto", 20.1, "Full with navigation", "Yes", "Yes"))

def show():
    for car in carList:
        print("\nModel: ",car.name)
        print("Type: ", car.car_type)
        print("Price: RM", car.price)


def run():
    a = input("What is the brand you prefer? Proton / Perodua\n")
    av = input("How much do you value this 1 - 5\n")
    b = input("What is the car type that you prefer? Sedan / MPV / Hatchback\n")
    bv = input("How much do you value this 1 - 5\n")
    c = input("How much is your budget? RM30000 - RM70000\n")
    cv = input("How much do you value this 1 - 5\n")

    scores= []

    for car in carList:
        x = 0
        if car.brand == a:
            x += 1* int(av)
        if car.car_type == b:
            x += 1* int(bv)
        if car.price < int(c):
            x += 1* int(cv)
        scores.append([car, x])



    scores_sorted= []
    for i in range(len(scores)):
        max= scores[len(scores)-1]
        for j in range(len(scores)):
            if max[1]< scores[j][1]:
                max= scores[j]
        scores_sorted.append(max)
        scores.remove(max)

    names= []
    for i in range(len(scores_sorted)):
        if i< 3:
            scores_sorted[i][0].show()
            for j in range(len(peroduaList)- 1):
                if peroduaList[j].name== scores_sorted[i][0].name:
                    check= True
                    for s in names:
                        if s== peroduaList[j].name:  check= False
                    if check:
                        names.append(peroduaList[j].name)
                        print("*Adding")

    if len(names)== 1:
        check= input("The car "+ names[0]+ " Has more variants, would you like to see it ?\t")
        if check== "yes":
            for i in peroduaList:
                if i.name == names[0]:
                    i.show()
    elif len(names)== 2:
        check= input("Two of the suggested cars have more variants, enter "+ names[0]+ " to see it's details or enter "+ names[1]+" ")
        for i in peroduaList:
            if i.name== check:
                i.show()
    elif len(names)== 3:
        check= input("Three of the suggested cars have more variants, enter "+ names[0]+ " to see it's details or enter "+ names[1]+ " or enter "+ names[2]+" ")
        for i in peroduaList:
            if i.name== check:
                i.show()

				
run()

wait = input("\n\nPress enter to exit")