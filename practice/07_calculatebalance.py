def calculateBalance(inputvalues):
    amount = 0
    values = inputvalues.split(" ")
    for x in range(0,len(values)):
        if values[x] == "D":
            amount = amount+int(values[x+1])
        elif values[x]=="W":
            amount = amount-int(values[x+1])
    print(amount)

calculateBalance("D 300 D 300 W 300 D 100")