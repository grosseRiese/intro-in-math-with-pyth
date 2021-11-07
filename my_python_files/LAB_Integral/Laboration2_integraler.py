# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 22:53:50 2021

@author: GrooseRiese
"""

import matplotlib.pyplot as plt
import numpy as np
#import sympy as sy

print("======================= uppgift 1 ===========================")
f = lambda x:x*np.sin(x)

def calculate_dx (a, b, n):
	return (b-a)/float(n)

def leftEndPoint_rektangelregel(a,b,f,n): 
    """ over-estimation """
    h = calculate_dx(a,b,n) 
    x = np.linspace(a,b-h,n) #x_left
    
    I = np.sum(h*f(x[0:n]) )
    print('vänster Integral = ', I)
    
    plt.subplot(2,2,1) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera första
    
    plt.title('Left Riemann Sum, N = {}'.format(n))
    plt.ylabel('h-värdena') # Text längs y-axeln
    plt.xlabel(' ')
    
    
    plt.plot(x,f(x), 'r',markersize=10)
    plt.bar(x,f(x),width = h ,color='pink',align='edge')
    
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='yellow', alpha = 0.3 )
      
leftEndPoint_rektangelregel(0,1,f,100)
    
def Hoger_rektangelregel(a,b,f,n): 
    """ under-estimation """
    h = calculate_dx(a,b,n)
    x = np.linspace(h,b,n) #x_right
   
    I = np.sum(h*f(x[0:n]))
    print('höger Integral = ', I)
    
    plt.subplot(2,2,2) # Aktivera andra fönstret
    
    plt.title('Right Riemann Sum, N = {}'.format(n))
    plt.xlabel(' ')
    
    plt.plot(x,f(x),'b',markersize=10)
    plt.bar(x,f(x),width =-h, color='green',align='edge')   # width = (b-a)/n = h = calculate_dx
    
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='red', alpha = 0.3 )
    
Hoger_rektangelregel(0,1,f,100)

def Mittpunkts_metoden(a,b,f,n):

    h = calculate_dx(a,b,n)
    x = np.linspace(h/2,b-h/2,n) #Domain from a to b
    
    I = np.sum(f(x) * h)
    print('Mittpunktsmetoden Integral = ', I)
    
    plt.subplot(2,2,3) # Aktivera andra fönstret
    plt.title('\n\n\n\n')
    plt.xlabel('Midpoint Riemann Sum, N = {}'.format(n))
    
    plt.plot(x,f(x),'y',markersize=10)
    plt.bar(x,f(x),width = h,color='teal',edgecolor='teal')
    
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='teal', alpha = 0.3 )
    
Mittpunkts_metoden(0,1,f,100)

def Trapezoidal(a,b,f,n):
    
    x = np.linspace(a,b,n+1) # N+1 points make N subintervals
    y = f(x)
    
    y_right = y[1:] # right endpoints array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])
    y_left = y[:-1] # left endpoints array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    
    dx = calculate_dx(a,b,n) 
    T = (dx/2) * np.sum(y_right + y_left)
    #return T
    print("Trapezoid area T: ", T)
    
    #x = np.linspace(a,b,n)
    plt.subplot(2,2,4) # Aktivera andra fönstret
    plt.title('\n\n\n\n')
    plt.xlabel('Trapezoidal Riemann Sum, N = {}'.format(n))
    
    plt.plot(x,f(x),'y',markersize=10)
    plt.bar(x,f(x),width=dx,color='Orange',edgecolor='Orange')
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='teal', alpha = 0.3 ) 
Trapezoidal(0,1,f,100)
print("============================================================")
"""
============== uppgift 2 ======================
"""
F = lambda x: x
F_1 = lambda x:np.exp(-x**2)

def min_integral(f,a,b,n,k):
    '''Compute the Riemann sum of f(x) over the interval [a,b].

    Parameters
    ----------
    f : function
        Vectorized function of one variable
    a , b : numbers
        Endpoints of the interval [a,b]
    N : integer
        Number of subintervals of equal length in the partition of [a,b]
    method : string
        Determines the kind of Riemann sum:
        right : Riemann sum using right endpoints
        left : Riemann sum using left endpoints
        Trapezoidal: Riemann sum using trapz
        midpoint (default) : Riemann sum using midpoints

    Returns
    -------
    float
        Approximation of the integral given by the Riemann sum.
    '''
    dx = calculate_dx(a,b,n)
    #x = np.linspace(a,b,n+1)
    
    if k == 1: #left
        x = np.linspace(a,b-dx,n) #x_left
        x_left = x[:-1]
        #return np.sum(f(x_left)*dx)
        print("Left -Approximation- : ",np.sum(f(x_left)*dx))
    elif k == 2: #right
        x = np.linspace(dx,b,n) #x_right
        x_right = x[1:]
        #return np.sum(f(x_right)*dx)
        print("Right -Approximation-  : ",np.sum(f(x_right)*dx) )
    elif k == 3: # midpunkts
        x = np.linspace(dx/2,b-dx/2,n)
        x_mid = (x[:-1] + x[1:])/2
        #return np.sum(f(x_mid)*dx)
        print("Midpunkts -Approximation-  : ", np.sum(f(x_mid)*dx) )
    elif k == 4: #trapeziodal
        x = np.linspace(a,b,n+1) # N+1 points make N subintervals
        y = f(x)
        y_right = y[1:] # right endpoints 
        y_left = y[:-1] # left endpoints
        #return (dx/2) * np.sum(y_right + y_left)
        print("Trapeziodal -Approximation-  : ", (dx/2) * np.sum(y_right + y_left) )
    else:
        raise ValueError("Method must be 'left', 'right' or 'midpoint'.")

print("===================== uppgift 2 ============================")
min_integral(F,a=0,b=2,n=10,k=1) # left
min_integral(F,a=0,b=2,n=10,k=2) # right
min_integral(F,a=0,b=2,n=10,k=3) # mid
min_integral(F,a=0,b=2,n=10,k=4) # trapeziodal
print("============================================================")

print("===================== uppgift 3 ============================")
def min_integral_upp3(f,a,b,n,k):
    dx = calculate_dx(a,b,n)
    #x = np.linspace(a,b,n+1)
    
    if k == 1: #left
        x = np.linspace(a,b-dx,n) #x_left
        x_left = x[:-1]
        
        #return np.sum(f(x_left)*dx)
        print("Left -uppgift_3a : ",np.sum(f(x_left)*dx))
    elif k == 2: #right
        x = np.linspace(dx,b,n) #x_right
        x_right = x[1:]
        #return np.sum(f(x_right)*dx)
        print("Right_uppgift_3a : ",np.sum(f(x_right)*dx) )
    elif k == 3: # midpunkts
        x = np.linspace(dx/2,b-dx/2,n)
        x_mid = (x[:-1] + x[1:])/2
        #return np.sum(f(x_mid)*dx)
        print("Midpunkts_uppgift_3a : ", np.sum(f(x_mid)*dx) )
    elif k == 4: #trapeziodal
        x = np.linspace(a,b,n+1) # N+1 points make N subintervals
        y = f(x)
        y_right = y[1:] # right endpoints 
        y_left = y[:-1] # left endpoints
        #return (dx/2) * np.sum(y_right + y_left)
        print("Trapeziodal_uppgift_3a  : ", (dx/2) * np.sum(y_right + y_left) )
    else:
        raise ValueError("Method must be 'left', 'right' or 'midpoint'.")
min_integral_upp3(F_1,a=0,b=1,n=10,k=1) # left
min_integral_upp3(F_1,a=0,b=1,n=10,k=2) # right
min_integral_upp3(F_1,a=0,b=1,n=10,k=3) # mid
min_integral_upp3(F_1,a=0,b=1,n=10,k=4) # trapeziodal"""
print("==========================================================")

