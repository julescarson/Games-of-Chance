from itertools import product

# all dice req to have same num faces
def waysToRollSum(numDice, desiredSum, numFaces=6, showPrintout=False):

    # is sum possible
    if not (numDice <= desiredSum <= (numDice * numFaces)):
        print(f"Invalid sum: {desiredSum}, must be between {numDice} and {numDice * numFaces}")
        return -1

    dice = range(1, numFaces + 1)
    rolls = [] # list of tuples for the set of dice

    # nested for-loop, foreach die
    for roll in product(dice, repeat=numDice):
        if (sum(roll) == desiredSum):
            rolls.append(roll)

    if showPrintout:
        print(f"Number of ways to produce {desiredSum} with {numDice} dice having {numFaces} faces: {len(rolls)}")
        print(rolls)

    return len(rolls)

