'''
Given two strings, A and B.
A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. 
Return True if and only if A can become B after some number of shifts on A.
    :type A: str
    :type B: str
    :rtype : bool
'''    
#solution1
def function_one(s1,s2):
    combined=s1+s1
    if s2 in combined:
        print(True)
    else:
        print(False)
    

s1=input()
s2=input()
function_one(s1,s2)



#solution2
def function_one(s1,s2):
    if len(s1)!=len(s2):
        return False

    for i in range(len(s1)):
        if s1==s2:
            return True
        
        s1 = s1[1:]+s1[0]
    return False


s1=input()
s2=input()
print(function_one(s1,s2))


