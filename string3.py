#find length of string in python
# four ways to solve the problemo
#way uno
def strlen(string : str)-> str:
    return len(string)
#way dos
def strlen2(string: str) -> str:
    string_length = 0
    for i in string:
        string_length+=1
    return string_length
    
#way tres
#this one is bit tricky using while loop and slicing
def strlen3(string):
    str_count = 0
    while string[str_count:]:
        str_count+=1
    return str_count


#way cuatro
#this is super tricky so grok it carefully
#how this work
#here we use "".join() method
'''Lets suppose our string is "python"
now we shall use join() method and join a random letter or stiring to it
>>> "x".join("python")
>>> "pxyxtxhxoxn"
it add a 'x' after every letter of the string except last one
now you can guess how this method is working😂 if not don't worry
count() method counts the occurrence of character in the string now we shall pass our random string to it,
it will count total no of random string in the new string
[!] Note, the no. of random string is 1 less than the total character in our string, coz it don't append after last character🧠🧠
and we will add +1 after count method
[!] this method won't work with empty string so use if -- else as shown in code below
[!] its better to create a random str variable and insted of passing string to function explicitly -- ok, lots of jargon it simply means use a don't pass string to "sdkf".join() insted use ran_str.join() and count(ran_str)
[!] if you are using the way mentioned below, remember to use same random string with join and count, don't use different string, u better know y😋, if not then lello de otra vez --google it 
'''
def findLen(string):
    if not string:
        return 0
    else:
        #ran_str = 'x'
        return ("j").join(string).count("j")+1
print(findLen('M11'))
