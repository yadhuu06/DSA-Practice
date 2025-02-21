# reverse a string using recursion

def reverse_str(s):
    if len(s)<=1:
        return s 
    return s[-1]+reverse_str(s[:-1])

s= "hello"
print(reverse_str(s))
