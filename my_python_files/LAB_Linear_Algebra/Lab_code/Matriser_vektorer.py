# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:40:51 2021
@author: Grosse...
"""
#from numpy import array
import numpy as np
import matplotlib.pyplot as plt


"""
#=========== Uppgift 1 ==================
=========================================
(a). Skriv in matriserna i Python och skriv sedan ut matriselementen a23, b2, c3.
Prova shape och size. Andra a23 till 15 genom att skriva A[1,2]=15.
"""

a = np.array([[1,4,7,10],[2,5,8,11],[3,6,9,12]])
b = np.array([[1],[3],[5]])
c = np.array([0,2,4,6,8])

print(">>>> A: \n",a)
print(">>>> B: \n",b)
print(">>>> C: \n",c)

print(">>>> a23: => a[1,2] \n",  a[1,2])
print(">>>> b2: => b[1] \n", b[1])
print(">>>> c3: => c[2] \n", c[2])

print(">> Shape(a) \n", a.shape) # eller  np.shape(a)
print(">> Size(a) \n", a.size) # eller np.size(a)


a[1,2] = 15
print(">>>> A: \n", a)

"""
(b) I Python skapar array ett s.k. objekt av en klass som heter ndarray. Därför kan vi också
skriva A.shape respektive b.size för att få reda på storlek och antal elemement. Testa även
detta på matriserna och vektorerna ovan. Prova också anropet c.shape=(5,1). Vad har hant
med c efter anropet?
Mer information om array i NumPy 
nns pa sidan
https://numpy.org/doc/stable/reference/arrays.ndarray.html
"""
c.shape=(5,1)
print(">>>> C: \n",c)

print(">> Shape(b) \n",  np.shape(b)) 
print(">> Size(b) \n",  np.size(b))

print(">> Shape(c) \n", np.shape(c)) 
print(">> Size(c) \n",  np.size(c))

"""==================== Ex. =======================""" 
T=[10,6,0,-6,-10,-16,-26,-30,-36]
v=[[2],[6],[10],[14],[18]]
Vind=[ [9,5,-2,-9,-14,-21,-33,-37,-44],
[7,2,-5,-13,-18,-26,-38,-44,-51],
[6,1,-7,-15,-20,-28,-41,-47,-55],
[6,0,-8,-16,-22,-30,-44,-49,-57],
[5,-1,-9,-17,-23,-31,-45,-51,-59]]

print("T:\n", T)
print("v:\n", v)
print("Vind:\n", Vind)

print("Vind 10 m/s & temp. -6:  ", Vind[2][3])

v= np.sin(c)
print("Vinkeln v: " ,v)

V= np.sin(a)
print("Vinkeln V: " ,V)

t= np.array([-np.pi/5,np.pi/3])
b= np.tan(t)
print("b : ",b)

"""
#=========== Uppgift 2 ==================
=========================================
Uppgift 2. Använd plot (från Matplotlib.pyplot) och rita upp tangensfunktionen på intervallet
0 <= x <= pi. Vad händer då x = pi/2 ?
"""

def tan_activeted_windows():
    plt.subplot(2,2,1)
    x = np.linspace(0,np.pi, 200) # Skapa lista med 200 jämnt fördelade tal från 0 till 2(pi)
    
    plt.plot(x, np.tan(x), 'y-') # Plotta tangens från 0 till 2pi med gul linje
    plt.title('tan 0 <= x <= pi')
    
#tan_activeted_windows()
"""======================================================"""
#Antalet rader och kolonner : [rader,kolonner]
[m,n] = np.shape(a)
print("[m,n] : ",[m,n] )
print("max(c):  ",np.max(c) )
print("max(a):  ",np.max(a) )

s = np.sum(c)
print("sum c: ", s)
p = np.prod(a)
print("Product: " ,p)

c=np.array([2,4,1,-9,0])
sc = np.sort(c)
print("c sorted: ",sc)
print("c before-sorted: ",c)

A=np.array([[2,4,1,-9,0],[-8,0,2,-3,5]])
sA=np.sort(A)
print("Sorted A: ",sA)

"""======================================================"""
#3-Hantering av vektorer och matriser i NumPy

c =(0,2,4,6,8)
c = np.arange(0,9,2)
print("c arange: ", c)

v= np.copy(c[[1,4]])    #Observera att man maste skriva dubbla hakparenteser
print("Copy c: ", v)

V= np.copy(A[0:2,1:3])
print("Copy A : rad 1-2 och kolonn 2-3: \n",V)

"""
#=========== Uppgift 3 ==================
=========================================
(a). Bilda en 2X2-matris B av det block av storlek 2X2 som står längst ned till höger
 (i de två sista raderna och de två sista kolonnerna) i matrisen A. Andra sedan elementet
b2,2 till 100.
(b) Transponera matrisen B.
"""
B_matris = np.array([[1,4],[2,5]])
print("B_matris Before : ",B_matris)

B_matris[1,1] = 100
print("B_matris After : ",B_matris)


#Vi kan transponera matrisen med .T:
print("Transponat Sorted A: ",B_matris.T )

"""======================================================"""
#3.3 Operatorer pa vektorer och matriser i NumPy
"""======================================================"""

"""
#================= Uppgift 4. =================================================
Använd linspace (läs hjälptexten) för att bilda vektorn d = (2; 5; 8; 11; 14).
"""
def vector_windows():
    d = np.linspace(2,14,num=5) # Get five numbers btw & including (2 -14 )
    
    d_1 = np.linspace(2,14,num=5, endpoint=False)
    d_2 = np.linspace(2,14,num=5, retstep=True) 
    d_3 = np.linspace(2,14,num=5, dtype = int) 
    print("   ************************ ")
    
    print("Vektorn d: ",d)
    print("Vektorn d_1 without endpoint, 14: ",d_1)
    print("Vektorn d_2 wit the long of the steps: ",d_2)
    print("Change the data type: ",d_3)
    
    print("   ************************ ")
vector_windows()

"""======================================================"""
   #==========  4 Linjara ekvationssystem ==============
"""======================================================"""







