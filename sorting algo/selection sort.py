'''Code for selection sort'''

# code:

def selection_sort(l):
    for i in range(len(l)):
        min_index=i
        for j in range(i,len(l)):
            if l[j]<l[min_index]:
                min_index=j 
        l[min_index],l[i]=l[i],l[min_index]  
    print(l)
    
    
def main():
    l=[2,4,3,1,5,6,3,8]
    selection_sort(l)
    
    
if __name__=="__main__":
    main()
    
    

