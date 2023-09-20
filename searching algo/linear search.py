'''this is the code for linear search algorithm'''

pos=-1
l=[1,8,4,6,9,3,10]
key=4


def linear_search(l):
    found=False
    for i in range(len(l)):
        if l[i]==4:
            global pos  #To change the global variable value inside the function.
            pos=i
            found=True
            break
    return found 

print(linear_search(l)) 
print("found at index position",pos) 