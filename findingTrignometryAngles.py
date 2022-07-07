import math


length = int(input("Enter the length of the ladder: "))
degrees = int(input("Enter the alignment degree: "))

radian = math.radians(degrees)
print(radian)

sin = math.sin(radian)
print(sin)

height = round(length * sin,2)

print("The height reached by ladder with length",length,"feet and aligned at",degrees,"degrees is",height, "feet.")


