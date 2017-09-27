g1 = [1,2,3,4,5]
g2 = [0,1,2,3,4]

# my long winded solution

def best_match(g1, g2):
    idx = 0
    best_match = [0, 0, 0]
    for x, y in zip(g1, g2):
        gd = x - y
        gs = y
        if idx == 0:
            best_match = [gd, gs, idx]
        else:
            if gd < best_match[0]:
                best_match = [gd, gs, idx]
            elif gd == best_match[0]:
                if gs > best_match[1]:
                    best_match = [gd, gs, idx]
                elif gs == best_match[1]:
                    if idx < best_match[2]:
                        best_match = [gd, gs, idx]
        idx += 1
    return best_match[2]
        
print best_match(g1, g2)

# elegant solution
def best_match_short(g1, g2):
    return min((a-b, -b, i) for i, (a,b) in enumerate(zip(g1, g2)))[2]
    #return sorted((a-b, -b, i) for i, (a,b) in enumerate(zip(g1, g2)))[0][2] # this one works but I don't know how
    #return sorted([(a-b, -b, i) for i, (a,b) in enumerate(zip(g1, g2))], key=lambda x : x[2]) # this one returns a sorted list of arrays, not the exact answer

print best_match_short(g1, g2)