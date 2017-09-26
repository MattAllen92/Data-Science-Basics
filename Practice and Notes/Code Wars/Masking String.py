cc = "hello1221312"
out = ['#' for x in cc[:-4]]
outStr = ''.join(out)
print outStr + cc[-4:]
#print ''.join(out)