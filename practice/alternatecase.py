input = "hello world"

def alternatecase(input):
    flgreset = 0

    for x in input:
        if flgreset ==0:
            print(x.upper(),end="")

            flgreset=1
        else:
            print(x.lower(),end="")
            flgreset=0

def alphabetpostion(input):
    values = {"A":1, "B":2}
    print(values.get("B"))