print("==========================================================")
F_b = lambda x: 1/(1+x**2)
def min_integral_upp3_b(f,a,b,n,k):
    dx = calculate_dx(a,b,n)
    #x = np.linspace(a,b,n+1)
    
    if k == 1: #left
        x = np.linspace(a,b-dx,n) #x_left
        x_left = x[:-1]
        
        #return np.sum(f(x_left)*dx)
        print("Left_upp_3b : ",np.sum(f(x_left)*dx))
    elif k == 2: #right
        x = np.linspace(dx,b,n) #x_right
        x_right = x[1:]
        #return np.sum(f(x_right)*dx)
        print("Right_upp_3b  : ",np.sum(f(x_right)*dx) )
    elif k == 3: # midpunkts
        x = np.linspace(dx/2,b-dx/2,n)
        x_mid = (x[:-1] + x[1:])/2
        #return np.sum(f(x_mid)*dx)
        print("Midpunkts_upp_3b  : ", np.sum(f(x_mid)*dx) )
    elif k == 4: #trapeziodal
        x = np.linspace(a,b,n+1) # N+1 points make N subintervals
        y = f(x)
        y_right = y[1:] # right endpoints 
        y_left = y[:-1] # left endpoints
        #return (dx/2) * np.sum(y_right + y_left)
        print("Trapeziodal_upp_3b  : ", (dx/2) * np.sum(y_right + y_left) )
    else:
        raise ValueError("Method must be 'left', 'right' or 'midpoint'.")
