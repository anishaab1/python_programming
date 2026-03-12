#check the digits, alpha, special char , char
s= "anishabhadra21@gmail.com"

alphabets = 0 #count1
digits = 0 #count2
special_chars = 0 #count3

for char in s:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1


        print("Number of alphabets:", alphabets)
print("Number of digits:", digits)
print("Number of special characters:", special_chars)
print("Total characters:", total)