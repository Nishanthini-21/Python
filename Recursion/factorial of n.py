'''code for factorial of a number using recursion'''

# code:

def factn(n):
    if n==0:
        return 1
    return n*factn(n-1)
print(factn(5))
