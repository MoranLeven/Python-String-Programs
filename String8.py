#Program to check either string contain at least one letter and one number / or to check either string is alphanumerical or not.

def is_alphanumerical(string : str) -> str:
    num = [str(i) for i in range(0,10)]
    has_letter = False
    has_numbers = False
    for i in string:
        if i not in num:
            has_letter = True
        elif i in num :
            has_numbers = True
        if has_numbers and has_letter:
            return True
    else:
        return False

print(is_alphanumerical("0a"))
            