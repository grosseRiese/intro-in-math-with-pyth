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
####################################################################################################
#uppgift_5

def projektilbanan(x):
    y0=1.85;
    v0=10; 
    theta=45; 
    g=9.81 #Antaganden
    
    t=theta*np.pi/180 #Konvertering från grader till radianer
    
    a=g/(2*v0**2*np.cos(t)**2);
    b=v0**2*np.sin(2*t)/(2*g);
    c=v0**2*np.sin(t)**2/(2*g)
    
    return y0-a*(x-b)**2+c #Returnerar projektilens höjd vid (horisontellt) avstånd x från utkastpunkten

def draw_graf():
    x = np.linspace(-4,5) # a list of x-value
    plt.plot(x,projektilbanan(x)) # plot values of (x,y)
    plt.text(6.1,0.5, "$y(x)=f(x)$",fontsize=16) 
    plt.axis([-3,6,-1,6]) 
    plt.grid() #Aktiverar rutnät
    
    x2 = min_bisect(projektilbanan,-2,-1)
    print("Solution Found: x2 = {}, f(x) = {} ".format(round(x2,5),round(projektilbanan(x2), 5) ))
    
#draw_graf()
##############################################################
#uppgift_6

def derivative(f, x, dx = 1e-6):
    df = f(x + dx) - f(x - dx)
    return df/(2*dx)

def newton_raphsons(f, x0, tol = 1e-10, maxit = 100): #tol:tolerance

    x = x0
    fx = f(x)

    for _ in range(maxit):

        if abs(fx) < tol:
            #print("fx {} ".format(fx))
            break
        
        fpx = derivative(f, x)
        if abs(fpx) < tol:
            #print("fpx {} ".format(fx))
            break

        x = x - fx/fpx
        fx = f(x)

    return x

func = lambda x: x**3 - np.cos(4*x)

def draw_newton_graf():
    x = np.linspace(-2,0.58) # a list of x-value
    plt.plot(x,func(x)) # plot values of (x,y)
    plt.text(4.5,0.5, "$Y=f(x)$",fontsize=16) 
    plt.axis([-1.5,4,-0.5,1]) 
    plt.grid() #Aktiverar rutnät
    
    x0 = 0.5
    x_k = newton_raphsons(func, x0, tol = 1e-10, maxit = 100)
    print("Solution: x = {}, f(x) = {}".format(x_k, func(x_k)))
    
#draw_newton_graf()

##############################################################
#uppgift_7
def derivative_function(f, x, dx = 1e-6):
    df = f(x + dx) - f(x - dx)
    return df/(2*dx)

def min_NewtonRaphson(f,Df,x0,tol = 1e-10):
    x = x0
    fx = f(x)

    for _ in range(100):

        if abs(fx) < tol:
            #print("fx {} ".format(fx))
            break
        
        fpx = Df(f, x)
        if abs(fpx) < tol:
            #print("fpx {} ".format(fx))
            break

        x = x - fx/fpx
        fx = f(x)

    return x

func_7 = lambda x: x
def draw_min_NewtonRaphson_graf():
    x = np.linspace(-1,5) # a list of x-value
    plt.plot(x,func_7(x)) # plot values of (x,y)
    plt.text(4.5,0.5, "$y=f(x)$",fontsize=16) 
    plt.axis([-1,4,-1,5]) 
    plt.grid() #Aktiverar rutnät
    
    x0 = 2
    x_k = min_NewtonRaphson(func_7,derivative_function,x0, tol = 1e-10)
    print("Solution: x = {}, f(x) = {}".format(x_k, func_7(x_k)))
    
#draw_min_NewtonRaphson_graf()
#############################################################################################
##=____________________________________________________________________________________##
""" uppgift_8 : Testa nu din funktion min_NewtonRaphson på följande funktioner 
genom att rita grafer samt beräkna samtliga nollställen:"""
#########################################################################################
func_8_a = lambda x: 0.5*(x-2)**2-2*np.cos(2*x)-1.5
""" upp.8_A"""
def draw_min_NewtonRaphson_8_a_graf():
    x = np.linspace(-1,5) # a list of x-value
    plt.plot(x,func_8_a(x)) # plot values of (x,y)
    plt.text(4,0.5, "$y=f(x)$",fontsize=16) 
    plt.axis([-1,4,-4,3]) 
    plt.grid() #Aktiverar rutnät
    
    x0 = 2
    x_k = min_NewtonRaphson(func_8_a,derivative_function,x0, tol = 1e-10)
    print("Solution: x = {}, f(x) = {}".format(x_k, func_8_a(x_k)))
    
draw_min_NewtonRaphson_8_a_graf()



""" upp.8_B"""

func_8_b = lambda x: x**3-np.cos(4*x)
def draw_min_NewtonRaphson_8_b_graf():
    x = np.linspace(-1,5) # a list of x-value
    plt.plot(x,func_8_b(x)) # plot values of (x,y)
    plt.text(4,0.5, "$Y=f(x)$",fontsize=16) 
    plt.axis([-1,2.5,-1.5,4.5]) 
    plt.grid() #Aktiverar rutnät
    
    x0 = 2
    x_k = min_NewtonRaphson(func_8_b,derivative_function,x0, tol = 1e-10)
    print("Solution: x = {}, f(x) = {}".format(x_k, func_8_b(x_k)))
    
draw_min_NewtonRaphson_8_b_graf()
