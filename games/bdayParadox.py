import math

def prTwoSame(n, total=365):
    return 1-(math.factorial(total) / ((total**n) * (math.factorial(total - n))))

print (prTwoSame(23))