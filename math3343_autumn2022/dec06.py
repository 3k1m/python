import numpy as np

A = np.arange(20).reshape(4,5)
print(A)
print(A<12) # array of bools
B = A[A<6]
print(B)
B[2] = -1
print(B, A) # but B was only a copy of A in this case

A[A<8] *= 2 # direct assignment to logically indexed array allows changes
print(A)

C = A[::2,2::] # all rows in strides of 2 and all columns from index 2 onwards
# rows 0, 2 and cols 2, 3, 4
print(C)

C[0,0] = -2 # standard slicing will result in references and thus we change A
print(C, A)

D=A[[1,0],[1,2]] # advanced indexing: select A[1,1] and A[0,2]. no view. just a copy
D[1] = -3
print(A, B, C, D)

#print(np.arange(20).reshape(3,10))
