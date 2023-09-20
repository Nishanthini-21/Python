'''Code for selection sort'''

# code:

l=[2,5,1,3,8,4,5,9,2]
for j in range(len(l)):
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            l[i],l[i+1],l[i],l[i+1]
print(l)
