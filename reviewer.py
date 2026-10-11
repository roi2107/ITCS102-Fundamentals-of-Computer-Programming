#inputs
owner_age = int(input("Enter your age --->"))
revenue = float(input("REVENUE --->"))
credit_score = int(input("CREDIT SCORE --->"))
years_in_business = float(input("YEARS IN BUSINESS --->"))
has_defaults = bool(input("FILE OF BANKRUPTCY --->"))
collateral = input("COLLATERAL NAME --->")
collateral_value = float(input("COLLATERAL VALUE --->"))


max_loan = 0
base_fee = 0

if owner_age >= 21 and years >= 2.0 and has_defaults == False:
    print("BASELINE PASSED")
    if credit_score >= 720: #tier 1
        max_loan = revenue * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO", max_loan)
        print("HIGH CREDIT SCORE")
        if revenue >= 50000:
            print("REVENUE IS HIGHER THAN 50K")
            base_fee = max_loan * 0.015


    elif cs >= 620 and cs >= 720: #tier2
        print("Credit Score withn Range of 620 to 720")
        max_loan = revenue * 1.5
        print("Maximum Loan for this credit score is", max_loan)
        if years_in_business >= 5:
            print("Business year are more than 5 years")
            base_fee = max_loan * 0.02
            print("Base fee rate is set to", base_fee)
        else:
            print("Business year are less than 5 years")
            base_fee = max_loan * 0.035 
            print("Base fee is set to", base_fee)


    elif credit_score >= 620 and credit_score >= 1: #tier3
        print("Decline, Credit Score too Low!")

        if collateral_value >= max_loan:
            print("Accepted ",collateral,"with a value of", collateral_value, "is ACCEPTED")
        else :
            print("Rejected: Insufficient collateral value for", collateral_value)

    surge_fee_rate = max_loan = base_fee 
    print("Additional Charged of", surge_fee_rate)
    if max_loan % 500 != 0:
        print("Additional Charge Added")
        surge_fee_rate += 250
        print("Updated base fee is", surge_fee_rate)
    else:
        print("INVALID")
else:
    print("BASELINE FAILED")
    
