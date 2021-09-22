# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:06:10 2021

@author: The GrosseReise
"""

# ***********__ PRAXIS __*******************
"""     1. Lista, for-loop, slumptal """

def positivt_heltal():
  try:
      input_num = input("Enter a number: ")
      input_num = abs(int(input_num))
      
      if input_num == 0:
        print("The number {} is not positive.".format(input_num))
        return input_num
      else:
        print("The positive ,(abs), nummer is : {} \n ".format(input_num))
     
  except ValueError:
      print("%s is not an integer.\n" % input_num)  
#positivt_heltal()

def list_random_nums():
  import random  # Modul för att använda slumptal
  list = []
  n = 0
  while n <= 15:
      my_nums = random.randint(1,100) # Ger ett slumpheltal n som uppfyller a<=n<=b
      list.append(my_nums)
      n += 1
  print("List with random numbers :\n {}".format(list))
#list_random_nums()

def sum_and_avrage():
    n_list = [20,49,75,45,3,91]
    """
    summan = 0
    avrage = 0
    for i in n:
     summan += abs(i)
    """
     
    summan = sum(n_list)
    avg = summan/len(n_list)
    
    print("The sum of {} = {}".format(n_list , summan))
    print("The avrage of the numbers = {}".format(avg))  
#sum_and_avrage()    

def sum_grans():
   import math
   try:
      input_num = input("Enter a number: ")
      input_num = abs(int(input_num))
      
      if input_num == 0:
        print("The number {} is not positive.".format(input_num))
        
      else:
        print("The positive ,(abs), nummer is : {} \n ".format(input_num))
        sum_n = 0
        k = 1
        for i in range(k,input_num + 1):
          sum_n += math.log(i,math.e)  # ln(i) = math.log(i,math.e)
          
        sum_n = sum_n 
        if sum_n >= input_num: 
          print("suamman: ", sum_n )    
          print("Den mista heltal n är : {}".format(input_num))
        else:
          print("suamman: ", sum_n )    
          print("{} är inte den minsta tal !! ".format(i)) 
              
        """
        while sum_n >= input_num :  
          print("suamman: ", sum_n )    
          print("Den mista heltal n är : {}".format(input_num))
        print("suamman: ", sum_n )    
        print("{} är inte den minsta tal !! ".format(input_num))"""
   except ValueError:
      print("%s is not an integer.\n" % input_num) 
#sum_grans()    

def mangder_set():
  import random as rdm  # Modul för att använda slumptal
  
  list_A = set({})
  list_B = set({})
  
  for i in range(1,21):
     my_nums_a = rdm.randint(1,100)# Ger ett slumpheltal n som uppfyller a<=n<=b 
     my_nums_b = rdm.randint(1,100)
     list_A.add(my_nums_a)
     list_B.add(my_nums_b)
     #print(i)
     
  print("A length : {}".format(len(list_A)) )
  print("A list with random numbers : {}".format(list_A)) 
  print("B length : {}".format(len(list_B)) )
  print("B list with random numbers : {}".format(list_B))  
  
  set3 = list_A.union(list_B)
  print("\nAntalet element i SET3: {} \n".format(len(set3)) )
  print("Set3 is list_A union list_B: \n" ,set3)
  
  # __* Find the A snitt B *__
  set4 = set({})
  for el in list_A:
     for ind in list_B:
         if el == ind:
             set4.add(el)
  print("\nSET4 is list_a snitt list_b: ", set4)
  print("\nAntalet element i set4: {} ".format(len(set4)) )
#mangder_set()    

#==========================================

# examplar section #
def logiska_operatorer():
    P = True
    Q = False
    X = P and Q
    Y = P or Q
    Z = not P
    V = 6 < 7
    W = 6 == 7
    
    print("P : {} \n".format(P))
    print("Q : {} \n".format(Q))
    print("X : P and Q => {} \n".format(X))
    print("Y : P or Q => {} \n".format(Y))
    print("Z : not P {} \n".format(Z))
    print("V : 6 < 7 {} \n".format(V))
    print("W : 6 == 7 {} \n".format(W))  
#logiska_operatorer()

def listor():
    lista1 = [True, 5, 7, 'Stefan']
    print(lista1[1])
    print(lista1[-1])
    print(lista1[1:3])
    
    lista2 = lista1  # lista1 och lista2 blir två olika namn på samma lista
    lista3 = lista1.copy() # lista1 och lista3 blir två olika listor
    
    lista1[0] = False
    lista1.append(7)
    lista1.remove(5)
    lista1.pop(0) # deleted the fst:element
    
    print(lista1)
    print(lista2)
    print(lista3)
    
    print([1, 3] == [1, 3])
    print([1, 3] == [3, 1])
#listor()

def quantities():
    mängd1 = {1, 7, 5}
    mängd2 = {5, 1, 5}
    mängd3 = {2, 4, 7}
    
    print(mängd2.issubset(mängd1)) #delmängd
    print(mängd1.union(mängd3)) #union
    print(mängd1.intersection(mängd3)) #snitt
    print(mängd1.difference(mängd3)) #A \ B
    
    mängd4 = mängd1 # mängd1 och mängd4 blir två olika namn på samma mängd
    mängd5 = mängd1.copy()  # mängd1 och mängd5 blir två olika mängder
    mängd1.remove(5)
    mängd1.add(10) 
#quantities()

def conditions():
    a = int(input("Mata in ett heltal: "))
    b = int(input("Mata in ett heltal: "))
    if a > b:   # Om a > b är sant så gör alla indenterade rader under här
        print(a, "är större än", b)
        print("så", a, "-", b, "> 0")
    elif a < b:  # Annars, om a < b är sant så gör alla indenterade rader under här
        print(a, "är mindre än", b)
        print("så", a, "-", b, "< 0")
    else:    # Annars gör alla indenterade rader under här
        print(a, "är lika med", b)
        print("så", a, "-", b, "= 0")
    print ("Nu var if-satsen slut.")
#conditions()

def while_loop():
   # Bestäm det minsta talet n>1 sådant att 2^n > n^5
    n = 2
    print(n**5 , 2**n)
    while n**5 >= 2**n: # Upprepa tills villkoret n**5 >= 2**n är falskt
        n += 1  # Öka n med 1
        print(n**5 , 2**n)
    print("Det minsta heltal n>1 sådant att 2^n > n^5 är", n)
#while_loop()

def for_loop():
    start = 1  # Första talet i range(start, slut, steg)
    slut = 15  # Slutvärdet i range(start, slut, steg) (som INTE inkluderas)
    steg = 2  # Steget mellan talen i range(start, slut, steg)
    summa = 0
    for i in range(start, slut, steg): # Upprepa för alla värden i range(...)
        print(i)
        summa += i
    print("Summan är", summa)
#for_loop()

