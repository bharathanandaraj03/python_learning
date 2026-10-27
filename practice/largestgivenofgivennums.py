def largest(num):
    totalitemcount = len(num)
    
    for x in range(0,totalitemcount):

        for y in range(0,totalitemcount-x-1):
            print(num[y],num[y+1])
            if num[y] > num[y+1]:
                print("Inside if:")
                print(num[y],num[y+1])
                num[y],  num[y+1]= num[y+1] , num[y]
    return num

num =  [32,45,21,55,28,68]
print(largest(num))
