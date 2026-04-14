import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.findall("^The.*Spain$", txt)
print(x)
if x:
  print("YES! We have a match!")
else:
  print("No match")

print()
txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\\d", txt)
print(x)
print()
txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[A-Za-z]", txt)
print(x)
print()
txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)
print()
txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print()
txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
print()
txt = "hello planeto"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)
x = re.findall("he.+o", txt)
print(x)
print()
txt = "helo planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)
x = re.findall("he.{1}o", txt)

print(x)

x = re.findall("falls|planet", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
 