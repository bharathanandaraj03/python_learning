print('To print sequence 100 10 90 20 80 30 inputs 100,10')

value1 = 100
value2 = 10
temp = value2
if (value2 < value1):
    print("Sequencing")
    
    while value1 > value2:
        print(value1,value2,"")
        value1 -= temp
        value2 += temp
else:
    print("Value 2 should be less than value 1")

high = 100
low = 10
step = low

while high > low:
    print(high, low, end=" ")
    high -= step
    low += step