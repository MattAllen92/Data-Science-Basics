# 1) Basic Functions
#def square(x, y=5):
#    """
#    Returns the square of the input
#    :param x: int
#    """
#    return (x ** 2) + y
#
#print square(3)
#print square(4,2)
#print square.__doc__

#def str_to_float(x):
#    try:
#        return float(x)
#    except:
#        print("Cannot convert input to float.")
#        
#str_to_float("Hello")
#str_to_float("5.32")
#str_to_float(32)

## 2) Containers
## a) Lists (mutable, indexed, ordered)
#test = list()
#test = []
#test.append("green")
#test.append("blue")
#test.append("yellow")
#print test[1]
#test[2] = "red"
#test2 = ["white", "black", "purple"]
#test3 = test + test2
#item = test.pop
#print item
#if "white" in test3:
#    print "True"
#if "black" not in test:
#    print "False"
#    
## b) Tuples (immutable, good for things that never change, can be used as dict keys)
#test_tup = tuple()
#test_tup = ()
#test_tup = ("hello",1,True)
#test_tup = ("hello",) # comma afer ensures it's a tuple and not sth like (9)
#print test_tup[0]
#test_tup[0] = "hello again" # raises exception, tuples are immutable
#if "hello" in test_tup:
#    print True
#    
## c) Dictionaries
#my_dict = dict()
#my_dict = {}
#my_dict = {"test":1,"test2":2}
#print my_dict["test"]
#my_dict["test2"] = 3
#my_dict["new_test"] = 4
#del my_dict["test"]
#if "test8" in my_dict:
#    print True
#else:
#    print "not found"
#    
## d) Containers within Containers
#tup_of_lists = ([1,2,3],[4,5,6])
#list_of_tups = [(1,"abc",True),(2,"def",False)]
#tup_of_dicts = ({1:"hello",2:"goodbye"}, {3:"ok",4:"not"})
#list_of_dicts = [{1:"hi",2:"bye"}, {3:"hey",4:"see ya"}]
#dict_of_tups = {1:(1,"abc"),2:(2,"def")}
#dict_of_lists = {1:[1,2,3],2:[4,5,6]}
#dict_of_dicts = {1:{1:"hi",2:"bye"}, 2:{3:"ok",4:"not"}}
#    
## e) Sets (no order, unique items only, fixed search time [hashable])   
#set1 = set([1,2,3])
#set2 = set([2,4,6])
#set3 = set([1,2])
#print len(set1)
#if 1 in set1:
#    print True
#if 1 not in set2:
#    print True
#if set3.issubset(set1):
#    print True
#if set1.issuperset(set3):
#    print True
#set4 = set1.union(set2) # combo of both, unique items only
#set5 = set1.intersection(set2) # items common to both only
#set6 = set1.difference(set2) # items unique to set1 only
#set7 = set1.symmetric_difference(set2) # items unique to each, not shared
#print set4, set5, set6, set7
    

    
    
    
    
    
    
    
    