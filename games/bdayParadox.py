import math

def probability(n, total=365):
    return 1-(math.factorial(total) / ((total**n) * (math.factorial(total - n))))


