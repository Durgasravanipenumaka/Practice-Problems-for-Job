# second largest number in alist
lst = [1, 3, 5, 7, 2]
unq = []

for i in lst:
    if i not in unq:
        unq.append(i)
unq_list = sorted(unq)
print("Second largest number is:", unq_list[-2])
