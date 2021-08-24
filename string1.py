#program to check either the given string is palindrome or not
def ispalindrome(string):
    rev_string = ''
    for i in range(len(string)-1,-1,-1):
        rev_string += string[i]
    if string == rev_string:
        return True
    else:
        return False

#reverse the words in the given string 
def words_reverse(string):
    str_lst = string.split(" ")
    
    return " ".join(reversed(str_lst))

#main function
if __name__ == "__main__":
    print()
    print(words_reverse("Por que tu usas python?"))





























