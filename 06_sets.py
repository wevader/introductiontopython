### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set)) #<class 'set'>
print(type(my_other_set)) #<class 'dict'> es normal que lo identifique de este tipo

my_other_set = { "Daniel", "Mendez", 37 } 
print(type(my_other_set)) #<class 'set'>

print(len(my_other_set))

my_other_set.add("Torres")
print(my_other_set) # Un set no es una estructura ordenada  --- {'Daniel', 'Mendez', 37, 'Torres'}

my_other_set.add("Torres")
print(my_other_set) # un set no admite repedidos --- {'Torres', 'Daniel', 37, 'Mendez'}

print("Daniel" in my_other_set) ## existe el elemento Daniel en el set --- True
print("Danie" in my_other_set)  ## --- False

my_other_set.remove("Daniel") ## se borro elemento Daniel
print(my_other_set)  ## {'Torres', 'Mendez', 37}

my_other_set.clear()
print(len(my_other_set)) ## 0

del my_other_set ## boramos el ser --- ya no existe!!!
#print(my_other_set) ## NameError: name 'my_other_set' is not defined

my_set = {'Victor', 'Torres', 1.78}
my_list = list(my_set) ## muy arriesgado hacer esto ---
print(my_list)
print(my_list[0])

my_other_set = {'JavaScript', 'Python', 'C++'}

my_new_set = my_set.union(my_other_set) ## une dos sets
print(my_new_set) ## {1.78, 'C++', 'JavaScript', 'Python', 'Torres', 'Victor'}

print(my_new_set.union(my_new_set)) ## no se aceptan duplicados --- {1.78, 'JavaScript', 'Torres', 'C++', 'Victor', 'Python'}
print(my_new_set.union({"HTML", "React"})) ## {1.78, 'JavaScript', 'Torres', 'React', 'C++', 'Victor', 'HTML', 'Python'}

print(my_new_set.difference(my_set)) ### quitamos solo my_other_set --- {'JavaScript', 'C++', 'Python'}