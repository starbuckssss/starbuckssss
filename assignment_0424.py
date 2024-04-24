# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:07:13 2024

@author: Sungwoo Park
"""


#%% 2  ## 
class Car:
    color = ""
    speed = 0
    
    def upSpeed(self, value): ## self 추가
        self.speed += value   ## self 추가
        
        

#%% 4 ## 
class Horse:
    speed = 0
    
    def __init__(self):
        self.speed = 50
        
    def get(self):
        return self.speed

h_speed = Horse()
print(h_speed.get()) ## reset the speed value "50"
    


#%% 6  
## 3.슈퍼클래스 서브클래스

#%% 7  
class Car:
    speed = 0
    
    def upSpeed(self, value):
        self.speed = self.speed + value
    
class RVCar(Car): ## 추가
    seatNum = 0
    
    def getSeatNum(self):
        return self.seatNum