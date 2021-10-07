# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 21:57:38 2021

@author: javie
"""

class Humano:
    def __init__(self, edad):
        self.edad = edad
    
    def hablar(self, mensaje):
        print(mensaje)
        
    
pedro = Humano(26)
raul = Humano(21)

print("Soy Pedro y tengo", pedro.edad)
print("Soy Raúl y tengo", raul.edad)

pedro.hablar("Hola")
raul.hablar("Hola, Pedro")

#%%

class Fraccion:
    
    def __init__(self, num=0, den=1):
        if isinstance(num,int):
            self.num = num
        else:
            self.num = 0
        if isinstance(den,int) and den !=0:
            self.den = den
        else:
            self.den = 1
        
    def __del__(self):
        print("Destruyendo el objeto")
        
    def imprime(self):
        print("{", self.num, "/",self.den, "}")
        
    def multiplicar(self, b):
        n = self.num * b.num
        d = self.den * b.den
        r = Fraccion(n,d)
        return r
    
    def sumar(self):
        
#def main():
   #a = Fraccion(5,7)
   #a.imprime()
         
#a = Fraccion(3,2)
#a.imprime()
#b = Fraccion(7, 4)
#b.imprime()
#r = a.multiplicar(b)
#r.imprime()
a = Fraccion()
a.imprime()



#%%
class Lampara:
    Estados = ["on", "off"]
    def __init__(self, esta_encendida):
        self.esta_encendida = esta_encendida
    
    def muestra_lampara(self):
        if self.esta_encendida == True:
            print(self.Estados[0])
        else:
            print(self.Estados[1])
            
    def encender(self):
        self.esta_encendida = True
        self.muestra_lampara()
        
    def apagar(self):
        self.esta_encendida = False
        self.muestra_lampara()
    
a = Lampara(False)
a.muestra_lampara()

#%%

import numpy as np #importar librería numpy

x = np.array([1,2,3,4,5])
print(np.sqrt([1,2,3,4,5]))
print(x)
print(np.array([1,2,3])*np.array([1,2,3])
      
lista1 = [1, 2, 3, 4, 5] #def de lista
arreglo1 = np.array([1,2,3,4,5]) #def de arreglo

for i in lista1:
    print(i)





#for item in reversed([1,2,3]):
#    print(item)
        