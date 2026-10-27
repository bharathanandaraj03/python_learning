def numdiv7not5():
    startRange = 2000
    endRange = 3200

    l=[]
    print("Number Divisble by 7 not by 5")

    for i in range(startRange,endRange):
        if((i%7==0) and (i%5!=0)):
            l.append(str(i))
    print(".".join(l))