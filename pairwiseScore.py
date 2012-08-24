def pairwiseScore(seqA, seqB): 
    x = 1
    i = 0
    score = 0
    rtnStr = seqA + "\n"
    while i < len(seqA) :
    	if seqA[i] == seqB[i]:
    	     x += 1
    	     if x > 3:
    	         x -= 1
        else:
    	     x = 1
        if x == 1:
             score -= 1
             rtnStr += " "
        if x == 2:
             score += 1
             rtnStr += "|"
        if x == 3:
            score += 3
            rtnStr += "|"
        i += 1
    rtnStr += "\n" + seqB + " Score: " + str(score)
    return rtnStr

# print pairwiseScore("ATTCGT", "ATCTAT")
print pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")