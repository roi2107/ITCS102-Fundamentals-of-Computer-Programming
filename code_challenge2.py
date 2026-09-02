#code challenge 2

d = eval(input("Enter the amount of deposit: "))

n1 = d // 1000
d = d % 1000
n2 = d // 500
d = d % 500
n3 = d // 200
d = d % 200
n4 = d // 100
d = d % 100
n5 = d // 50
d = d % 50
n6 = d // 20
d = d % 20
n7 = d // 10
d = d % 10
n8 = d // 5
d = d % 5
n9 = d // 1
d = d % 1

print(n1, "- 1000")
print(n2, "- 500")
print(n3, "- 200")
print(n4, "- 100")
print(n5, "- 50")
print(n6, "- 20")
print(n7, "- 10")
print(n8, "- 5")
print(n9, "- 1")
