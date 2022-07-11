#Series: S = 1! + 2! + 3! ... + n!

n = int(input("Enter the value of n:"))

f = 1
s = 0

for i in range(1,n+1):
    f *= i
    s += f
    
    

print("Sum of series =",s)
