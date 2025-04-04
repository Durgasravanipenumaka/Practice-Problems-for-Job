# check palindrome or not
lst=[2,4,5,5,4,2]
is_palindrome=True
for i in range(0,len(lst)//2):
    if lst[i] != lst[-(i+1)]:
        is_palindrome=False
        break
print(is_palindrome)