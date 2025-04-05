# Tuple Comprehension Alternative:  
# Since tuple comprehension doesn’t exist, write a one-liner to generate a tuple of squares from 1 to 10.
s=()
for i in range(1,11,+1):
    s+=(i**2,)
print(s)
