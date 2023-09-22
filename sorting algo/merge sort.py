'''This code represents merge sort'''


# function to sort and merge the divided array from merge_sort function 

def merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1 
        else:
            c.append(b[j])
            j+=1 
    while j<len(b):
        c.append(b[j])
        j+=1 
    while i<len(a):
        c.append(a[i])
        i+=1 
    return c


# function to divide the array

def merge_sort(l):
    if len(l)==1:
        return l 
    return merge(merge_sort(l[:len(l)//2]),merge_sort(l[len(l)//2:]))



if __name__=="__main__":

    l=[5,2,3,4,1]
    print(merge_sort(l))


