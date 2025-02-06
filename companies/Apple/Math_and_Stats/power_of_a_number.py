# Double x, and Integer n
# res = x^n

def myPow(x:float, n:int):
    if n == 0:
        return 1 # Base case: x^0 = 1

    if n < 0:
        x = 1/x # Handle negative exponent
        n = -n

    # Recursively calculate power
    half = myPow(x, n // 2) # Compute x^(n//2) once

    # If n is even, return half * half
    if n%2 == 0:
        return half * half
    else:
        return half * half * x # If n is odd, multiply extra x 

print(myPow(2, -3))
