# Double x, and Integer n
# res = x^n

def power_of_a_number(x:float, n:int):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power_of_a_number(x, -n)
    elif n % 2 == 0:
        half_power = power_of_a_number(x, n // 2)
        return half_power * half_power
    else:
        return x * power_of_a_number(x, n-1)

print(power_of_a_number(2, -3))