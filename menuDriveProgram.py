while True:
    print("1.Area of Rectangle \n2.Area of Square \n3.Area of Circle \n4.Area of Triangle \n5.Exit")

    ch = int(input("Enter your choice(1-5):"))

    if ch == 1:
        l = int(input("Enter the length of the Rectangle:"))
        b = int(input("Enter the breadth of the Rectangle:"))
        print("The area of the rectangle is:",l*b)

    elif ch == 2:
        s = int(input("Enter the side of the Square:"))
        print("The area of the Square is:",s*s)

    elif ch == 3:
        r = int(input("Enter the radius of the Circle:"))
        print("The area of the Circle is:",3.14*r*r)

    elif ch == 4:
        b = int(input("Enter the base length of the Triangle:"))
        h = int(input("Enter the height of the Triangle:"))
        print("The area of the Triangle is:",1/2*b*h)

    elif ch == 5:
        print("Thank you!!!")
        break

    else:
        print("The entered number is invalid.")




    

    
