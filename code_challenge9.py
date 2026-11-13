
# challenge1
loan_amount = float(input("Enter the loan amount: ---> "))
loan_period = int(input("Enter the years: ---> "))
interest_rate = 0.00256

months = loan_period * 12
monthly_principal = loan_amount / months
remaining_loan = loan_amount

print("\nMonth\tPayment\t\tInterest\tPrincipal\tRemaining Loan")

for r in range(months):
    interest = remaining_loan * interest_rate
    monthly_payment = monthly_principal + interest
    remaining_loan = remaining_loan - monthly_principal

    print(str(r + 1) + "\t" + 
        format(monthly_payment, ".2f") + "\t\t" +
        format(interest, ".2f") + "\t\t" +
        format(monthly_principal, ".2f") + "\t\t" +
        format(remaining_loan, ".2f"))


#challenge 2

rows = int(input("Enter number of rows: "))

for x in range(rows):
    for y in range(rows - x - 1):
        print(" ", end="")

    for z in range(2 * x + 1):
        if z == 0 or z == 2 * x or x == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
    
#challenge3

rows = int(input("Enter number of rows: "))

for a in range(rows):
    for b in range(rows):
        if a == 0 or a == rows - 1 or b == rows - a - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

