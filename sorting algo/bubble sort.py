'''Code for bubble sort'''

# code:

l=[2,5,1,3,8,4,5,9,2]
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j+1]<l[j]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)