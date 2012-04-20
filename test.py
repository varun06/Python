ranks = [9,9,7,7,5]


def kind(n,ranks):
    for r in ranks:
        if ranks.count(r) == n: return r
    return None



def two_pair(ranks):
    pair = kind(2,ranks)
    lowpair = kind(2,list(reversed(ranks)))
    print (pair and lowpair)
    if pair and lowpair !=pair:
        return (pair,lowpair)
    else:
        return None

print two_pair(ranks)