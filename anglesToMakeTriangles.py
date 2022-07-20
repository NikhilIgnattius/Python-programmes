a = int(input("Enter angle-1:"))
b = int(input("Enter angle-2:"))
c = int(input("Enter angle-3:"))

if a+b+c == 180:
    if a > 0 and b > 0 and c > 0:
        print("A triangle can be formed.")

    else:
        print("Please enter a valid data.")

else:
    print("It can't form a triangle")
