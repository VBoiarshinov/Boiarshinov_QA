first = int(input("First: "))
second = int(input("Second: "))
third = int(input("Third: "))

if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
elif first != second or second != third or third != first:
    print(0)
else:
    print("Bingo!")