'''This code provides with fibonacci series with recursion function'''


# code:

def f(n):   #function declaration
    if n<=1:
        return n
    return f(n-1)+f(n-2) #multiple function calls


n=3
print(f(n))  #function call