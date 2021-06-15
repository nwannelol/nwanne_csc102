# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 16:28:10 2021

@author: SST-LAB
"""


class Orange:
 orangecount = 0    
 def __init__(self,orange):
        self.orange = orange
        
            
        Orange.number_of_oranges = 10
        

customer1 = Orange(2)
if (customer1.orange > Orange.number_of_oranges):
     print ("sorry, amoount of oranges requested is greater than that in stock")
else:
     print("Oranges added to cart. Thank you for shopping")
 
     print(customer1.orange)