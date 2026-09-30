print("SMALL BUSINESS LOAN APPLICATION")
owner_age = int(input("Enter your Age: "))
monthly_revenue = float(input("Enter your Monthly Revenue: "))
credits_score = float(input("Enter your Credit Score: "))
years_in_business = float(input("Enter your Years in Business: "))
has_default = bool(input("Do you have any defaults? (True/False): "))
has_collateral = bool(input("Do you have collateral? (True/False): "))
collateral_value = float(input("Enter your collateral value: "))

max_loan = 0
base_fee = 0

if owner_age >= 21 and years_in_business >= 2.0 and has_default == False:
    print("Baseline Requirements Met: Eligible for Loan Application")
    if credits_score >= 720: #tier 1
        max_loan = monthly_revenue * 3
        print("Maximum Loan Limit: $", max_limit)
        if monthly_revenue >= 50000:
            base_fee = max_limit * 0.015
            print("Base Fee: %", base_fee)
        else:
            base_fee = max_loan * 0.025
            print("base free rate is",base_fee)
    elif credits_score <= 620 and credits_score <720:
        max_loan = monthly_revenue * 1.5
        if years_in_business >= 5:
            base_fee = max_loan * 0.02
            print("base fee rate is",base_fee)
        else:
            base_fee = max_loan * 0.035
            print("base fee rate is", base_fee)
    elif credits_score < 620:
        print("credit score too low for loan")
    else:
        print("not tier1")  