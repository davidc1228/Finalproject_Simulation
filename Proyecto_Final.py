#!/usr/bin/env python
# coding: utf-8

# La forma de aplicarlo es creando un conjunto de propuestas como solución al problema, cada solución será un individuo de la población. 

# In[56]:


import numpy as np
from math import pi, pow
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Circle


# Una generación en un algoritmo genético es una población diferente, donde en cada generación se realiza una evaluación para determinar cuál es la solución que más se acerca a lo óptimo.

# Al crear una nueva generación los individuos sufren de mutación, que realmente es lo que aporta nuevas soluciones posibles al problema y a lo largo del tiempo se encontrará la mejor.

# In[158]:


modelo = [1,1,1,1,1,1,1,1,1,1] #Objetivo a alcanzar
#La longitud del material genetico de cada individuo
largo = 10
#La cantidad de individuos que habra en la poblacion
num = 10 
#Cuantos individuos se seleccionan para reproduccion. Necesariamente mayor que 2
pressure = 3 
 #La probabilidad de que un individuo mute
mutation_chance = 0.4
  
print("\n\nModelo: %s\n"%(modelo))
  
def individual(min, max):
     return[random.randint(min, max) for i in range(largo)]
  
def crearPoblacion():
    return [individual(1,9) for i in range(num)]
  
def calcularFitness(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelo[i]:
            fitness += 1
  
    return fitness
  
def selection_and_reproduction(population):
    #Calcula el fitness de cada individuo, y lo guarda en pares ordenados de la forma (i , [1,2,1,1,4,1,8,9,4,1])
    puntuados = [ (calcularFitness(i), i) for i in population]
    #Ordena los pares ordenados y se queda solo con el array de valores
    puntuados = [i[1] for i in sorted(puntuados)] 
    population = puntuados
  
  
  #Esta linea selecciona los 'n' individuos del final, donde n viene dado por 'pressure'
    selected =  puntuados[(len(puntuados)-pressure):] 
  
  
  
    #Se mezcla el material genetico para crear nuevos individuos
    for i in range(len(population)-pressure):
        #Se elige un punto para hacer el intercambio
        punto = random.randint(1,largo-1) 
        #Se eligen dos padres
        padre = random.sample(selected, 2) 
          
            #Se mezcla el material genetico de los padres en cada nuevo individuo
        population[i][:punto] = padre[0][:punto] 
        population[i][punto:] = padre[1][punto:]
  
 #El array 'population' tiene ahora una nueva poblacion de individuos, que se devuelven
    return population 
  
def mutation(population):
    """
        Se mutan los individuos al azar. Sin la mutacion de nuevos genes nunca podria
        alcanzarse la solucion.
    """
    contador = 0
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: #Cada individuo de la poblacion (menos los padres) tienen una probabilidad de mutar
            punto = random.randint(0,largo-1) #Se elgie un punto al azar
            nuevo_valor = random.randint(1,9) #y un nuevo valor para este punto
            #Es importante mirar que el nuevo valor no sea igual al viejo
            while nuevo_valor == population[i][punto]:
                nuevo_valor = random.randint(1,9)
  
            #Se aplica la mutacion
            population[i][punto] = nuevo_valor
            if nuevo_valor == population[i][punto]:
                contador = contador +1

  
    return population, contador
      
  
  
population = crearPoblacion()#Inicializar una poblacion
print("Poblacion Inicial:\n%s"%(population)) 
  
  
#Se evoluciona la poblacion
for i in range(100):
    population = selection_and_reproduction(population)
    population = mutation(population)[0]
  
print('arr\n', mutation(population)[1])
print("\nPoblacion Final:\n%s"%(population))
print("\n\n")


# In[ ]:





# In[ ]:




