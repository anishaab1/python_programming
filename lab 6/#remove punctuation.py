#remove punctuation
import string
s="Hello, World! Welcome to Python programming."
result=""
for ch in s:
    if ch not in string.punctuation:
     result+=ch
print(result)