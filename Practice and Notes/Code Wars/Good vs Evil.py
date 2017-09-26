def goodVsEvil(good, evil):
    good_dict = {1:1,2:2,3:3,4:3,5:4,6:10}
    evil_dict = {1:1,2:2,3:2,4:2,5:3,6:5,7:10}
    sum_good = 0
    sum_evil = 0
    for i, x in enumerate(good.split()):
        sum_good += int(x) * good_dict[i+1]
    for i, x in enumerate(evil.split()):
        sum_evil += int(x) * evil_dict[i+1]
    if sum_good > sum_evil:
        return "Battle Result: Good triumphs over Evil"
    if sum_good < sum_evil:
        return "Battle Result: Evil eradicates all trace of Good"
    else:
        return "Battle Result: No victor on this battle field"


print goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')