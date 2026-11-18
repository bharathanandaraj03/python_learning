try:
    inputvalue = int(input("Enter any value: "))

    print(f"entered value is {inputvalue}")
    if inputvalue%2 == 0:
        print("Even")
    else:   
        print("odd")
except:
    print("Enter valid number")