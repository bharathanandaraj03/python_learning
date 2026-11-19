input = [1,2,3,4]
output = []

for i in range(len(input)):
    currnum = input[i]
    product = 1
    for j in range(len(input)):
        if currnum != input[j]:
            product = product * input[j]
    output.append(product)
print(output)

