'''This code is to check whether the given array is sorted or not'''

# solution 

# l=[45,23,87,12,98,0,4]

l=[2,6,7,10,14,56,78,90]

def sorted_array(l):
    for i in range(len(l)-1):
        if l[i+1]<l[i]:
            return False
            break
    return True

print(sorted_array(l))