set1={1,5,3,4,2}
pairs=set()
for i in set1 :
    for j in set1 :
        if (i-j) == 2:
            pairs.add((j,i))
print(pairs)