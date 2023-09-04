'''
Question:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M and their values are 1,5,10,50,100,500,1000 respectively.
Given a roman numeral,convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input : 'XI'
Output : 11

Example 2:
Input : 'CCCXL'
Output : 340
'''

#solution
def function_one(s):
    d={'I':1,'V':5,"X":10,'C':100,'L':50,'M':1000}
    sum=0
    previous_value=0
    for i in s[::-1]:
        value=d[i]
        if value>previous_value:
            sum=sum+value 
        else:
            sum=sum-value
        previous_value=value    
    print(sum)    
    
s=input()
function_one(s)
