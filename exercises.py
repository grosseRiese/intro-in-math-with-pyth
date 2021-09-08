# -*- coding: utf-8 -*-
"""
Spyder Editor

This is exercise script file.
"""


print("____________________________________________________")
def first_exercise():
    print("==============  O1 ================");
    x = 3
    y = 8
    z = 12
    
    S = x + y + z
    P = x * y * z
    
    sum_in_string = "Summan of  {} + {} + {} = {} .".format(x,y,z, S)
    product_in_string = "Prroduct of  {} * {} * {} = {} .".format(x,y,z, P)
    #print("Summan av : ",{x , y , z} ," is ", S)
    #print("Product P: ", P)
    
    print(sum_in_string)
    print(product_in_string)
    """
    a = (x,y,z)
    print(sum(a))
    """
first_exercise()

print("____________________________________________________")
def second_exercise():

    import math
    print("============== O2 ================");
    
    v1 = 0
    v2 = 30
    v3 = 60
    v4 = 90
    
    # second_ovning(v1 = 0,v2 = 30,v3 = 60,v4 = 90)
    print("Radians cos {} : " .format(v1), ( math.cos( math.radians(v1) ) ) ) 
    print("Radians cos {} : " .format(v2), ( math.cos( math.radians(v2) ) ) )
    print("Radians cos {} : " .format(v3), ( math.cos( math.radians(v3) ) ) )
    print("Radians cos {} : " .format(v4), ( math.cos( math.radians(v4) ) ) )
    print("       -----------     ")
    print("Radians sin {} : " .format(v1), ( math.sin( math.radians(v1) ) ) )
    print("Radians sin {} : " .format(v2), ( math.sin( math.radians(v2) ) ) )
    print("Radians sin {} : " .format(v3), ( math.sin( math.radians(v3) ) ) )
    print("Radians sin {} : " .format(v4), ( math.sin( math.radians(v4) ) ) )
    print("       -----------     ")
    print("Radians tan {} : " .format(v1), ( math.tan( math.radians(v1) ) ) )
    print("Radians tan {} : " .format(v2), ( math.tan( math.radians(v2) ) ) )
    print("Radians tan {} : " .format(v3), ( math.tan( math.radians(v3) ) ) )
    print("Radians tan {} : " .format(v4), ( math.tan( math.radians(v4) ) ) )
    print("Resultatet blir inte helt right ...!")
second_exercise()

print("____________________________________________________")
def quadratic_equation():
    import math
    print("============== O3 ================");
    # x^2 +px + q = 0
    #x = -p/2 (+/-) sqrt( (p/2)^2 -q ) 
    
    p = int(input("Input p coefficient : ") )
    q = int(input("Input q coefficient : ") )
    D =  ( pow((p/2),2) - q )
    # (p/2)**2 ==  pow((p/2)
    
    x_1 = -(p/2)+ math.sqrt( abs(D) )
    x_2 = -(p/2)- math.sqrt( abs(D) )
    
    print("First root to x: ", x_1)
    print("Second root to x: ", x_2)  
quadratic_equation()

#print("Power ", pow(3,2)) 
#print("** the same pow()  ", 4 ** 2)
print("____________________________________________________")