a = int(input('Enter your percentage of marks:'))

if a > 100:
    print("Your percentage is invalid.")


elif a >= 90:
    print("Excellent.You have got A grade.")

elif a >= 80:
    print("Good.You have got B grade.")

elif a >= 60:
    print("Average.You have got C grade.")

elif a >= 40:
    print("Needs Improvement.You have got D grade.")

else:
    print("Sorry.You have failed.")


