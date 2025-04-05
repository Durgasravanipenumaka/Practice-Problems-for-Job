# count occurence of an element in a tuple
t=(1,2,3,2,2,4)
count=0
n=int(input())
for i in t:
    if n == i:
        count += 1
print(count)