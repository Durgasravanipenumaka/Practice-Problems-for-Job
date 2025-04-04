# Smallest number in a list
lst=[1,3,5,7]
min_num=lst[0]
for i in lst:
    if i < min_num :
        min_num = i
print("Largest number : ",min_num)