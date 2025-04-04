# find common elent b/w 2 lists
lst1=[1,2,3,6,4]
lst2=[5,6,7,8,9]
unq=[]
for i in lst1:
    if i in lst2:
        unq.append(i)
print(unq)