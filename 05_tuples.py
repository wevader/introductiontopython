## Tuples // es un cojunto de valores ##

my_tuple = tuple()
my_other_tuple = ("Rojo", 'Azul')

my_tuple = (37, 1.78, "Daniel", "Mendez")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Daniel")) #numero de veces que se repite un elemento 
print(my_tuple.index("Daniel"))

##my_tuple[1] = 1.80 ## en un  tuple no es posible reasignar valores
print(my_tuple)

my_new_tuple = my_tuple + my_other_tuple
print(my_new_tuple) ## es posible unir tuples

my_tuple = list(my_tuple) ## se cambio a a typo list para poder modificar

print(my_new_tuple[3:5]) ##cortar del indice 3 al 5 sin contar el 5

my_tuple[2] = "Torres"
my_tuple.insert(1, "Torres")
my_tuple = tuple(my_tuple) ## se cambio nuevamente a tipo tuple
print(my_tuple)
print(type(my_tuple))

del my_tuple[1] #TypeError: 'tuple' object doesn't support item deletion --- no es pósible borrar un solo elemento

del my_tuple
#print(my_tuple) ##NameError: name 'my_tuple' is not defined --- fue borrada en la linea anterior