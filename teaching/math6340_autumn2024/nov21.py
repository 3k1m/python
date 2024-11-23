'''
(P1) Write a Python Vector class that stores a list to represent a vector. There should be 
- a constructor that accepts a list and sets the internal list accordingly 
- a print function that will print the vector in the form <1,2,3>
- a norm function that will return the Euclidean lenth of the vector 
- an add_to function that will add another vector of the same length to the present vector and if the lengths 
are not the same, nothing should happen '''

class Vector:
    
    def __init__(self,lst): # come back to this...
        self.lst = lst.copy() # copy to prevent weird dependencies
        
    def print(self):
        print("<"+",".join([str(i) for i in self.lst]), ">",sep='')
        
    def norm(self):
        return sum([i**2 for i in self.lst])**0.5
        
    def add_to(self,v2):
        if len(self.lst) != len(v2.lst):
            return
        for i in range(len(self.lst)):
            self.lst[i] += v2.lst[i]
      

def main():
    
  '''Determine the printout:'''

  class C:
    i = 7
    def __init__(self, p):
      self.j = p
    def f(*a):
      print(type(a), len(a))
    def g(self,q):
      print(q)

  def h(u,v):
    print(u.j.append(3))

  x = []    # x --------------->   [  ]
            #                      ^
  y = C(x)  # y ---- {            j   }
  C.r = h

  C.f(1)     # <class 'tuple'> 1
  y.f(1)     # <class 'tuple'> 2
  C.g(4,5)   # 5 (self is 4 here)
  y.g(6)     # 6 (self is y now)
  print(y.i) # 7 (from the class)
  print(y.j) # []
  
  y.i = 128 
  print(C.i, y.i) # 7 128 ("masking")
  del C.i 
  print(y.i) # 128 
  y.r(100) # h(y,100) -> y.j.append(3), so y.j == [3]
  # prints None from append 
  print(y.j) # [3]
    
    
    
    
  x = [2,5]
    
  v = Vector(x)
  v.print()
    
  v2 = Vector([1,-1])
  v.add_to(v2)
  v.print()
    
  print(x) # x got changed!!! (or not changed after using .copy())
    
  print(v.norm())
    
if __name__ == "__main__":
    main()
