#JEEPNEY SIMULATOR 

passengers = [ "iya", "yeti", "kiro" ]
passengers.append("Dan")
passengers.insert(0,"Lola")
passengers.remove("yeti")
x = passengers.pop
y = passengers.pop(0)
len(passengers)
"iya" in passengers
passengers.reverse()
route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
SEATS = 6 
FARE = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("\n1Sakay\n2 Priority seat\n3 Para po!")
    print("\n4 Baba sa pinto \n5 Baba sa harap")
    print("\n6 Seat check \n7 Balikan \n8 Exit")
    choice = input(choice)

    if choice == "1":
        if len(passengers) == SEATS:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "boarded at the back.")

    elif choice == "2":
        if len(passengers) == SEATS:
         print("Puno na!")
    else:
        name = input("Name: ")
        passengers.insert(0, name)
        total = total + FARE
        print(name, "took the priority seat")
            
    elif choice == "3":
        name = input("Name: ")
        if name in passengers:
            passengers.remove(name)
            print("name, got off. Ingat!")
        else:
            print(name, "is not on this jeep.")

    elif choice = "4":
        if len(passengers) == 0:
           print("The jepp is empty. ")
        else:
             left = passengers.pop()
             print(left, "got off at the door." )

    elif choice = "5":
        if len(passengers) == 0:
           print("The jeep is empty")
        else:
             front = passengers.pop(0)
             print(front, "got off at the front")

    elif choice = "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice = "7"
         route.reverse()
         print("Route:", route)

    elif choice = "8":
         print("Total fare today:", total)
         break

        else: print("Invalid code")