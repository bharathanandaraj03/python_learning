def factorial(x):
    temp = 1
    i=1
    for i in range(1,x+1): 
        temp = temp*i
    print(f"Factorial of give number is : {temp}")

factorial(int(input("Enter input to calculate factorial:")))