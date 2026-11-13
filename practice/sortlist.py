num = [11,5,10,7,8,12]
rvnum=[]
small = float('inf') 
num.reverse()
#print(num)
def selectionsort():
    for i in range(len(num)):
        minindex = i
        for j in range(i+1,len(num)):

            if num[j] <= num[minindex]:
                minindex = j

        num[i],num[minindex] = num[minindex],num[i]

l1 = [2,5,3]
l2 = [4,6,9]

n = len(l1)

num1 = ""
num2 = ""
for x in range(n):
    num1 = str(l1[x])+num1
    num2 = str(l2[x])+num2

sum = int(num1)+int(num2)
print(str(sum)[::-1])
