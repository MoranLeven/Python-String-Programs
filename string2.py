#ways to remove i'th charachter from the string
def ith_index_remover(string,remove_index):
    """This function has an issue, it will not return the exact string; the returned string 
        does not have spaces ' ' in them 
        e.g.
        >>> ith_index_remover("this is a string",0)
        >>> hisisastring
        """
    if len(string)<remove_index:
        return "The index is out of range"
    new_string = ''
    string_list = list(string)
    for j,i in enumerate(string_list):
        if j!=remove_index:
            new_string +=i
    return new_string



print(ith_index_remover('My name is m11',5))
print(ith_index_remover.__doc__)

