# declaring a  string variable
string1="Hello World!"
print(string1)

string2='Hello Python!'
print(string2)

string3='''Hello world'''
print(string3)








#Slicing techniques
print("Slicing Techniques:\n")
text = "HELLO"

print(text[0])  
print(text[2]) 
print(text[-1])
print(text[1:4])
print(text[1:])
print(text[:])







#string Functions:
test_string = "Hello World"
print("Test string is:", test_string)

# 1.Length of a string
print("1.length of string:",len(test_string))

# 2.lowercase of a string
print("2.lowercase of string:",test_string.lower())

# 3.uppercase of a string
print("3.uppercase of string:",test_string.upper())

# 4.Strip whitespace from the beginning and end of a string
print("4.strip whitespace:",test_string.strip())

# 5.lstrip() removes whitespace from the left side of a string
print("5.lstrip whitespace:",test_string.lstrip())

# 6.rstrip() removes whitespace from the right side of a string
print("6.rstrip whitespace:",test_string.rstrip())

# 7.replace() replaces a substring with another substring
print("7.replace substring:",test_string.replace("World","Python"))

#8.split() splits a string into a list of substrings
print("8.split string:",test_string.split())

#9.join() joins a list of strings into a single string
list_of_strings = ['Hello', 'Python', 'World']
print("9.join list of strings:", ' '.join(list_of_strings))

# 10.find() returns the index of the first occurrence of a substring
print("10.find substring index:", test_string.find("World"))

# 11.count() counts the occurrences of a substring in a string
print("11.count substring occurrences:", test_string.count("l"))

# 12.startswith() checks if a string starts with a specified substring
print("12.check if string starts with 'Hello':", test_string.startswith("Hello"))      

# 13.endswith() checks if a string ends with a specified substring
print("13.check if string ends with 'World':", test_string.endswith("World"))

# 14.capitalize() capitalizes the first character of a string
print("14.capitalize first character:", test_string.capitalize())

# 15.title() capitalizes the first character of each word in a string
print("15.capitalize first character of each word:", test_string.title())

# 16.isalpha() checks if all characters in a string are alphabetic
print("16.check if all characters are alphabetic:", test_string.isalpha())

# 17.isdigit() checks if all characters in a string are digits
print("17.check if all characters are digits:", test_string.isdigit())

# 18.isalnum() checks if all characters in a string are alphanumeric
print("18.check if all characters are alphanumeric:", test_string.isalnum())

# 19.islower() checks if all characters in a string are lowercase
print("19.check if all characters are lowercase:", test_string.islower())

# 20.isupper() checks if all characters in a string are uppercase
print("20.check if all characters are uppercase:", test_string.isupper())








#Q. write a program to build simple text analysis to the tool should perform following tasks for the inpute text::
# 1.count the total no of words 
# 2. count the total no of space 
# 3. count the frequency of each word in the input 
# 4.identify and display top 3 mostly frequent word
# 5.count the total no of vowels in the entire text
# 6.sort the string with conversion of original string into the reverse ascending order (first reverse and then ascending)

# Input text from user
text = input("Enter your text to analyse:\n")

# 1. Total number of words
words = text.split()
total_words = len(words)
print(f"\n1. Total number of words: {total_words}")

# 2. Total number of spaces
total_spaces = text.count(' ')
print(f"2. Total number of spaces: {total_spaces}")

# 3. Frequency of each word (case insensitive)
word_freq = {}
for word in words:
    word_lower = word.lower()
    if word_lower in word_freq:
        word_freq[word_lower] += 1
    else:
        word_freq[word_lower] = 1

print("3. Frequency of each word:")
for word, count in word_freq.items():
    print(f"   {word}: {count}")

# 4. Top 3 most frequent words
sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
print("\n4. Top 3 most frequent words:")
for i in range(min(3, len(sorted_freq))):
    print(f"   {sorted_freq[i][0]}: {sorted_freq[i][1]}")

# 5. Count total number of vowels in the entire text
vowels = "aeiouAEIOU"
vowel_count = 0
for char in text:
    if char in vowels:
        vowel_count += 1
print(f"\n5. Total number of vowels: {vowel_count}")

# 6. Reverse string and then sort it in ascending order
reversed_text = text[::-1]
sorted_reversed = ''.join(sorted(reversed_text))
print("\n6. Sorted reversed string (ascending after reverse):")
print(sorted_reversed)

# Output
print("\n--- Text Analysis Result ---")
print(f"1. Total number of words      : {total_words}")
print(f"2. Total number of spaces     : {total_spaces}")
print(f"3. Word frequencies           : {dict(word_freq)}")
print(f"4. Top 3 frequent words       : {top_3_words}")
print(f"5. Total number of vowels     : {vowel_count}")
print(f"6. Sorted reversed string     : {sorted_reversed_text}")







# Q2 write a program to analyse two different word files or paragraphs where u need to do following tasks :
# 1. find all unique words use in each paragraph 
# 2. identify the common words between both paragraphs 
# display the total count of unique words found in both paragraphs

# Sample input: you can use file input or direct paragraph input
para1 = input("Enter Paragraph 1:\n")
para2 = input("Enter Paragraph 2:\n")

# Function to clean and get unique words
def get_unique_words(text):
    words = text.lower().replace(".", "").replace(",", "").split()
    return set(words)

# 1. Unique words from each paragraph
unique_words_para1 = get_unique_words(para1)
unique_words_para2 = get_unique_words(para2)

# 2. Common words between both paragraphs
common_words = unique_words_para1.intersection(unique_words_para2)

# 3. Total unique words in both paragraphs (union)
total_unique_words = unique_words_para1.union(unique_words_para2)

# Output
print("\n--- Paragraph Analysis ---")
print(f"1. Unique words in Paragraph 1:\n{unique_words_para1}")
print(f"2. Unique words in Paragraph 2:\n{unique_words_para2}")
print(f"3. Common words:\n{common_words}")
print(f"4. Total count of unique words (combined): {len(total_unique_words)}")






