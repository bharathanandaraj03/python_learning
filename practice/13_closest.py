def closest(n,m):
    for i in range(n,1,-1):
        print(i)
        if m==0 :
            print("Values is zero")
        elif n <= m: 
            print("n is less than or equal m")
        elif i%m == 0:
            print(f"Closest: {i}")
            break

def can_type(key,word):
    try:
        key = str(key)
    
        for x in word:
            #print(x)
            if key.find(x)==-1:
                print(f"{x} Not present")
    except:
        raise Exception
can_type("abc","cbg")
closest(265,5)

#Reverse string
new = "12345"
print(new[::-1])
            
