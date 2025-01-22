import math

# Total number of 5-card combinations in a 52-card deck
totalCombos = math.comb(52, 5)

def generateLatex(handType):
    """
    Generate LaTeX formatted string for each hand type's calculations.
    """
    latexCode = ""

    if handType == "Royal Flush":
        # 4 suits, each has exactly one royal flush (A, K, Q, J, 10 of the same suit)
        subsetSize = 4  # 1 royal flush for each suit
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 4 \quad \\text{{(1 Royal Flush per suit)}}
\\]
"""

    elif handType == "Straight Flush":
        # 9 possible straight flushes per suit (excluding the Royal Flush)
        # 10 possible starting points for the straight (A-5, 2-6, ..., 10-K)
        subsetSize = 9 * 4  # 9 possible straights per suit, 4 suits
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 9 \\times 4 = 36 \quad \\text{{(9 possible straights per suit, 4 suits)}}
\\]
"""

    elif handType == "Four of a Kind":
        # Choose 1 rank out of 13 for the four of a kind (13 choices)
        # Choose the 5th card from 48 remaining cards (not the 4 of a kind)
        subsetSize = 13 * math.comb(48, 1)  # 13 ranks, 48 options for the 5th card
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 13 \\times \\binom{{48}}{{1}} = {13 * math.comb(48, 1)} \quad \\text{{(13 ranks, 48 options for the 5th card)}}
\\]
"""

    elif handType == "Full House":
        # Choose 1 rank for three of a kind (13 options)
        # Choose 1 rank for a pair from remaining 12 ranks (12 options)
        # Choose 2 suits for the three of a kind (4 choose 3)
        # Choose 2 suits for the pair (4 choose 2)
        subsetSize = 13 * math.comb(4, 3) * 12 * math.comb(4, 2)
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 13 \\times \\binom{{4}}{{3}} \\times 12 \\times \\binom{{4}}{{2}} = {subsetSize} \quad \\text{{(13 ranks for 3-of-a-kind, 12 ranks for pair)}}
\\]
"""

    elif handType == "Flush":
        # Choose 1 suit out of 4 (4 choices)
        # Choose 5 cards from the 13 cards in that suit (13 choose 5)
        # Subtract the number of straight flushes (calculated separately)
        flushSubset = 4 * math.comb(13, 5)
        straightFlushes = 36  # Already known, 9 per suit, 4 suits
        subsetSize = flushSubset - straightFlushes
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 4 \\times \\binom{{13}}{{5}} - 36 = {subsetSize} \quad \\text{{(4 suits, 5 cards from each suit, minus straight flushes)}}
\\]
"""

    elif handType == "Straight":
        # 10 possible starting points for a straight (A-5, 2-6, ..., 10-K)
        # Choose 5 cards from the 10 consecutive ranks
        # Exclude straight flushes, already calculated
        straightSubset = 10 * math.comb(4, 1)**5
        straightFlushes = 36  # Already known
        subsetSize = straightSubset - straightFlushes
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 10 \\times \\binom{{4}}{{1}}^5 - 36 = {subsetSize} \quad \\text{{(10 starting points, suits for each card, minus straight flushes)}}
\\]
"""

    elif handType == "Three of a Kind":
        # Choose 1 rank for three of a kind (13 choices)
        # Choose 2 ranks for the other two cards (12 choose 2)
        # Choose 1 suit for each of the two remaining cards (4 choose 1)
        subsetSize = 13 * math.comb(4, 3) * math.comb(12, 2) * math.comb(4, 1)**2
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 13 \\times \\binom{{4}}{{3}} \\times \\binom{{12}}{{2}} \\times \\binom{{4}}{{1}}^2 = {subsetSize} \quad \\text{{(13 ranks for trips, suits for 2 cards)}}
\\]
"""

    elif handType == "Two Pair":
        # Choose 2 ranks for pairs (13 choose 2)
        # Choose 1 rank for the 5th card (11 choices)
        # Choose 2 suits for each pair (4 choose 2)
        # Choose 1 suit for the 5th card (4 choices)
        subsetSize = math.comb(13, 2) * math.comb(4, 2)**2 * math.comb(11, 1) * math.comb(4, 1)
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = \\binom{{13}}{{2}} \\times \\binom{{4}}{{2}}^2 \\times \\binom{{11}}{{1}} \\times \\binom{{4}}{{1}} = {subsetSize} \quad \\text{{(13 ranks for 2 pairs, suits for pairs)}}
\\]
"""

    elif handType == "One Pair":
        # Choose 1 rank for the pair (13 choices)
        # Choose 3 ranks for the other cards (12 choose 3)
        # Choose 2 suits for the pair (4 choose 2)
        # Choose 1 suit for each of the other 3 cards (4 choices for each)
        subsetSize = 13 * math.comb(4, 2) * math.comb(12, 3) * math.comb(4, 1)**3
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = 13 \\times \\binom{{4}}{{2}} \\times \\binom{{12}}{{3}} \\times \\binom{{4}}{{1}}^3 = {subsetSize} \quad \\text{{(13 ranks for pair, 12 ranks for other 3 cards)}}
\\]
"""

    elif handType == "High Card":
        # Total number of hands - sum of all other hand types
        highCardSubset = totalCombos
        nonHighCardSubsets = sum([4, 36, 624, 3744, 5108, 10200, 54912, 123552, 1098240])
        subsetSize = highCardSubset - nonHighCardSubsets
        latexCode = f"""
\\section*{{{handType}}}
The subset size for a {handType} is calculated as follows:
\\[
\\text{{Subset size}} = {totalCombos} - \\left(4 + 36 + 624 + 3744 + 5108 + 10200 + 54912 + 123552 + 1098240\\right) = {subsetSize}
\\]
"""

    return latexCode


def writeLatex(handTypes, filename="pokerHands.tex"):
    """
    Write the LaTeX formatted output to a .tex file.
    """
    with open(filename, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage{amsmath}\n")
        # Manually set the margins
        f.write("\\setlength{\\oddsidemargin}{0in}\n")
        f.write("\\setlength{\\evensidemargin}{0in}\n")
        f.write("\\setlength{\\topmargin}{-0.5in}\n")
        f.write("\\setlength{\\textwidth}{6.5in}\n")
        f.write("\\setlength{\\textheight}{9in}\n")
        f.write("\\begin{document}\n")
        f.write("\\title{Poker Hand Calculations}\n")
        f.write("\\maketitle\n")

        for handType in handTypes:
            f.write(generateLatex(handType))
            f.write("\n")

        f.write("\\end{document}\n")


# Example usage
handTypes = [
    "Royal Flush",
    "Straight Flush",
    "Four of a Kind",
    "Full House",
    "Flush",
    "Straight",
    "Three of a Kind",
    "Two Pair",
    "One Pair",
    "High Card"
]

writeLatex(handTypes)
print("LaTeX file has been generated as pokerHands.tex")
