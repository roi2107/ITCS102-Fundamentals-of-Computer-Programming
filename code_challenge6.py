size = int(input("input the size of your pattern: "))

for w in range(size):
    for l in range(size):
        if w + l == size -1 or w == l:
            print("*", end = " ")
        else: 
            print(" ", end = " ")
    print()
