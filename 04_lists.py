### lists ###

my_list = list()
my_other_list = []


print(len(my_list))

my_list = [35, 24, 52, 30, 17, 30, 30]

print(len(my_list))

my_other_list = [37, 1.77, "Daniel", "Mendez"]

print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_list.count(30))

age, height, name, surname = my_other_list

print(age)

my_other_list.append("wevader")
print(my_other_list)

my_other_list.insert(1, "wevader")
print(my_other_list)

my_other_list.remove("wevader")
my_list.remove(30)
print(my_other_list)
print(my_list)

my_other_list.pop()
print(my_other_list)

my_pop_element = my_other_list.pop(2) ## pop quita el elemento y lo puedes guardar
print(my_pop_element)

del my_list[2] # eliminas un elemento por indice

my_list.clear() # elimina la lista
print(my_list) 

my_other_list[1] = "rojo" # cambiar valor de un elemnto por indice
print(my_other_list)

print(my_list + my_other_list)

print(name)

my_list = "hola python"
print(my_list)
print(type(my_list)) # solo hay variables, se puede cambiar el valor por error

my_new_list = my_other_list.copy()

my_other_list.clear()
print(my_other_list)
print(my_new_list)

my_new_list.reverse() #ordena los elemntos a la inversa
print(my_new_list)

my_new_list = [30, 45, 1, 4, 100]

my_new_list.sort() # ordena elementos
print(my_new_list)

print(my_new_list[1:3])