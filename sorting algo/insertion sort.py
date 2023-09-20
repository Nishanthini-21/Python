'''This code represents the insertion sort mechanism'''

l=[2,6,1,7,4,9]
for i in range(1,len(l)):
    current_value=l[i]
    pos=i 
    while current_value<l[pos-1] and pos>0:
        l[pos]=l[pos-1]
        pos=pos-1
    l[pos]=current_value 
print(l)