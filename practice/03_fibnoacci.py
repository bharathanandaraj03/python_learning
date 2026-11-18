def fibonacci(n):
    output = []

    output.append(0)
    output.append(1)
    
    for i in range(1,n):
        #if(i!=1):
            output.append(output[i-1]+output[i])
    print(output)

fibonacci(7)