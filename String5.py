#Program to print even length words in a string
#if len(words_arr[i])&1==0 print()
def even_word_printer(string):
    #split the string with space as delimiter 
    splitted_list = string.split(" ")
    for i in splitted_list:
        if len(i) %2 == 0 and i != None:
            print(i)
    
even_word_printer("This is the coolest problemo i ever solved con mi amigo")


