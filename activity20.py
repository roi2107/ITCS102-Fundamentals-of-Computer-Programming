anime = []

isContinuing = True

while isContinuing:
    ans = input("Do you want to add a title of an anime (y/n): ") == "y"
    if ans == True:
        title = input("Enter the title of an anime: ")
        anime.append(title)
        print(anime)
      
    else:
        isContinuing = False
        print(anime)