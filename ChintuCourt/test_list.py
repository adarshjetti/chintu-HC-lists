blist=["ponni","munni","chinni","ponni"]
print(blist.count("ponni"))

#If you only want one item's count, use the count method:
[1, 2, 3, 4, 1, 4, 1].count(1)


indices = [i for i, x in enumerate(blist) if x == "ponni"]
print(indices)

haystack = ['a', 'b', 'c', 'V', 'd', 'e', 'X', 'f', 'V', 'g', 'h']
needles = ['V', 'W', 'X', 'Y', 'Z']
st = set(needles)
print([i for i, e in enumerate(haystack) if e in st])

from operator import itemgetter
a = ["ponni", "munni", "chinni", "sunny", "jinny", "minni", "pinni"]
b = [1, 2, 5]
x=list(itemgetter(*b)(a))
print(x)


import numpy as np
a = np.array(["ponni", "munni", "chinni", "sunny", "jinny", "minni", "pinni"])
b = [1]
print(list(a[b]))

z=['guntur','tenali','kakinada','guntur']
for k,i in enumerate(z):
    print(k,i)
    #print(z.index(x))

    '''ProgramFailedError :as pfe
        #print('Exception Name: ', pfe.value)
        #if pfe.value=="'DatesMismatchError'":
            #print("Dates on webpage have been changed.\nRun the program after 5 minutes.")'''

