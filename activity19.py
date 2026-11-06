from getpass import getpass
isLogin = True
loginattempt = 0

u = "roi"
p = "klint"


while isLogin == False:
    username = input("Please enter your username -->")
    password = input("Please enter your password -->")

    if username == u and password == p:
        print("Login attempt successfuly")
        print("Total Login Attempts", loginattempt)
        isLogin = True

    else:
        print("Incorrect Username and Password")
        loginattempt += 1
        isLogin = False