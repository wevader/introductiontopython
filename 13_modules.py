  ### modules ### para conectar varios ficheros y llamar funciones

import modules, ten_functions ## el modulo puede ser un libreria externa, de python, creada por alguien mas
from ten_functions import sum_two_values, sum_two_values_with_return ## podemos llamar la funcion directamente de otra libreri

modules.sumValues(10, 10 , 10)

ten_functions.print_name_with_default("daniel", "mendez", "wevader")

sum_two_values(23, 43)


import math

print(math.pi) #valor de pi
print(math.pow(2, 8)) #potencia 2 elvado a la 8

from math import pi as Pi_Value ## se puede traer un valor en especifico de una libreria de python y reasignar el valor

print(Pi_Value)
