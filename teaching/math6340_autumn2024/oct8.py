a = [2, 4, 6]
b = a
c = [ a ]
b.append(8)
d = c + [1, 2, 3]
d[0][0] = True

'''
d -------------------> [ *, 1, 2, 3]
                         |
                         v

a ------------------->    [ True , 4, 6, 8 ]  <---------------- b
                         ^
                         |
c -------------------> [ * ]

a == [True, 4, 6, 8]
b == [True, 4, 6, 8]
c == [[True, 4, 6, 8]]
d == [[True, 4, 6, 8], 1, 2, 3]
'''
print(a,b,c,d)


for i in range(1001):
    # ints allocated 0 to 256
    if i is (i+0): # stops being true after i == 256
        print(i)

t = (1,2,[])
print(type(t[2]))
L = [1,2,[]]
print(type(L[2]))
L[2] = [1,2,3]
print(L)
#t[2] = [1,2,3] # t[2] is list, same as L[2], but Python tracks this as an element of a tuple, no =


x = (1,[])
y = x
y[1].append(14)
print(x,y)
