#check whether a the first letter is a vowel or not
string = input("Enter a string: ")
if string[0].lower() in 'aeiou':
    print("The first letter is a vowel.")
else:    
    print("The first letter is not a vowel.")
