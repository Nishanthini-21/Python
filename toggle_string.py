'''
Question:
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet 
in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted 
to uppercase. You need to then print the resultant String to output.
Source Hackerearth

SAMPLE INPUT: 
abcdE
SAMPLE OUTPUT: 
ABCDe
'''

#solution1
def function_one(s):
    return s.swapcase()

s=input()
print(function_one(s))



#solution2
def function_one(s):
    result=""
    for char in s:
        if char.isalpha():
            if char.islower():
                char=char.upper()
                result+=char
            elif char.isupper():
                char=char.lower()
                result+=char
        else:
            result+=char
    return result
                

s=input()
print(function_one(s))



