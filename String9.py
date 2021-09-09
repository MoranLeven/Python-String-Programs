def accept_only_vowels(string):
    str =list(set(string.lower()))
    for i in str:
        if 'a' in str and 'e' in str and 'i' in str and 'o' in str and 'u' in str:
            return f"String Accepted"
        else:
            return f"String Forbidden"

print(accept_only_vowels("AeioxkjlkfuuUUjsdlkfj"))

#using intersection cool way

def accept_only_vowels_2(string):
    if len(set(string.lower()).intersection('aeiou')) >= 5:
        return f"[+] String Accepted"
    else:
        return f"[-] String Forbidden"

print(accept_only_vowels_2("djfl"))



