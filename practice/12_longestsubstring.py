value = "abcabcbb"
n = len(value)
output = ""

for i in range(n):
    compchar = value[i]
    print(f"compchar: {compchar}")

    for j in range(i+1,n):

        if compchar ==value[j]:
            print(j)
            output = value[i::j]
            print(output)
            break
    
    #print(output)