# find the missing number in a list
lst=[1,2,4,5,6,7,8]
for i in range(1,len(lst)+1):
    if i not in lst:
        print(i)
        break
    
