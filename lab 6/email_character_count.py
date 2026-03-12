# Count alphabets, digits, special characters and total characters in email ID


s= "anishabhadra21@gmail.com"

alphabets = ""
digits = ""
special_chars = ""

count1 = 0
count2 = 0
count3 = 0

for char in s:
    if char.isalpha():
        alphabets += char
        count1 += 1
    elif char.isdigit():
        digits += char
        count2 += 1
    else:
        special_chars += char
        count3 += 1



print("Number of alphabets:", count1)
print("Number of digits:", count2)
print("Number of special characters:", count3)

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Special characters:", special_chars)


