#def longest(s1, s2):
#    s1_crush = sorted(set(s1))
#    s2_crush = sorted(set(s2))
#    if len(s1_crush) > len(s2_crush):
#        return ''.join(s1_crush)
#    else:
#        return ''.join(s2_crush)
#    
#print longest("loopingisfunbutdangerous", "lessdangerousthancoding")

a = set("lessdangerousthancoding")
print ''.join(a)
print ''.join(sorted(a))