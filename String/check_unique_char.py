'''Question: You are given a string S, check if all characters are unique.

sample input and output:
----------------------------
input1:
abcd
output1:
True
---------------------------- 
input2:
abbcd
output:
False
----------------------------
'''

#solution
def function_one(s):
    d={}
    for i in s:
        if i in d:
            return False 
        else:
            d[i]=True
    return True        

s=input()
print(function_one(s))



