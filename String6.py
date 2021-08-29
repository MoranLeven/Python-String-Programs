#uppercase half string
def half_str_to_uppercase(string : str)-> str:
    halfstrlen = len(string)//2
    res = ''
    for j,i in enumerate(string):
        if j>=halfstrlen:
            res += i.upper()
        else:
            res += i
    return res
print(half_str_to_uppercase("ab"))


#way 2nd
#this one is tricky ok no worry leme explain it
#here i used join() function along list comprehension that is it
'''
lets break it down
we used list comprehension which will check either the index i is greater than the len(string)//2 or greater than the half of len(string)😂 --Actually both mean same--
if true then string[i].upper() which will return the capital/uppercase of i'th indexed letter of sting 
if false then return string[i] no uppercase 
and finally the join function joins all letters of our list
e.g.
>>> string = 'abcd'
>>> [string[i] if i>=len(string)//2 else string[i] for i in string]
#code above will return ['a','b','C','D]
>>> "".join(['a','b','C','D])
>>> 'abCD'
Go DI now --Do It--
'''
def half_str_to_uppercase_2(string):
    res = "".join([string[i].upper() if i>=len(string)//2 else string[i] for i in range(len(string))])
    return res
print(half_str_to_uppercase_2("this is a string"))