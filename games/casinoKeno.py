import math
import metrics

# casino keno pick-n, return array of probabilities for 0 to n catches
# usage example:  casinoKenoPick(3, showPrintout=True)
def probability(nPicks):
    probabilities = []
    totalChoices = 80
    draw = 20
    ohm = math.comb(totalChoices, draw)

    for catches in range(0, nPicks+1):
        subset = math.comb(nPicks, catches) * math.comb((totalChoices-nPicks), (draw-catches))
        probabilities.append(subset/ohm)

    return probabilities

def houseEdge():
    return 0