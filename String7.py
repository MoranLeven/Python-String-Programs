#program to capitalize first and last letter of the string
#this problem is simple just use first index and last index thatall
def uno_y_ultimo(string: str)-> str:
    empty = ''
    for j,i in enumerate(string):
        if j == 0:
            empty += i.upper()
        elif j == (len(string)-1):
            empty += i.upper()
        else:    
            empty += i
        
    return empty

print(uno_y_ultimo("moran"))

