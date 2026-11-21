class Time:
    def __init__(self,h,m):
        self.h = h 
        self.m = m
        
    def disp(self):
        print(f"{self.h}:{self.m}")
        
now = Time(21,9)
print(now.h,":",now.m,sep='')

# these are equivalent
now.disp()
Time.disp(now)
