# Move all zeros to the end
lst=[1,0,2,0,4,5,0,0,5,7]
zeros=[]
non_zeros=[]
for i in lst:
    if i==0:
        zeros.append(i)
    else:
        non_zeros.append(i)
for i in zeros:
    non_zeros.append(i)
print(non_zeros)