# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 00:46:49 2021

"""

import matplotlib.pyplot as plt
import numpy as np



""" ======== OVN========== """
"""
k_value = float(input("Input k parameter : ") )
m_value = float(input("Input m parameter : ") )
"""
def korsar_x_axeln(k,m):
    x_arr= np.array([-3,-1,0,1,2])
    y_arr = ([])
    
    if k != 0:
        for j in x_arr:
            x=j
            y=k*x+m
            print("y = k*x+m, {}*{}+{} : => {}".format(k,x,m,y))        
            y_arr.append(y)
        
        
        print("Linjen korsar x-axeln när;\n x:{} då\n y:{} .".format(x_arr,y_arr))
        return x
    else:
        print("Linjen korsar inte x-axeln när k==0 då x=0 \ vilket gör att y = m")
        for h in y_arr:
            print("y = k*x+m, {}*{}+{} : => {}".format(k,x,m,h))   
        return ("Inget svar")
#korsar_x_axeln(k_value,m_value)

def numpy_arr_func():
    num_array = np.arange(1, 10**6+1)
    #print("num_array: ",num_array)
    
    segma_sum = np.sin(num_array)
    summa = np.sum(segma_sum)
    
    print("segma_sum",segma_sum)
    print("summa: ",summa)
    
    sum_en_del_av_i = np.sum(1/num_array)
    
    print("sum 1/i: ",sum_en_del_av_i)
#numpy_arr_func()

def funktions_grafer():
   
    x_values = np.linspace(0, 2, 100)  # Skapa lista med 200 jämnt fördelade tal från 0 till 2
    plt.axis([0, 2, 0, 4])      # Ange gränser för x och y i fönstret
    plt.subplot(2,2,1) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera första
     #f(x)=√x,
    x_values = np.array([0,1,2,4])
    y_values =  np.zeros(len(x_values))#([])
    for i in range(len(x_values)):
        print("X: ",i)
        y_values[i] = np.sqrt(x_values[i])
    print("f(x) : ",y_values)
    plt.plot(x_values,y_values,'r--o',label='f(x)=√x')
    plt.legend() # Förklaring till de olika listorna med texten som angavs som 'label' i kommandot plot
    #plt.show()
    #plt.title('f(x)=√x')
    """
    x_values = np.array([0,1,3,8])
    y_values = ([])
    for x in x_values:
        fx = np.sqrt(x)
        print("X: ",x)
        y_values.append(fx)
    print("f(x) : ",y_values)
    plt.plot(x_values,y_values)
    plt.show()
    """
    #=======================================================================================
    # f(x)=x
    #plt.axis([0, 2, 0, 4])      # Ange gränser för x och y i fönstret
    plt.subplot(2,2,2) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera andra
    x2_values = np.array([-1,0,2,4])
    y2_values =  np.zeros(len(x2_values))
    for x2 in range(len(x2_values)):
        print("X: ",x2)
        y2_values[x2] = x2_values[x2]
    print("f(x) : ",y2_values)
    plt.plot(x2_values,y2_values,'gh ',label='f(x)=x')
    plt.legend() # Förklaring till de olika listorna med texten som angavs som 'label' i kommandot plot
    #plt.show()
    #plt.title('f(x)=x')
    #========================================================================================
     # f(x)=x^2
    #plt.axis([0, 2, 0, 4])      # Ange gränser för x och y i fönstret
    plt.subplot(2,2,3) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera andra
    x3_values = np.array([0,1,2,4])
    y3_values =  np.zeros(len(x3_values))
    for _x in range(len(x3_values)):
        u =_x**2
        print("u: ",u)
        y3_values[_x] = u
    print("x^2: ",y3_values)
    plt.plot(x3_values,y3_values,'b-o',label='f(x)=x^2')
    plt.legend() # Förklaring till de olika listorna med texten som angavs som 'label' i kommandot plot
    #plt.show()
    #plt.title('f(x)=x^2')
    #========================================================================================
    # f(x)=x^3
    #plt.axis([0, 2, 0, 4])      # Ange gränser för x och y i fönstret
    plt.subplot(2,2,4) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera andra
    xi_val = np.array([0,1,2,4])
    yi_val =  np.zeros(len(xi_val))
    for _xi in range(len(xi_val)):
        u =_xi**3
        print("u: ",u)
        yi_val[_xi] = u
    print("x^3: ",yi_val)
    plt.plot(xi_val,yi_val,'y-.',label='f(x)=x^3')
    plt.legend() # Förklaring till de olika listorna med texten som angavs som 'label' i kommandot plot
    #plt.show()
    #plt.title('f(x)=x^3')
    
funktions_grafer()    




""" =================Examplar ====================== """

# Skapa en "vanlig" funktion min_f som beräknar värdet av f
def min_f(x):
    return x**3-x+1 

# Skapa en universell funktion av denna med samma namn dvs min_f
min_f = np.frompyfunc(min_f,1,1)

x_lista = np.array([-2, -1, 0, 1, 2])  # En lista (array) av x-värden
y_lista = min_f(x_lista)               # Ger lista med  f(x) för alla värden 
                                       # i x_lista, dvs [-5, 1, 1, 1, 7]
#print(y_lista)

"""====================== : Grafer och diagram ==============================="""
def kvadraterna():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) # Plotta de 4 första jämna kvadraterna
    plt.show()                         # Visa figuren (behövs ej i Spyder som automatiskt visar den i panelen Plots)
#kvadraterna()
"""====================================================="""
def fibonacci_talen():
    plt.plot([0,1,1,2,3,5,8,13,21,34]) # Plotta de 10 första Fibonacci-talen
    plt.show()
#fibonacci_talen()
"""====================================================="""
def jamna_kvadraterna():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'k--o' ) # De 4 första jämna kvadraterna som svart ('k') streckad linje ('--') och runda ringar ('o')
#jamna_kvadraterna()
"""====================================================="""
def fibonacci_talen_red_h():
    plt.plot([0,1,1,2,3,5,8,13,21,34], 'rh') # De 10 första Fibonacci-talen som röda ('r') hexagoner ('h')
#fibonacci_talen_red_h()
""" =========================================================="""
def tva_rader_av_fonster():
    plt.subplot(2, 1, 1) # Skapa två rader av fönster (i en kolumn) och aktivera första
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'k--o' ) # Plottar i första fönstret
    plt.subplot(2, 1, 2) # Aktivera andra fönstret
    plt.plot([0,1,1,2,3,5,8,13,21,34], 'rh')# Plottar i andra fönstret
#tva_rader_av_fonster()
"""============================================================="""
def aktivera_den_valda_figuren():
    plt.figure(1) # Skapa och aktivera den första figuren
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'k--o' ) # Plottar i första figuren
    plt.figure(2) # Skapa och aktivera den andra figuren
    plt.plot([0,1,1,2,3,5,8,13,21,34], 'rh') # Plottar i andra figuren
#aktivera_den_valda_figuren()
"""================================================================="""
def listorna_med_texten_som_label():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'k--o', label='Jämna kvadrater' ) 
    plt.plot([0,1,1,2,3,5,8,13,21,34], 'rh', label='Fibonacci') 
    plt.title('Kvadrater och Fibonacci') # Sätt en titel
    plt.axis([-1,10,-1,40]) # Ange gränser för x och y i fönstret
    plt.xlabel('x-värdena') # Text längs x-axeln
    plt.ylabel('y-värdena') # Text längs y-axeln
    plt.legend() # Förklaring till de olika listorna med texten som angavs som 'label' i kommandot plot
#listorna_med_texten_som_label()
"""===================================================================="""
def sinus_alla_x_varden(): 
    x = np.linspace(0,2 * np.pi, 200) # Skapa lista med 200 jämnt fördelade tal från 0 till 2(pi)
    y = np.sin(x) # Beräkna sinus av alla värden i x
    plt.plot(x, y, 'r-.') # Plotta sinus från 0 till 2pi med röda streck/punkt-linje
    print(x[-1] - 2 * np.pi) # Sista värdet i x är 2pi
#sinus_alla_x_varden()
"""===================================================================="""

def sinus_cos_tan_activeted_windows():
    x = np.linspace(0,2 * np.pi, 200) # Skapa lista med 200 jämnt fördelade tal från 0 till 2(pi)
    
    plt.subplot(2,2,1) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera första
    plt.plot(x, np.sin(x), 'r-.') # Plotta sinus från 0 till 2pi med röda streck/punkt-linje
    plt.title('sin')
    
    plt.subplot(2,2,2) # Aktivera andra fönstret
    plt.plot(x, np.cos(x), 'g--') # Plotta cosinus från 0 till 2pi med gröna streck
    plt.title('cos')
    
    plt.subplot(2,2,3) # Aktivera tredje fönstret
    plt.plot(x, np.tan(x), 'y-') # Plotta tangens från 0 till 2pi med gul linje
    plt.title('tan')
    
    plt.subplot(2,2,4) # Aktivera fjärde fönstret
    x = np.linspace(np.pi/2 + 1e-5,3 * np.pi/2 - 1e-5, 200) # Skapa lista med 200 jämnt fördelade tal från pi/2 till 3pi/2 (men undvik ändpunkter)
    plt.plot(x, np.tan(x), 'y-') # Plotta tangens från pi/2 till 3pi/2 (undviker ändpunkter och skär av höga värden) med gul linje
    plt.axis([1,5,-10,10])              # Skär av höga och låga värden genom att bara visa mellan -10 och 10
    plt.title('tan')
#sinus_cos_tan_activeted_windows()
"""======================================================"""
def cirkeldiagram_med_pie():
    x = [10, 15, 25, 5, 45]  # Värdena som ska illustreras i diagrammet
    namn = ['Fysik', 'Kemi', 'Biologi', 'Annat', 'Matematik']  # Kategori för de olika värdena
    plt.pie(x, labels=namn)   # Rita upp cirkeldiagrammet
    plt.title('Mitt favoritämne')  # Lägg till en titel
#cirkeldiagram_med_pie()
"""======================================================"""
def histogram_slumptal():
    from numpy import random # Funktioner för att arbeta med slumptal
    
    x = random.randint(10, size=50) # Skapa ett fält med 50 slumpheltal n med 0 <= n <10 
    plt.hist(x) # Rita histogram av värdena i listan med slumptal
#histogram_slumptal()
"""======================================================"""
def scatter_tva_dimensionell_digram():
    import matplotlib.pyplot as plt
    from numpy import random # Funktioner för att arbeta med slumptal
    
    x = random.rand(500) # Skapa ett fält med 500 slumpflyttal n med 0 < n < 1 
    y = random.rand(500) # Skapa ett fält med 500 slumpflyttal n med 0 < n < 1 
    farg = np.arctan(x/y) # Skapar lista med vinkeln mellan x-axeln och linjen till respektive punkt
    storlek = 50 * np.sqrt(x**2 + y**2) # Skapar lista med avstånden till origo
    plt.scatter(x, y, c = farg, s = storlek, alpha = 0.5) # Plotta cirklar med färg baserat på vinkel 
                                                       # och storlek baserat på avstånd från origo
                                                       # alpha = 0.5 gör dem transparenta
#scatter_tva_dimensionell_digram()
"""======================================================"""

