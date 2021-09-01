#Uno. How to confirm two strings have same identity 
from typing import final


b = ['letter','consonant']
x = b
assert(b == x) == True
assert(b is x) ==  True
c = ['letter','consonant']
assert(c == b) == True
#but 
assert(c is b ) == False
#why
print("ID of x",id(x))
print("ID of c",id(c))
print("ID of b",id(b))

a = [2,3,5]
b = a


#Dos. How to check if each word in string is capitalize or not
print("This doesn't contain all capital letters".istitle())
print("The Legend Of A Legend".istitle())


#Tres. Check if string contain specific character or not
specific_character = '😎'
string = "This string contains the specific character % 😎"
print(specific_character in string)

#Cuatro. Find the index of first occurrence of a substring in a string
print("This contain substring".find('This'))
try:
    #remember the index() will pop ValueError if it is unable to find the substring in the string. Google it 🔎🔎
    print("This doesn't  contain the substing".index("this"))
except ValueError:
    print("NO substring named this")

