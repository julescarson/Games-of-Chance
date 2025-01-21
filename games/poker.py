'''
For a poker hand, face values:
 {f0, f1, f2, f3, f4} : e.g., 
 f1 = the number of face (A,2,3,...,K) cards appearing exactly once
 f2 = the number of face (A,2,3,...,K) cards appearing exactly twice ...
 f0 will always be greater than 1 since some face cards will not have been chosen

Example: {9, 9, 9, K , A} 
{(f0 = 10), (f1 = 2), (f2 = 0), (f3 = 1), (f4 = 0)}
10 face cards not shown, 
2 face cards shown a single time (A,K), 
0 face cards shown exactly twice, 
1 face card shown 3 times (9,9,9)
0 face cards shown 4 times

In general..
(f4, f3, f2, f1, f0)
(1,0,0,1,11): four of a kind, {aaaab};
(0,1,1,0,11): full house, {aaabb};
(0,1,0,2,10): three of a kind, {aaabc};
(0,0,2,1,10): two pair, {aabbc};
(0,0,1,3,10): one pair, {aabcd};
(0,0,0,5,8): five distinct face values,

*note, suits do not have a ranking, they are considered equal

'''
import math
from collections import Counter

#TODO output step calculations fully

# dict for testing - [a,b,c,d,e] as 5 distinct cards = "Lower than a pair"
handTypes = {
    '[1, 0, 0, 1, 11]': 'four of a kind',
    '[0, 1, 1, 0, 11]': 'full house',
    '[0, 1, 0, 2, 10]': 'three of a kind',
    '[0, 0, 2, 1, 10]': 'two pair',
    '[0, 0, 1, 3, 9]': 'one pair',
    '[0, 0, 0, 5, 8]': 'five distinct cards'
}

# return pr for a specific hand in decimal
def handProbability(subsetSize):
    ohm = math.comb(52,5)
    return subsetSize/ohm

# helper function for subset size calculation
def factorialList(parsedArray):
    ans = 1
    for f in parsedArray:
        ans *= math.factorial(f)
    return ans

# returns subset size for different types of hands
def numHandsOfType(cardArray, isFlush=False, isStraight=False):
    # TODO
    if (isFlush and isStraight):
        return 0
    elif (isFlush):
        return 0
    elif (isStraight):
        return 0

    #calculate set size, explicitly shown for comprehension:
    # |S| = (13! / (f4!,..f0!) ) * (4^(f3+f1)) * (6^f2)
    term1 = math.factorial(13)/factorialList(cardArray)
    term2 = 4**(cardArray[1]+cardArray[3]) # 4^(f3+f1)
    term3 = 6**cardArray[2]
    ans = term1 * term2 * term3
    return ans


# returns array in form [f4,f3,f2,f1,f0] : f4 = instances of four of a kind, .., f0 : unseen cards
def cardsToHandType(cards):
    faceValues = [0,0,0,0, 13-len(set(cards))] 
    # dict counter each element -> secondary counter, group instances  { 2 : 1 } "1 instance of 2 same face value card" 
    hand = Counter(Counter(cards).values()) 
    
    # update faceValues array
    for fCount in hand.items():
        faceValues[4-fCount[0]] = fCount[1]  
    return faceValues

# output some metrics for a specific poker hand
def poker(hand):
    #TODO: return value, parse by metrics.py functions
    parsedHand = cardsToHandType(hand)
    nameType = handTypes.get((str)(parsedHand))
    numType = numHandsOfType(parsedHand)
    prType = handProbability(numType)
    print(f"{hand} -> {parsedHand}, '{nameType}', ways: {numType}, probability: {prType} = {round(prType*100, 4)}%")    
  

#test
handsWithoutFlushes = [[2,2,2,2,4],[3,3,3,2,2],[3,3,3,2,1],[2,2,6,6,3],[1,1,4,3,5],[1,2,3,4,5]]
for e in handsWithoutFlushes:
    poker(e)


