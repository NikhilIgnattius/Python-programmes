a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

if b*b-(4*a*c) == 0:
    print("The nature of roots are real and equal.")

elif b*b-(4*a*c) > 0:
    print("The nature of roots are real and distinct.")

else:
    print("The nature of roots are not real.")
    
