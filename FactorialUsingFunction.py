def factorial(n):

    if n==1 or n==0:
        return 1
    else:
        return (n*factorial(n-1))

n=int(input("Enter a number:"))
result=factorial(n)
print("factorial of",n,"is:",result)