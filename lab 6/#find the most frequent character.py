#find the most frequent character 
s="programming"
max_char=max(s,key=s.count)
print(max_char)

#1 2 3 4 5 6 7 8 9 10
#p r o g a m m i n g

#here the location of "r" is 1 and 4
# "m" is 5 and 6 
#so "r" is coming first accroding to the location and "m" is coming second according to the location
#thts why the output is "r" 