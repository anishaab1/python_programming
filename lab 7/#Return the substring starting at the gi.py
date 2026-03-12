# Return the substring starting at the given position with the specified length

s = input("Enter a string: ")
start, length = map(int, input("Enter the starting position and length: ").split())

if start < 0 or start > len(s) or length < 0:
    print("")
else:
    ans = s[start:start+length]
    print(ans)
