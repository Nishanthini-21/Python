'''code for sum of n natural number using recursion'''


# approach 1
def sumn(n):
    if n==0:
        return 0
    return n+sumn(n-1)
print(sumn(5))


# approach 2
def sumofn(i,n):
    sum=0
    if i>n:
        return sum 
    sum=sum+i
    sumofn(i+1,n)


n=10
print(sumofn(1,n))