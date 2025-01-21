import metrics
import games
import casinoKeno

# -- Example 1: casino keno pick-3 --
# setup [probabilities (calculated), and payoffs (based on odds given)]
probabilities = games.casinoKenoPick(3, True) # ex for specific game
houseNet = [1,0,-1,-15] # based on odds

pr = casinoKeno.probability(3)
print(pr)

# metric calculations & output (set showPrintout=True or False)
houseEdge = metrics.houseEdge(probabilities, houseNet, showPrintout=False)
variance = metrics.variance(probabilities, houseNet, houseEdge, showPrintout=False)
stdDev = metrics.stdDev(variance, showPrintout=False)

#  -- Example 2: sum-7 bet on 3 dice -- 
# setup
# s7 = games.threeDice(sum=7, showPrintout=False)
# ohm = 6**3
# pr_s7 = [1-(s7/ohm) , s7/ohm] # pr0: Casino Win, pr1: Casino Lose
# hn_s7 = [1,-12] # odds 12-to-1, can think of as housenet here

# # metric calculations & output
# print(f"Three dice roll for sum 7, 12-to-1 odds: ")
# s7HE = metrics.houseEdge(pr_s7, hn_s7, showPrintout=True)
# s7Var = metrics.variance(pr_s7, hn_s7, s7HE, showPrintout=True)
# s7stdDev = metrics.stdDev(s7Var, showPrintout=True)


# # bet sum 12 
# sum12 = games.threeDice(sum=12, showPrintout=False)
# ohm = 6**3
# pr12 = [1-(sum12/ohm), sum12/ohm]
# h12 = [1, -6]
# sum12HE = metrics.houseEdge(pr12, h12, showPrintout=True)

