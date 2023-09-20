'''This code is to find the maximum element in an array/list'''

# solution
l=[1,7,8,9,11,15,18,98,107,7,8,9]
mx=l[0]
 
for i in range(1,len(l)-1):
    if l[i+1]>mx:
        mx=l[i+1]
print("the maximum element:",mx)
