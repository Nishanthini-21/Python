'''Program to print name n times using recursion'''

def funcname(i,n):
    if i>n:
        return 
    print("Nisha")
    funcname(i+1,n)

n=7
funcname(1,n)