






age = int(input("Enter age"))
is_employed = bool(input ("Are you currently employed? ---> "))
credit_score = eval(input("Credit score history ---> "))
annual_income = eval(input("How much is your annual income? ---> "))
has_collateral = bool(input("Do you have any collateral?---> "))
                      
if age >= 21 and is_employed == True: 
     print("pwidi")
else: 
     print("Baseline requirement failed")

if credit_score >= 750:
     print("Your Credit Score is above 750")
     if   annual_income >= 100000:
        print("You have a high annual income")
        base_rate = 4.5
        print("Hi, your interest rate is", base_rate)
     else: 
         base_rate = 5.0
         print("Hi, your interest rate is", base_rate)   
elif credit_score >= 600 and credit_score < 750:
     if has_has_collateral == True:
        base_rate = 7.0 
        print("Hi, your interest rate is ", base_rate)
     elif annual_income <4000:
          base_rate = 9.5 
          print("Hi, your interest rate is ", base_rate)
     else: 
        base_rate = 8.0
        print("Hi, your interest rate is ", base_rate)

     if credit_score < 600:
        print("Rejected: Credit Scpre too low")
            

else:
    print("Baseline requirement failed")

            