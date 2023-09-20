'''This code is to find the count of distinct element in array'''

l = [1,7,8,9,117,7,9,11,2,6,15,7,8,9]
i = 0
for j in range(1, len(l)):
    if l[j] not in l[:i+1]:
        i = i + 1
        l[i] = l[j]

unique_count = i + 1

print("Number of unique elements:", unique_count)
print("dictinct array:",l[:unique_count])