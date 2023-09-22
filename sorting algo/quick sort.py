'''This code presents quick sort'''


# code:

def partition(a,low,high):
    pivot=a[high]
    item=low-1
    for i in range(low,high):
        if a[i]<=pivot:
            item=item+1 
            a[i],a[item]=a[item],a[i]
    a[high],a[item+1]=a[item+1],a[high]
    return item+1 
    
    
def quick(a,low,high):
    if low<high:
        part=partition(a,low,high)
        quick(a,low,part-1)
        quick(a,part+1,high)
    return a



l=[2,3,1,8,6,89,5,6,3,3,4]        
print(quick(l,0,len(l)-1)) 