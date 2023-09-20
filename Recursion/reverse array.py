'''Problem solving for reversing an array'''

# approch 1 -- normal aproach no recursion
n=1
for i in range(len(l)//2):
    
    l[i],l[-n]=l[-n],l[i]
    n=n+1
    
print(l)


# approach2 using 2 parameter recursion
def func(l,li,r):
    if l>=r:
        return 
    li[l],li[r]=li[r],li[l]
    func(l+1,li,r-1)
    return li
    
    
    
li=[1,2,3,5,9,4,3,2,1,6]
print(func(0,li,len(li)-1))  



# approach2 using 1 parameter recursion
def func(i,li):
    n=len(li)
    if i>=n/2:
        return 
    li[i],li[n-i-1]=li[n-i-1],li[i]
    func(i+1,li)
    return li
    
li=[1,2,3,5,9,4,3,2,1,6]
print(func(0,li)) 