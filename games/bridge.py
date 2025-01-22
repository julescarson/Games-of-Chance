import math
from collections import Counter

# suitsInHand = 4 tuple of suits dealt to the hand (from 0 to 13)
def probabilityBridge(distribution):
    if (sum(distribution) != 13):
        return "error"
    
    # suits of same value
    numMatching = max(dict(Counter(distribution)).values()) # same suit (occurances)
    arrange = math.factorial(4)/math.factorial(numMatching)
    
    # nCk foreach suit
    dist = [math.comb(13, e) for e in distribution]
    numerator = 1
    for d in dist:
        numerator *= d
    numerator *= arrange

    # denom total ohm
    denom = math.comb(52,13)
    ans = numerator/denom 
    return ans 

bridgeHands = [
    [4, 4, 3, 2],
    [5, 3, 3, 2],
    [5, 4, 3, 1],
    [5, 4, 2, 2],
    [4, 3, 3, 3],
    [6, 3, 2, 2],
    [6, 4, 2, 1],
    [6, 3, 3, 1],
    [5, 5, 2, 1],
    [4, 4, 4, 1],
    [7, 3, 2, 1],
    [6, 4, 3, 0],
    [5, 4, 4, 0],
    [5, 5, 3, 0]
]

print("General Formula \n Numerator: (4!/ (repeatCount)!) x (13 choose suit1) x ... x (13 choose suit4)")
print(" Denominator = 52 Choose 1\n")


print("Shape        | Probability")
for hand in bridgeHands:
    print(f"{hand} | {round(probabilityBridge(hand), 4)}")


def highCardPoint():
    return 0