min_integral_upp3_b(F_b,a=-1,b=1,n=10,k=1) # left
min_integral_upp3_b(F_b,a=-1,b=1,n=10,k=2) # right
min_integral_upp3_b(F_b,a=-1,b=1,n=10,k=3) # mid
min_integral_upp3_b(F_b,a=-1,b=1,n=10,k=4) # trapeziodal
print("==========================================================")


print("==========================================================")
F_c = lambda x: np.tan(x**0.5)
def min_integral_upp3_c(f,a,b,n,k):
    dx = calculate_dx(a,b,n)
    #x = np.linspace(a,b,n+1)
    
    if k == 1: #left
        x = np.linspace(a,b-dx,n) #x_left
        x_left = x[:-1]
        
        #return np.sum(f(x_left)*dx)
        print("Left_upp_3c : ",np.sum(f(x_left)*dx))
    elif k == 2: #right
        x = np.linspace(dx,b,n) #x_right
        x_right = x[1:]
        #return np.sum(f(x_right)*dx)
        print("Right_upp_3c  : ",np.sum(f(x_right)*dx) )
    elif k == 3: # midpunkts
        x = np.linspace(dx/2,b-dx/2,n)
        x_mid = (x[:-1] + x[1:])/2
        #return np.sum(f(x_mid)*dx)
        print("Midpunkts_upp_3c  : ", np.sum(f(x_mid)*dx) )
    elif k == 4: #trapeziodal
        x = np.linspace(a,b,n+1) # N+1 points make N subintervals
        y = f(x)
        y_right = y[1:] # right endpoints 
        y_left = y[:-1] # left endpoints
        #return (dx/2) * np.sum(y_right + y_left)
        print("Trapeziodal_upp_3c  : ", (dx/2) * np.sum(y_right + y_left) )
    else:
        raise ValueError("Method must be 'left', 'right' or 'midpoint'.")
min_integral_upp3_c(F_c,a=0,b=1,n=10,k=1) # left
min_integral_upp3_c(F_c,a=0,b=1,n=10,k=2) # right
min_integral_upp3_c(F_c,a=0,b=1,n=10,k=3) # mid
min_integral_upp3_c(F_c,a=0,b=1,n=10,k=4) # trapeziodal
print("==========================================================")
print("=============== uppgift 4 ===================================")

wy = lambda x: np.tan(x**0.5)
def min_integral_upp4(f,a,b,n,k):
    dx = calculate_dx(a,b,n)
    #x = np.linspace(a,b,n+1)
    
    if k == 1: #left
        x = np.linspace(a,b-dx,n) #x_left
        x_left = x[:-1]
        
        #return np.sum(f(x_left)*dx)
        print("Left_upp_4 : ",np.sum(f(x_left)*dx))
    elif k == 2: #right
        x = np.linspace(dx,b,n) #x_right
        x_right = x[1:]
        #return np.sum(f(x_right)*dx)
        print("Right_upp_4  : ",np.sum(f(x_right)*dx) )
    elif k == 3: # midpunkts
        x = np.linspace(dx/2,b-dx/2,n)
        x_mid = (x[:-1] + x[1:])/2
        #return np.sum(f(x_mid)*dx)
        print("Midpunkts_upp_4  : ", np.sum(f(x_mid)*dx) )
    elif k == 4: #trapeziodal
        x = np.linspace(a,b,n+1) # N+1 points make N subintervals
        y = f(x)
        y_right = y[1:] # right endpoints 
        y_left = y[:-1] # left endpoints
        #return (dx/2) * np.sum(y_right + y_left)
        print("Trapeziodal_upp_4  : ", (dx/2) * np.sum(y_right + y_left) )
    else:
        raise ValueError("Method must be 'left', 'right' or 'midpoint'.")
min_integral_upp4(wy,a=0,b=1,n=100,k=1) # left
min_integral_upp4(wy,a=0,b=1,n=100,k=2) # right
min_integral_upp4(wy,a=0,b=1,n=100,k=3) # mid
min_integral_upp4(wy,a=0,b=1,n=100,k=4) # trapeziodal
print("==========================================================")














