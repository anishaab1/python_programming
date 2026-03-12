#check palindrome
#s='madam'
#if s==s[::-1]:
 #   print('palindrome')
#else:
 #   print('not palindrome')


#count vowels
s='education'
count=0 
for ch in s:
    if ch.lower() in 'aeiou':
        count+=1
print('number of vowels:',count)


#count constants
s='education'
count=0 
for ch in s:
    if ch.lower() not in 'aeiou' and ch.isalpha():
        count+=1
print('number of constants:',count)



#count frequency of each character
s='hello world'
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)


      
      #find the first non-repeating character
s='hello world'
for ch in s:
    if s.count(ch)==1:
        print('first non-repeating character:',ch)
        break
