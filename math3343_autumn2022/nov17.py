L1 = [1,2,3,4,5,6]
L2 = [2, 9, 6, 14]

# L3 = [ ... for e in L1 if e % 2 == 0] -- evens in L1
# L3 = [ 3*e if e in L2 else 2*e   ... ]  -- either tripling or doubling
L3 = [ 3*e if e in L2 else 2*e for e in L1 if e % 2 == 0 
