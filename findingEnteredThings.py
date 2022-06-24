a = input('Enter something except special characters:')

if ord(a) >= 65 and ord(a) <= 90 or ord(a) >= 97 and ord(a) <= 122:
    print("The entered value",a,"is an alphabet.")

else:
    print("The entered value",a,"is a number.")
