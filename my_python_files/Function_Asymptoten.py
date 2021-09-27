# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:12:47 2021

@author: Me
"""
import numpy as np
import matplotlib.pyplot as plt

def asymptoten_function ():
    f = lambda x: (x**3-3*x**2+2*x+1)/(x**2+1)
    asymptote = lambda x : x-3
    
    x = np.linspace(-4,6,1000)#Skapar en lista med 1000 x-värden mellan 
    y1 = f(x) #Beräknar motsvarande y-värden för functionen f
    y2 = asymptote(x) #Beräknar motsvarande y-värden för asymptoten
    
    plt.plot(x,y1)
    plt.plot(x,y2,'--',color='red')
    
    plt.axis([-4,6,-8,5]) #Anger gränser för x och y i fönstret
    plt.grid()  #Aktiverar rutnät
    plt.text(0,2, "$y=f(x)$", fontsize=16)
    plt.text(2,-2, "$y=x-3$", fontsize=16)
    
asymptoten_function()