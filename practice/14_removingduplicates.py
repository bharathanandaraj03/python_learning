list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

#print(list(set(list2)-set(list1)))
#finding insersection
#print(list(set(list2)&set(list1)))

duplicatelist = "this is a duplicate sentence this is a"
iteratelist = duplicatelist.split()
for word in iteratelist:
    print(f"{word} {duplicatelist.count(word)}")
    if duplicatelist.count(word) > 1:
        duplicatelist = duplicatelist.replace(word,"")
print(duplicatelist)

#To Remove duplicate chars
duplicatechars = "asdddddasfddsaddrgewqeeqwexyz"

for i in duplicatechars:
    if duplicatechars.count(i) > 1 :
        duplicatechars = duplicatechars.replace(i,"")
print(duplicatechars)