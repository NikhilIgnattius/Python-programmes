string = input("Enter a word:")
vowel = "aeiouAEIOU"
count = 0

for i in string:
    if i in vowel:
        count += 1

print("No.Of.Vowels =",count)
