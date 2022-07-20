a = int(input("Enter side-1:"))
b = int(input("Enter side-2(Base):"))
c = int(input("Enter side-3:"))

if a == b == c:
    print("It is an equilateral triangle.")

elif a == c != b:
    print("It is an isoceles triangle.")

else:
    print("It is a scalene triangle.")
