
'''code for palindrome check using recursion'''

def func(i,s):
    n=len(s)
    if i>=n/2:
        return True 
    if s[i]!=s[n-i-1]:
        return False 
    return func(i+1,s)



string="madam"
print(func(0,string))