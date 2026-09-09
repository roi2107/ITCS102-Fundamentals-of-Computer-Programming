name = input("Please enter your name: ")

item = input("Enter the type of item: ")

weight = float(input("Enter weight (kg): "))

distance = float(input("Enter distance (km): "))

is_express = input("Is it express? (yes/no): ")

is_international = input("Is it international? (yes/no): ")

base_cost = (weight * 2.50) + (distance * 0.15)

if is_express != "yes" and is_express != "no":
    print("Invalid answer")

elif is_international != "yes" and is_international != "no":
    print("Invalid answer")

elif weight <= 2.0 and distance <= 100 and is_express == "no" and is_international == "no":
    total = 0
    print("Rate: Free Shipping")

elif is_international == "yes" and is_express == "yes":
    total = (base_cost * 1.40) + 50
    print("Rate: International Express")

elif is_express == "yes" or (is_international == "yes" and weight > 20):
    total = (base_cost * 1.20) + 25
    print("Rate: Express or Heavy International")

elif weight > 30 or distance > 1000:
    total = base_cost + 30
    print("Rate: Oversized")

else:
    total = base_cost
    print("Rate: Standard Rate")

print("\n--- Global Freight Calculator ---")
print("Name: ", name)
print("Type of item: ", item)
print("Base Cost:", base_cost)
print("Total Shipping Cost:", total)