import math

def race(v1, v2, g):
    if v1 > v2:
        return None
    else:
        vDiff = abs(v1 - v2)
        secondsToCatch = math.floor((float(g) / vDiff)*60*60)               
        m, s = divmod(secondsToCatch, 60)
        h, m = divmod(m, 60)
        return [h,m,s]