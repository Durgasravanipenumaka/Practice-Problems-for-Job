# count occurence of a element
lst=[3,5,4,3,2,3]
count=0
element=int(input())
for i in lst:
    if i == element:
         count=count+1
print(count)