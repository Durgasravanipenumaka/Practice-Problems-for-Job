# Index of a number in a list
lst = [1, 2, 3, 4, 5]
m = int(input())
if m in lst:
    print(lst.index(m))
else:
    print("Number not in the list")
