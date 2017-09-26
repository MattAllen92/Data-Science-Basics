list1 = [3,2,4,1,1]
list2 = ['three','two','four','one','one2']

newList, newList2 = zip(*sorted(zip(list1, list2)))
print newList, newList2