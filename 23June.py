#1) WAP to take 5 numbers from the user and store them in a list. Print the maximum and minimum number from the list.

'''print("Enter 5 numbers:")
numbers = [] #create an empty list to store the numbers
for i in range(5):
    num = float(input(f"Number {i+1}: "))
    numbers.append(num) #appending the input numbers to the list

max_num = max(numbers) #calling the max() function to find the maximum number in the list
min_num = min(numbers)  #calling the min() function to find the minimum number in the list
print(f"The maximum number is: {max_num}")
print(f"The minimum number is: {min_num}")
'''

#2) Create a fucntion is_palindrome(word)that returns True if the given word is a palindrome and False otherwise. A palindrome is a word that reads the same backward as forward.
'''
def is_palindrome(word):
    word = word.lower() #to lowercase thw word.
    return word == word[::-1] #[start : stop : Increment/decerement]
print(is_palindrome("Radar") )#True
'''
#3) Take a sentence as input and count: total words, total vowels, total consonants. 
'''
print("Enter a sentence:")
sentence = [input()] #taking input from the user
words = sentence[0].split() #splitting the sentence into words. split() method splits the string into a list of words based on whitespace.
totalWords = len(words)

vowelsCount = 0
consonantsCount = 0
vowels = "aeiouAEIOU"

for char in sentence[0]:  #loops through characters
  if char.isalpha():
    if char in vowels:
        vowelsCount += 1
    else:
        consonantsCount += 1
        
print("Total words:", totalWords)
print("Total vowels:", vowelsCount)
print("Total consonants:", consonantsCount)
'''