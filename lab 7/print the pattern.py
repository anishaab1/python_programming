#print the pattern
str='abcdqwertyuio'
n = int(input("Enter the number of rows: "))
for i in range(1,n+ 1):
    for j in range(i,n+1):
        print(str[j], end=' ')
    print()


    #print the pattern
string='abcd'
for i in range(len(string)):
    for j in range(i,len(string)):
        print(string[j],end=" ")

    print()