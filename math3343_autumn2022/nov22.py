class C:
    _i = 4
    __j = 10
    def __init__(self):
        self.__k = 10
    def info(self):
        return self._i, self.__j, self.__k
   
x = C()
print(x.info())

print(x._i) #okay, no mangling with _ 
# print(x.__j) # Error, mangled 

x._i = 1000 # no mangling with single _
x._C__j = 7 # with two _, name is mangled via _ClassName__attributeName
print(x.info())

x.__j = 7 # adds another instance variable to x 
print(x.info()) # the "__j" from before still 7 
