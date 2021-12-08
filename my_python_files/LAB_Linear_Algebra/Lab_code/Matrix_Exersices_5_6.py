# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:11:23 2021

@author: Groose
"""
import numpy as np
#import matplotlib.pyplot as plt

from numpy.linalg import solve
from sympy import Matrix
from scipy.linalg import hilbert
"""
#================= Uppgift 5. =================================================
Skriv följande ekvationssystem på matrisform och läs dem sedan med solve.
(Skulle det finnas oändigt många lösningar eller om systemet saknar lösningar,
måste vi använda andra kommandon är solve.)
********** Ax = b, ************
*****  A =[1 2 3], x[x1], och b = [m]  ******
"""
#--> (a):

A = np.array([[2,3],[5,4]])
b = np.array([[8],[13]])
x = solve(A,b)

print("a: Lösningarna till ekvationssystemet. \n", x) #[[1],[2]]

#--> (b):
A = np.array([[1,5,9],[2,0,5],[3,7,11]])
b = np.array([[29],[26],[39]])
x = solve(A,b)

print("b: Lösningarna till ekvationssystemet. \n", x) #[[3],[-2],[4]]

#--> (c):
A = np.array([[1,1/2,1/3],[1/2,1/3,1/4],[1/3,1/4,1/5]])
b = np.array([[11/6],[13/12],[47/60]])
x = solve(A,b)

print("c: Lösningarna till ekvationssystemet. \n", x) #[[1],[1],[1]]

#--> (d):
A = np.array([[1,1,3,4],[-2,2,2,0],[1,1,2,3],[1,-1,-2,-1]])
b = np.array([[2],[-4],[1],[1]])
#x = solve(A,b)

#print("d: Lösningarna till ekvationssystemet. \n", x) #systemet saknar lösningar,


"""
#================= Uppgift 6. =================================================
(a) Bilda en 10 X 10-Hilbertmatris och beräkna dess determinant.. med hjälp av
"""
A=hilbert(10)
D=np.linalg.det(A)
print("Hilbertmatris : ",D)

"""
(b),c,d..
"""
x_exact = np.ones((10, 10)) #Return a new array of given shape and type, filled with ones.
b = np.matmul(A,x_exact)
print("b <<<<: ",b)
#print("x_exact <<<<: ",x_exact)

x = solve(A,b)
print("X solve(): ",x)








