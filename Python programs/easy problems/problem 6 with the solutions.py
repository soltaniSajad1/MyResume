# Calculate the union of two sets
import time

setA = {1, 3, 5, 7, 9, 11}
setB = {0, 2, 4, 6, 8, 10, 12}

print(setA)
print(setB)
print("We are making union of two sets, please wait . . . ")
time.sleep(4)
setResult = setA.union(setB)
print(setResult)

# Calculate the union of three sets

set1 = {1, 3, 6, 2, 8}
set2 = {4, 9, 5, 11, 0}
set3 = {12, 17, 14, 13, 8}
setTrain = {}

print("\n", set1, "\n", set2, "\n", set3)
print("We are making three union of sets, please wait . . . ")
time.sleep(4)
setTrain = set1.union(set2)
result = setTrain.union(set3)
print(result)