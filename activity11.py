import getpass


username = "roiroi123"
password = "kumag123"

u = input("Input Username ---> ")
p = getpass.getpass("Input Password ---> ")

if u == username and p == password: 
     print("username and password correct")

else:
     print("ACCESS DENIED")