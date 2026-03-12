a=int(input("enter two digit num:"))
if(a>10 and a<=99):
 sum_digit=(a//10)+(a%10)
 print("the sum of the digit is",sum_digit)
else:
 print("invalid input")
