#Series:S = x/1! - x/2! + x/3! - x/4! ... (+/-)x/n!

x = int(input("Enter the value of x:"))
n = int(input("Enter the value of n:"))

f = 1
s = 0

for i in range(1,n+1):
    f *= i
    if i % 2 == 0:
        s -= x/f

    else:
        s += x/f
        
  

print("Sum of series =",s)

  
   
