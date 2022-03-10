#creating the factorial function
def factorial(n):
    if n==0 or n==1:
        return 1 
    return n*(factorial(n-1))
    
#Calling the function 
print(factorial(4))
