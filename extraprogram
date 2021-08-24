def balanced_string_counter(string="LRRRRLLRLLRL"):
    n = len(string)
    if n==0:
        return 0
    r = 0 #it will represent right 
    sub_str = ""
    l = 0 #it will represent left
    ans = 0 # the total no. of equal lr substrings in the main string
    for i in range(n):
        if(string[i]=='R'):
            r+=1
            sub_str+=string[i]
        elif string[i]=='L':
            l+=1
            sub_str+=string[i]
        if r==l:
            if i<n-1:
                print(sub_str,end=", ")
                ans+=1
                sub_str = ""
                l=0
                r=0
            else:
                print(sub_str)
                ans+=1
                sub_str = ""
                l=0
                r=0
    return ans

if __name__ == '__main__':
    print(balanced_string_counter())
