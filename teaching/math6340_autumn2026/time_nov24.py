class Time:
    __max_min = 59
    __max_hr = 23
    
    def __init__(self,h,m):
        self.h = h 
        self.m = m
        
    def disp(self):
        print(f"{self.h}:{self.m}")
        
    def next(self):
        if self.m == self.__max_min:
            if self.h == self.__max_hr:
                self.h=0
                self.m = 0
            else:
                self.h += 1
                self.m = 0
        else:
            self.m += 1
            
    def advance_min(self,num):
        for i in range(num):
            self.next()
            
    def __str__(self): # magic method 
        return f"{self.h}:{self.m}"
                
    
        
now = Time(20,4)
now.disp()
now.next()
now.disp()
now.advance_min(60)
now.disp()
print(now)

# evil hacking 
now._Time__max_min = 30
now.advance_min(60)
print(now)
