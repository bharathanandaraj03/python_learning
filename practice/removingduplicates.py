list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

print(list(set(list2)-set(list1)))
#finding insersection
print(list(set(list2)&set(list1)))