#calculate the length of string avoiding the spaces in it
#function no. 1

def string_len_cal(string : str) -> str:
    counter = 0
    for i in string:
        if i != " ":
            counter+=1
    return counter


print(string_len_cal('         a           b                  c           '))

#function no. 2
def string_len_cal_2(string : str) -> str:
    return sum(not ch.isspace() for ch in string)
print(string_len_cal_2("a b b"))

#function no. 3
#this one is tricky, heed it dude

'''no worry I'll break it down 
here we are using 4 functions sum, map, len and split
>>> sum(map(len, "m11 11m".split))
>>> "m11 11m".split == ['m11','11m']
>>> map(len, ['m11','11m']) # if your are using python interpreter to look under the hood, map() will return a generator and if you want to print it will print ⚠<map object at 0x00000221D1DF0F10>⚠ <-- something like this 
>>> don't cry just use simple trick use list comprehension e.g [i for i in map(len, ['m11','11m'])], it will prompt something intelligible means easy to grok
>>> eventually sum([3,3]) 
>>> 6 
>>> Remember to break down the problem 
'''
def string_len_cal_3(string: str)-> str:
    return sum(map(len, string.split()))
print(string_len_cal_3("m11 11m"))


