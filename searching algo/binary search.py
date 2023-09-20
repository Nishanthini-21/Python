
'''This is a binary search algorithm'''

# NOTE: It is necessary for binary search algorithm to sort the array before the process.

# code

def binary_search(li,key):

    l=0
    h=len(li)-1
    found=False
    while l<=h and not found:
        mid=(l+h)//2
        if key==li[mid]:
            found=True 
        else:
            if key>li[mid]:
                l=mid+1
            else:
                h=mid-1 
    return found



li=[1,4,6,7,3,2,9,10]
key=9

li.sort()
print(binary_search(li,key))







