
myList  = [i for i in range(20) if i%2 ==0 ]

print(myList)

anotherList = ['banana', 'shortpath', 'another', 'koko']
myset = {"set", "twoset", "threeset"}

print(f"AnotherLIst: {anotherList}")
print(f"myset: {myset}")

for i, itemset in enumerate(myset): 
    print(f"i:{i} itemset:{itemset}")

frznset = frozenset(myset)

print(f"Frozenset : {frznset}")
