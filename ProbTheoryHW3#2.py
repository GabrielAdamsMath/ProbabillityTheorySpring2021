from itertools import chain, combinations,permutations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


nSizeLists = list(powerset("SIGMA"))



permList = []


for i in nSizeLists:
    if len(list(i)) > 0:
            for j in list(permutations(list(i))):
                permList.append(j)

print(permList)
print(len(permList))