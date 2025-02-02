# Double x, and Integer n
# res = x^n

def power_of_a_number(x:float, n:int):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n > 1:
        power_of_a_number(x*x, n - 1)
    elif n < -1:
        power_of_a_number(1/x, n + 1)

print(power_of_a_number(2, 3))