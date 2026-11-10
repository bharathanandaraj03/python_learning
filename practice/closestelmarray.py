a = [2,4,7,21,55]
output = []

def solution(a):
    for item in a :
        #print(item)
        #item = 4
        sum = 0
        for x in range(0,len(a)) :
            #print(a[x])
            sum = sum + abs(a[x] - item)
            #print(sum)
            #abs(2-2) + abs (4-2)
        output.append(sum)
    #print(output)


    for i in range(len(output)):
        if i == 0:
            lowest = output[i]
        if lowest >= output[i]:
            lowest = output[i]
    #print(lowest)

    #print(output.index(lowest))
    
    return a[output.index(lowest)]

def solution2(a):

    indexOfMinimum = -1
    minimalSum = float('inf')

    for i in range(len(a)):
        curSum = 0
        for j in range(len(a)):
            curSum += abs(a[j] - a[i])
        if curSum < minimalSum:
            minimalSum = curSum
            indexOfMinimum = i

    return a[indexOfMinimum]

print(f"Closet number is:  {solution2(a)}")

N = 5
def pyramid(N):
    for i in range(N):        
        for j in range(N-i-1):
            print(" ",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
pyramid(N)
