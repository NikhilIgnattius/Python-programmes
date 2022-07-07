a = float(input("Enter the no.of.units consumed:"))

if a <= 50:
    print("The total amount is:",0)

elif a <= 100:
    print("The total amount is:",a*0.6)

elif a <= 200:
    print("The total amount is:",a*0.75)

elif a <= 300:
    print("The total amount is:",a*0.9)

else:
    print("The total amount is:",a*1.5)



