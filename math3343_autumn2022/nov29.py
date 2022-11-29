import numpy as np

x = np.array([1,2,3]) # shape is (3,) -- one dimensional, length 3

A = np.array([[1,2,3],[4,5,6]]) # shape (2,3) -- 2x3 matrix

print(x.shape, A.shape)

print("x=\n",x)

print("A=\n",A)

u = np.zeros((10,)) # take tuples as arguments!!!
v = np.ones((5,8)) # !!!
# w = np.zeros(5,3) # ERROR: did not pass tuple

print(u,v)
