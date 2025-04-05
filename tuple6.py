# Tuple Filtering:  
# Given t = (15, 28, 30, 42, 50, 65, 70), remove all numbers that are not divisible by 5 and return a new tuple.
t = (15, 28, 30, 42, 50, 65, 70)
s=()
for i in t:
    if i % 5 == 0 :
        s += (i,)
print(s)