a=str(input("enter student name:"))
b=int(input("enter marks:"))
if b>=90:
    print(a,"got A grade")      
elif b>=80 and b<90:
    print(a,"got B grade")
elif b>=70 and b<80:
    print(a,"got C grade")
elif b>=60 and b<70:
    print(a,"got D grade")
elif b>=50 and b<60:
    print(a,"got E grade")  
else:
    print(a,"got F grade")
    