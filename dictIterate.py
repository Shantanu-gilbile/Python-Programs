batches= {"PPA" : 18000 , "LB" : 16700 , "Python" : 16500 , "Angular" : 15000}

print("Data of dictionary is : ",batches)

print("Data traversal using for loop")

for x in batches:
    print(x)

print("______________________")

for x in batches:
    print(x," : ",batches[x])

print("______________________")

for x in batches:
    print(x," : ",batches.get(x))

keyBatches = batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches=batches.values()
print(type(valueBatches))
print(valueBatches)




