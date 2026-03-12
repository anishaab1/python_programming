#find longest word
s='python is a easy language'
word=s.split()
longest=max(word,key=len)
print(longest)