import re

txt = "ÅThe rain in Spain falls mainly on the plain"

#Find all ASCII matches:
print(re.findall("\w", txt, re.ASCII))

#Without the flag, the example would return all character:
print(re.findall("\w", txt))

#Same result using the shorthand re.A flag:
print(re.findall("\w", txt, re.A))
print()
print(re.findall("Spain", txt, re.DEBUG))
print()

#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.IGNORECASE))

#Same result using the shorthand re.I flag:
print(re.findall("spain", txt, re.I))
print()


#Find and return words that contains the phrase "ain":

pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""

print(re.findall(pattern, txt, re.VERBOSE))

#The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, txt))


#Same result with the shorthand re.X flag:
print(re.findall(pattern, txt, re.X))
print()

txt = """Hi
my
name
is
Sally"""

#Search for a sequence that starts with "me", followed by one character, even a newline character, and continues with "is":
print(re.findall("me.is", txt, re.DOTALL))

#This example would return no match without the re.DOTALL flag:
print(re.findall("me.is", txt))

#Same result with the shorthand re.S flag:
print(re.findall("me.is", txt, re.S))
print()

#Search for the sequence "ain", at the beginning of a line:
print(re.findall("^nam", txt, re.MULTILINE))

#This example would return no matches without the re.MULTILINE flag, because the ^ character without re.MULTILINE only get a match at the very beginning of the text:
print(re.findall("^nam", txt))


#Same result with the shorthand re.M flag:
print(re.findall("^nam", txt, re.M))

print(re.findall("\w", txt, re.UNICODE))
print()

#SPECIAL SEQUENCES
print("SPECIAL SEQUENCES OUTPUT")

txt = "The rain in Spain 897 @#%"
x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match") 
  
#Check if "ain" is present, but NOT at the beginning of a word (or at the end):

x = re.findall(r"\Bain", txt)
print(x)

x = re.findall(r"ain\B", txt)
print(x)

x = re.findall(r"\bain", txt)
print(x)

x = re.findall(r"ain\b", txt)
print(x)

x = re.findall("\\d", txt)
print(x)

x = re.findall("\\D", txt)
print(x)

x = re.findall("\\s", txt)
print(x)

x = re.findall("\\S", txt)
print(x)

x = re.findall("\\w", txt)
print(x)

x = re.findall("\\W", txt)
print(x)

x = re.findall("@#%\\Z", txt)
print(x)