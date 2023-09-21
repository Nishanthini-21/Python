'''Code for bubble sort'''

# code:

def bubble_sort(l):
    for i in range(len(l)):

        for j in range(len(l)-1):
            
            if l[j]>l[j+1]:
                
                l[j+1],l[j]=l[j],l[j+1] 
                
    print(l)
    
    
def main():
    l=[2,4,3,1,5,6,3,8]
    bubble_sort(l)
    
    
if __name__=="__main__":
    main()