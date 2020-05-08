#Count the vowels and consonants in a given string.
import re

str = input("Enter a String : ")
x = re.findall("[AaEeIiOoUu]",str)
print("Total Vowels are : ",len(x))
x = re.findall("[^AaEeIiOoUu]",str)
print("Total Consonants are : ",len(x))