grade = float(input("Enetr Your Grade: "))
if grade == 4:
    print("A+")
elif grade >= 3.75 and grade <= 3.99:
    print("A")
elif grade >= 3.26 and grade <= 3.74:
    print("A-")
elif grade >=3.1 and grade <= 3.25:
    print("B+")
elif grade >=2.76 and grade <=3:
    print("B")
elif grade >=2.51 and grade<=2.75:
    print("b-")
elif grade>=2.1 and grade <= 2.5:
    print("C+")
elif grade == 2:
    print("C")
elif grade < 2:
    print("faill")
else:
    print("invalid Grade")