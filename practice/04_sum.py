input = "4 5 10 20"

input = input.split(" ")

sum = 0 

for i in range(len(input)):
    sum = sum + int(input[i])

print(f"output: {sum}")

input2 = "aabccccaaadd"
input2 = list(input2)
count = 1
tempchar = input2[0]
print(len(input2))

for i in input2[1:]:

    #print(tempchar, input2[i])
    if tempchar == i:
        count += 1
        #print(f"if {tempchar},{count}")
    else:
        print(f"{tempchar},{count}")
        tempchar = i
        count = 1
print(f"{tempchar},{count}")     

