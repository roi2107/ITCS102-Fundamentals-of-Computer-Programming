for x in range(6,0,-1):
    for y in range(1, x + 1):
        if y == 1 or y == x or x == 6:
          print("*", end="")
    print("")
