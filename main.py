
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The Year {year} Leap Year")
        else:
            print(f"The Year {year} Not a Leap Year")
    else:
        print(f"The Year {year} Leap Year")
else:
    print(f"The Year {year} is Not a Leap Year")
    