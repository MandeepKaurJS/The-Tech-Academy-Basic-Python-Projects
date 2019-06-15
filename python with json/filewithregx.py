import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")
#split chracters 
x = re.split("\s", txt)
print(x)
#for first letter split
x = re.split("\s", txt, 1)
print(x)
# for adding anythin between letter
x = re.sub("\s", "*", txt)
print(x)
#replace with symbal two occurance
x = re.sub("\s", "9", txt, 2)
print(x)
#search will returns the match object
x = re.search("ai", txt)
print(x)
j = re.search("\s", txt)
print("The first white-space character is located in position:", j.start()) 
#Search for an upper case "S" character in the beginning of a word, and print its position:


x = re.search(r"\bS\w+", txt)
print(x.span())
#Search for an upper case "S" character in the beginning of a word, and print the word:

x = re.search(r"\bS\w+", txt)
print(x.group())

  

str = "The rain in Spain"
y = re.findall("ai", str)
print(y)
k = re.findall("Portugal", str)
if (k):
  print("Yes, there is at least one match!")
else:
  print("No match")

print(k) 