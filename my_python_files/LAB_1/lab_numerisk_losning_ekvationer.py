# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 08:54:21 2021

@author: Me
"""
import matplotlib.pyplot as plt
import numpy as np

def ExpoFunc():
    x=np.linspace(-2,7) #Skapar en lista med x-värden
    y=(x-2.5)*np.exp(-0.5*(x-2)**2)+0.2 #Beräknar motsvarande funktionsvärden y=f(x)
    
    plt.plot(x,y)
    plt.text(4.1,0.5, "$y=f(x)$",fontsize=16) #Text vid grafen
    plt.axis([-2,7,-1,1]) #Anger gränser för x och y i fönstret
    plt.grid() #Aktiverar rutnät
    
#ExpoFunc()

#lambda func _ uppgift_1 >>LAb_1
f_X = lambda x:(x-2.5)*np.exp(-0.5*(x-2)**2)+0.2 #corresponding valuesto func y = f (x)
def uppgift_1(f_X):
    x=np.linspace(-1,5) # a list of x-value
        
    plt.plot(x,f_X(x)) 
    plt.text(4.1,0.5, "$y=f(x)$",fontsize=16) 
    plt.axis([-1,5,-1,1]) 
    plt.grid() #Aktiverar rutnät
uppgift_1(f_X)  

# the interval halving method is called :"Bisection method"
#uppgift_2

def intervall_halverings_metoden(f,a,b):
    fa = f(a)
    fb = f(b)
    
    if fa*fb > 0:
        print("f(a) and f(b) must have different signs")
        return None
    
    for _ in range(100):
        
        m = (a + b) /2
        fm =f(m)
        
        if fm == 0:
            #return m            
            break
        
        if fa*fm > 0:
            a = m
            fa = fm
            
        if fb*fm > 0:
            b = m
            fb = fm
            
    return m        
 
LampdaFunc = lambda x:(x-2.5)*np.exp(-0.5*(x-2)**2)+0.2 #corresponding valuesto func y = f (x)
x = intervall_halverings_metoden(LampdaFunc,-1,0)
#print("Solution Found: {} ".format(x))

####################################################################################################
#uppgift_3
"""
def min_bisect(f,a,b):
    fa = f(a)
    fb = f(b)
    
    if fa*fb > 0:
        print("f(a) and f(b) must have different signs")
        return None
    
    for _ in range(100):
        
        m = (a + b) /2
        fm =f(m)
        
        if fm == 0:
            #return m            
            break
        
        if fa*fm > 0:
            a = m
            fa = fm
            
        if fb*fm > 0:
            b = m
            fb = fm
            
    return m        
 
my_y = lambda x:(x-2.5)*np.exp(-0.5*(x-2)**2)+0.2 #corresponding valuesto func y = f (x)
x_3 = min_bisect(my_y,-1,0)
#print("Solution Found: {} ".format(x_3))
"""
####################################################################################################
####################################################################################################
#uppgift_4

def min_bisect(f,a,b,tolerance = 1e-10):
    fa = f(a)
    if abs(fa) < tolerance:
        return a
    
    fb = f(b)
    if abs(fb) < tolerance:
        return b
    
    
    if fa*fb > 0:
        print("f(a) and f(b) must have different signs")
        return None
    
    for _ in range(100):
        
        m = (a + b) /2
        fm =f(m)
        
        if abs(b - a) < tolerance:
            break
        
        if abs(fm) < tolerance: #fm == 0:
            #return m            
            break
        
        if fa*fm > 0:
            a = m
            fa = fm
            
        if fb*fm > 0:
            b = m
            fb = fm
            
    return m        
 
y = lambda x:(x-2.5)*np.exp(-0.5*(x-2)**2)+0.2 #corresponding valuesto func y = f (x)
_x_ = min_bisect(y,-1,0)
print("Solution Found: x = {}, f(x) = {} ".format(round(_x_,5),round(y(_x_), 5) ))

####################################################################################################