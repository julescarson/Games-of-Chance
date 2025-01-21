# poker, roulette, casino-keno, bridge, Sic Bo, ...
import math

def nCk(n, k):
    return math.comb(n, k) # useful for importing

# casino keno pick-n, return array of probabilities for 0 to n catches
# usage example:  casinoKenoPick(3, showPrintout=True)
def casinoKenoPick(nPicks, showPrintout):
    probabilities = []
    totalChoices = 80
    draw = 20
    ohm = math.comb(totalChoices, draw)

    for catches in range(0, nPicks+1):
        subset = math.comb(nPicks, catches) * math.comb((totalChoices-nPicks), (draw-catches))
        probabilities.append(subset/ohm)
    
    if (showPrintout):
        print(f"Probabilities for Casino Keno pick-{nPicks}: {probabilities}")

    return probabilities

# set from 3..18 to find num ways to produce such sum 
# could refactor for arbitrary num dice
def threeDice(sum, showPrintout):
    totalCount = 0
    dice = [1,2,3,4,5,6]
    diceRolls = [] # for testing

    if sum >= 3 and sum <=18:
        for d1 in dice:
            for d2 in dice:
                for d3 in dice:
                    if (d1 + d2 + d3) == sum:
                        totalCount += 1
                        diceRolls.append((d1,d2,d3))
    else:
        print(f"Invalid sum : {sum}, must be from 3 to 18")
    if (showPrintout):
        print(f"Number of ways to produce {sum} : {totalCount}")
        print(diceRolls)
    return totalCount

def poker(cards, decks, hand, showPrintout):
    probabilities = []
    return probabilities

def sicBo():
    probabilities = []
    return probabilities