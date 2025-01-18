def houseEdge(probabilities, houseNet, showPrintout):
    if (len(houseNet) != len(probabilities)):
        print(f"Check for missing values in input arrays \n Probabilities:{probabilities}, House Net: {houseNet}")
        return
    else:
        ans = 0
        display = ""
        for i in range(len(probabilities)):
            ans += (probabilities[i]) * (houseNet[i])
            # for showing calcuations
            if (i < len(probabilities)-1):
                display += f"({probabilities[i]} x {houseNet[i]}) + "
            else:
                display += f"({probabilities[i]} x {houseNet[i]}) = {ans}"
        if (showPrintout):
            print(f"House Edge = {display}")
            print (f" .: House Edge = {ans} or {round(ans*100, 4)}%")
        return ans
    
def variance(probabilities, houseNet, houseEdge, showPrintout):
    if (len(houseNet) != len(probabilities)):
        print(f"Check for missing values in input arrays \n Probabilities:{probabilities}, House Net: {houseNet}")
        return
    else:
        var = 0
        display = ""
        for i in range(len(probabilities)):
            var += probabilities[i] * (houseNet[i]-houseEdge)**2
            if (i < len(probabilities)-1):
                # showing calculations
                display += f"{probabilities[i]} x ({houseNet[i]}-{round(houseEdge, 4)})^2 + "
            else:
                display += f"{probabilities[i]} x ({houseNet[i]}-{round(houseEdge, 4)})^2 = {round(var,4)}"
        if (showPrintout):
            print(f"Variance = {display}")
            print (f" .: Variance = {var}")
        return var

def stdDev(variance, showPrintout):
    stdDev = variance**0.5
    if (showPrintout):
        print(f" .: Standard Deviation = {stdDev}") 
    return stdDev




