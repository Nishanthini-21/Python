'''this code is to find the second largest element in list without sorting method'''

# solution


l=[1,7,8,9,11,15,18,98,107,7,8,9]
mx=l[0]
 
for i in range(1,len(l)-1):
    if l[i+1]>mx:
        mx=l[i+1]



second_mx=-1
for i in l:
    if i>second_mx and i!=mx:
        second_mx=i 
print("Second largest element of the list is",second_mx)
