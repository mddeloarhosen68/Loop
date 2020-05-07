#Ex:1
i = 1
while i <= 5:
    print("Anon")
    i = i + 1

#Ex:2
i = 5
while i >= 1:
    print("Anon")
    i = i - 1


#Ex:3
i = 1
while i <= 5:
    print("Anon ",end = "")
    j = 1
    while j <= 4:
        print("Rocks ",end = "")
        j = j + 1

    i = i + 1
    print()