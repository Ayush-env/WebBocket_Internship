#String

s = "It means a loop inside another loop, it is useful when we have" \
"multidimensional data like matrices. "
# print(s[1])
# print(s[1:10])#1 to 10
# print(s[10:])#from 10 to end
# print(s[:10])#0 to 10
# print(s[:])#everything
# print(s[-10])#accesses the 10th character from the END of the string
# print(s[-10:])#accesses the last 10 characters of the string


s2 = "It means a loop inside another loop, it is useful when we have"
# print(s+s2)
# print(s*3)#repeats the string 3 times
# print(len(s))#tells the length of the string
#print(s.upper())#converts the string to uppercase
#print(s.lower())#converts the string to lowercase
#print(s.split())#splits the string into a list of words based on whitespace
#print(s.split(","))#splits the string into a list of substrings based on the comma delimiter
print(s.replace("loop","for loop"))#replaces all occurrences of "loop" with "for loop" in the string
print(s.find("loop"))#returns the index of the first occurrence of "loop" in the string, or -1 if it is not found
print(s.count("loop"))#returns the number of occurrences of "loop" in the string
print(s.startswith("It"))#returns True if the string starts with "It", otherwise False
print(s.endswith("have"))#returns True if the string ends with "have", otherwise False
print(s.isalpha())#returns True if all characters in the string are alphabetic, otherwise False
print(s.isdigit())#returns True if all characters in the string are digits, otherwise False
print(s.isalnum())#returns True if all characters in the string are alphanumeric (letters and digits), otherwise False
print(s.strip())#removes leading and trailing whitespace from the string
print(s.center(100))#centers the string within a field of a specified width (100 in this case)
print(s.ljust(100))#left-justifies the string within a field of a specified width (100 in this case)
print(s.rjust(100))#right-justifies the string within a field of a specified width (100 in this case)
print(s.zfill(100))#pads the string with zeros on the left to fill a specified width (100 in this case)
print(s.capitalize())#capitalizes the first character of the string and converts the rest to lowercase
print(s.title())#capitalizes the first character of each word in the string
print(s.swapcase())#swaps the case of each character in the string (uppercase to lowercase and vice versa)
print(s.isupper())#returns True if all characters in the string are uppercase, otherwise False
print(s.islower())#returns True if all characters in the string are lowercase, otherwise False
print(s.isnumeric())#returns True if all characters in the string are numeric, otherwise False
print(s.isdecimal())#returns True if all characters in the string are decimal characters, otherwise False
print(s.isidentifier())#returns True if the string is a valid identifier (can be used as a variable name), otherwise False
print(s.isprintable())#returns True if all characters in the string are printable, otherwise False
print(s.isascii())#returns True if all characters in the string are ASCII characters, otherwise False
