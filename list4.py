# remove duplicates from a list
lst=[1,3,5,7,4,5,7]
unq=[]
for i in lst:
    if i not in unq:
        unq.append(i)
print(unq)