def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

num = int(input("Enter the nunber: "))

if num < 0:
    print("No Factorial")
elif num==0:
    print("Factorial is 0")

else:
    print("Factorial is: " , factorial(num))    
    