'''This code represents the insertion sort mechanism'''

def insertion_sort(l):
    for i in range(1,len(l)):

        current_element=l[i]
        pos=i
        
        while current_element<l[pos-1] and pos>0:
            l[pos]=l[pos-1]
            pos=pos-1 
        l[pos]=current_element
                
    print(l)
    
    
def main():
    l=[2,4,3,1,5,6,3,8]
    insertion_sort(l)
    
    
if __name__=="__main__":
    main()
    